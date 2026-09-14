"""Independent language reproducer; does not load the guard or SFM."""
from __future__ import print_function
import json
import sys

prefix = 'def outer():\n    value = 1\n    def inner():\n        return value\n    namespace = {}\n'
results = {'python': sys.version.split()[0]}
for name, operation in (
    ('tuple_exec', "exec(compile('x=1', '<example>', 'exec'), namespace, namespace)"),
    ('eval_exec_code', "eval(compile('x=1', '<example>', 'exec'), namespace, namespace)"),
):
    source = prefix + '    ' + operation + '\n    return namespace["x"]\n'
    namespace = {}
    try:
        code = compile(source, '<' + name + '>', 'exec')
    except SyntaxError:
        results[name] = 'compile-fails'
    else:
        eval(code, namespace, namespace)
        assert namespace['outer']() == 1
        results[name] = 'works'
assert results['eval_exec_code'] == 'works'
if sys.version_info[:3] == (2, 7, 5):
    assert results['tuple_exec'] == 'compile-fails'
print(json.dumps(results, sort_keys=True, indent=2))
