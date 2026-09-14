# SPDX-License-Identifier: CC0-1.0
# Standalone isolated checks; Python 2.7.5 and Python 3.
from __future__ import print_function
try:
    import builtins as __builtin__
except ImportError:
    import __builtin__
import ast
import hashlib
import json
import os
import sys
import types

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, '..', 'Remove_Remove_Workshop_Prompt.py')
source = open(PATH, 'rb').read()
compiled = compile(source, PATH, 'exec')
assert len(source) == 48019
assert hashlib.sha256(source).hexdigest() == '06c6654df735849fcd5ea4d3c437107ad358a23ba04c0a114fd902b0b9130356'
results = {'python': sys.version.split()[0], 'complete_artifact_compiles': True}
tree = ast.parse(source)
embedded = [ast.literal_eval(n.value) for n in ast.walk(tree) if isinstance(n, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == '_rrwp_guard_source' for t in n.targets)]
assert len(embedded) == 1 and type(embedded[0]) is str
body = embedded[0]
assert len(body) == 25077
assert hashlib.sha256(body.encode('ascii')).hexdigest() == '078555ae2b93e01462e40c019ca862dcb65ddf55c790e234e468b5832c838bfa'
results['embedded_fingerprint_matches'] = True

# Project-owned Qt stand-ins; never import a real PySide.
class Signal(object):
    def __init__(self): self.callbacks = []
    def connect(self, callback): self.callbacks.append(callback)

class Timer(object):
    def __init__(self):
        self.timeout = Signal()
        self.active = False
    def setInterval(self, value): self.interval = value
    def setSingleShot(self, value): self.single = value
    def start(self): self.active = True
    def stop(self): self.active = False

class QPushButton(object):
    def __init__(self, text): self.label, self.clicks = text, 0
    def text(self): return self.label
    def isVisible(self): return True
    def isEnabled(self): return True
    def isDefault(self): return self.label == 'OK'
    def autoDefault(self): return True
    def click(self): self.clicks += 1

class QDialogButtonBox(object):
    AcceptRole, RejectRole = 1, 2
    def __init__(self): self.controls = [QPushButton('OK'), QPushButton('Cancel')]
    def buttons(self): return self.controls
    def buttonRole(self, button):
        return self.AcceptRole if button.label == 'OK' else self.RejectRole

class QListWidget(object):
    def count(self): return 1

class QDialog(object):
    def __init__(self, title='Remove Unsubscribed And Deleted Workshop Files'):
        self.title = title
        self.box = QDialogButtonBox()
        self.items = QListWidget()
    def windowTitle(self): return self.title
    def metaObject(self): return types.SimpleNamespace(className=lambda: 'QDialog')
    def isVisible(self): return True
    def isEnabled(self): return True
    def isModal(self): return True
    def windowModality(self): return 2
    def findChildren(self, cls): return [self.box] if cls is QDialogButtonBox else [self.items]

class App(object):
    def __init__(self): self.modal, self.aboutToQuit = None, Signal()
    def activeModalWidget(self): return self.modal
    def thread(self): return 1

def blocked_open(*args, **kwargs):
    raise IOError('Mock denies all guard file access')

class Namespace(object):
    def __init__(self, **values): self.__dict__.update(values)
types.SimpleNamespace = Namespace
class QObject(object):
    def __init__(self): pass
class QEvent(object):
    Close, Hide, Destroy, WindowDeactivate = 1, 2, 3, 4
OriginalDialog = QDialog
class QDialog(OriginalDialog):
    def __init__(self):
        OriginalDialog.__init__(self)
        self.filters = []
        self.destroyed, self.finished = Signal(), Signal()
        self.accepted, self.rejected = Signal(), Signal()
    def installEventFilter(self, observer): self.filters.append(observer)
class CountTimer(Timer):
    created = []
    def __init__(self):
        Timer.__init__(self); CountTimer.created.append(self)
STATE = '_remove_remove_workshop_prompt_bootstrap_state'
IMPL = '_remove_remove_workshop_prompt_implementation'
RUNTIME = '_remove_remove_workshop_prompt_runtime'
checks = {}
def function_globals(function):
    return getattr(function, '__globals__', None) or function.func_globals
def check(name, value):
    assert value, name
    checks[name] = True
def fail(): raise RuntimeError('injected failure')
def environment(available=True, timer=CountTimer):
    for name in (STATE, IMPL, RUNTIME): sys.modules.pop(name, None)
    CountTimer.created = []
    app, availability = App(), [available]
    qtcore = Namespace(QTimer=timer, QObject=QObject, QEvent=QEvent,
        Qt=Namespace(ApplicationModal=2), QThread=Namespace(currentThread=lambda: 1))
    qtgui = Namespace(QPushButton=QPushButton, QDialogButtonBox=QDialogButtonBox,
        QListWidget=QListWidget, QApplication=Namespace(instance=lambda: app if availability[0] else None))
    sys.modules['PySide'] = Namespace(QtCore=qtcore, QtGui=qtgui)
    # Keep real builtins: substituting their dictionary triggers Python 2's
    # restricted-execution import rules. Deny logging in private globals instead.
    def private_eval(code, global_dict, local_dict):
        global_dict['open'] = blocked_open
        global_dict['unicode'] = type(u'')
        return eval(code, global_dict, local_dict)
    host = {'__builtins__': vars(__builtin__), '__name__': '__main__', 'eval': private_eval}
    return app, availability, host
def invoke(host):
    eval(compiled, host, host)

app, availability, host = environment()
eval_calls = []
def inspect_eval(code, global_dict, local_dict):
    eval_calls.append((isinstance(code, types.CodeType), global_dict is local_dict,
                       global_dict is sys.modules[IMPL].__dict__))
    global_dict['open'] = blocked_open
    global_dict['unicode'] = type(u'')
    return eval(code, global_dict, local_dict)
host['eval'] = inspect_eval
invoke(host)
impl, runtime = sys.modules[IMPL], sys.modules[RUNTIME]
check('eval receives code object and same private globals/locals', eval_calls == [(True, True, True)])
check('successful install READY', sys.modules[STATE].phase == 'READY' and runtime.installed)
functions = [v for name, v in vars(impl).items() if name != 'open' and isinstance(v, types.FunctionType)]
methods = [v for v in vars(impl._LifecycleSentinel).values() if isinstance(v, types.FunctionType)]
check('actual func_globals private', len(functions) > 10 and all(function_globals(f) is vars(impl) for f in functions + methods))
app.modal = QDialog(); impl._poll()
callbacks = sum([s.callbacks for s in (app.modal.destroyed, app.modal.finished, app.modal.accepted, app.modal.rejected)], [])
check('four nested lifecycle callbacks private', len(callbacks) == 4 and all(function_globals(f) is vars(impl) for f in callbacks))
snapshot = vars(runtime).copy()
invoke(host)
check('repeat does not execute body or reset state', len(eval_calls) == 1 and vars(runtime) == snapshot and len(CountTimer.created) == 1)
for name in ('_runtime','_poll','_write','_stop','_inspect_target','_EVENT_NAMES','TARGET_TITLE','QtCore','QtGui','time','traceback'):
    host[name] = None
runtime.poll_timer.timeout.callbacks[0]()
check('retained callback survives host pollution', runtime.attempt_consumed and app.modal.box.controls[1].clicks == 1)
check('post action callback private', function_globals(runtime.post_timer.timeout.callbacks[0]) is vars(impl))
snapshot = vars(runtime).copy(); timer_count = len(CountTimer.created)
invoke(host)
check('consumed attempt retained on repeat', vars(runtime) == snapshot and len(CountTimer.created) == timer_count)

class StartFails(CountTimer):
    def start(self): fail()
app, availability, host = environment(timer=StartFails)
invoke(host); runtime = sys.modules[RUNTIME]; snapshot = vars(runtime).copy()
invoke(host); invoke(host)
check('A timer start failure permanently latched', sys.modules[STATE].phase == 'FAILED_AFTER_EXECUTION' and len(CountTimer.created) == 1 and len(app.aboutToQuit.callbacks) == 1 and vars(runtime) == snapshot)

app, availability, host = environment(False)
invoke(host); impl = sys.modules[IMPL]; poll = impl._poll
check('clean prerequisite retryable', sys.modules[STATE].phase == 'READY_RETRYABLE')
availability[0] = True; invoke(host)
check('clean retry preserves private functions', sys.modules[STATE].phase == 'READY' and sys.modules[IMPL] is impl and impl._poll is poll and len(CountTimer.created) == 1)

app, availability, host = environment(False)
invoke(host); availability[0] = True; impl = sys.modules[IMPL]; original = impl._now_elapsed
impl._now_elapsed = fail
try: invoke(host)
except RuntimeError: pass
else: raise AssertionError('expected later install exception')
runtime = sys.modules[RUNTIME]; snapshot = vars(runtime).copy()
impl._now_elapsed = original; invoke(host); invoke(host)
check('B later install exception permanently latched', sys.modules[STATE].phase == 'FAILED_AFTER_EXECUTION' and len(CountTimer.created) == 1 and vars(runtime) == snapshot)

for stage in ('allocation', 'compile'):
    app, availability, host = environment()
    original_module_type = types.ModuleType
    foreign_runtime = original_module_type(RUNTIME)
    sys.modules[RUNTIME] = foreign_runtime
    def allocation(name, *args):
        if name == IMPL: raise MemoryError('allocation')
        return original_module_type(name, *args)
    def compilation(*args, **kwargs): raise MemoryError('compile')
    if stage == 'allocation': types.ModuleType = allocation
    else: host['compile'] = compilation
    try:
        try: invoke(host)
        except MemoryError: pass
        else: raise AssertionError('expected preexecution failure')
    finally: types.ModuleType = original_module_type
    check('C ownership cleanup ' + stage, STATE not in sys.modules and IMPL not in sys.modules and sys.modules[RUNTIME] is foreign_runtime)
    # Harness removes its own artificial runtime to permit a fresh install.
    sys.modules.pop(RUNTIME); host['compile'] = compile
    invoke(host)
    check('C safe retry ' + stage, sys.modules[STATE].phase == 'READY')


# Initial guard execution failure retains its module and permanently blocks.
app, availability, host = environment()
del sys.modules['PySide'].QtCore.QObject
try: invoke(host)
except AttributeError: pass
else: raise AssertionError('expected class-definition failure')
saved_impl = sys.modules[IMPL]
sys.modules['PySide'].QtCore.QObject = QObject
invoke(host)
check('initial execution failure stays blocked', sys.modules[STATE].phase == 'FAILED_AFTER_EXECUTION' and sys.modules[IMPL] is saved_impl and not CountTimer.created)

# Same-host synchronous re-entry is blocked while executing and retrying.
for phase in ('EXECUTING', 'RETRYING_INSTALL'):
    app, availability, host = environment(phase != 'RETRYING_INSTALL')
    if phase == 'RETRYING_INSTALL': invoke(host); availability[0] = True
    observed = []
    def reentrant_instance():
        observed.append(sys.modules[STATE].phase)
        invoke(host)
        return app
    sys.modules['PySide'].QtGui.QApplication.instance = reentrant_instance
    invoke(host)
    check('reentry blocked ' + phase, observed == [phase] and len(CountTimer.created) == 1 and len(app.aboutToQuit.callbacks) == 1)

# Budget and target continuity are retained safety boundaries.
app, availability, host = environment(); invoke(host)
impl, runtime = sys.modules[IMPL], sys.modules[RUNTIME]
for unused in range(161): impl._poll()
check('eligible polling budget stops at 40 seconds', runtime.stopped and runtime.unblocked_seconds == 40.0 and not runtime.attempt_consumed)
app, availability, host = environment(); invoke(host)
impl, runtime = sys.modules[IMPL], sys.modules[RUNTIME]
app.modal = QDialog(); app.modal.title = 'Unrelated dialog'
for unused in range(200): impl._poll()
check('unrelated modal pauses budget', runtime.unblocked_seconds == 0.0 and not runtime.stopped)
app.modal = QDialog(); impl._poll()
sentinel = runtime.confirmation_sentinel
app.modal.destroyed.callbacks[0]()
app.modal = QDialog(); impl._poll()
check('invalidated sentinel does not confirm replacement', app.modal.box.controls[1].clicks == 0 and not runtime.attempt_consumed)

# Source-level reproduction of the applicable literal Autoinit pass.
text = source.decode('ascii')
basename = 'Remove_Remove_Workshop_Prompt.py'
rewritten = text.replace('sfmApp.RegisterTabWindow(', '_autoinit_global.register_window("' + basename + '", ')
rewritten = rewritten.replace('sfmApp.ShowTabWindow(', 'pass #sfmApp.ShowTabWindow(')
check('applicable loader rewrite changes no bytes', rewritten == text and not any(basename.endswith(n) for n in ('quickmenu_v3.py','directional_scale_patch.py','sfm_flex_unlocker.py','light_limit_patch.py')))
results['checks'] = checks
results['passed'] = len(checks)
print(json.dumps(results, indent=2))
