REMOVE REMOVE WORKSHOP PROMPT - R3 MANUAL INSTALL

Automatically chooses Cancel on Source Filmmaker's exact
"Remove Unsubscribed And Deleted Workshop Files" startup window.

INSTALL

Extract this ZIP into SourceFilmmaker/game/. It installs one script at:

  usermod/scripts/sfm/autoinit/Remove_Remove_Workshop_Prompt.py

Choose one startup method:

1. Steam Launch Options:

   -sfm_startup_script "usermod/scripts/sfm/autoinit/Remove_Remove_Workshop_Prompt.py"

2. With KiwifruitDev Autoinit already installed, enable this script in
   Autoinit Manager. Autoinit is not included in this archive.

Restart SFM. Only one startup method is needed. Use the actual game-relative
file path if a different mod or Workshop installation placed your file elsewhere.

BEHAVIOR

Watching uses up to 40 seconds of eligible, unblocked polling time. Other
application-modal windows pause that budget. It is not a wall-clock deadline
or a project-open event hook. At most one cancellation attempt is made per
process, after conservative target and lifecycle checks. Uncertainty means
no action; a failed attempt is not retried.

Later removal windows are left alone after the attempt or after watching
stops. An intentional identical removal window opened while the guard is
still watching may also be cancelled.

VERIFICATION STATUS

Target: Python 2.7.5, PySide 1.2.0, Qt 4.8.3 in SFM.
Complete R3 compilation and isolated tests passed with bundled Python 2.7.5.
Project records report real-SFM qualification of the embedded standalone
guard. Complete real-SFM qualification of this exact R3 dual-host wrapper
remains outstanding; isolated tests do not establish live Qt behavior.

TROUBLESHOOTING / UNINSTALL

Log: C:\Users\Public\Documents\Remove_Remove_Workshop_Prompt.log
Review the log before sharing: it may include unrelated SFM window titles.
The historical host=-sfm_startup_script log label also appears under Autoinit.

Remove the launch option and/or disable this script in Autoinit Manager,
close SFM, and delete the installed file from its actual location. Restart
SFM; disabling discovery does not stop an already-installed runtime.

AUTHOR / LICENSE

ChadChan3D. Eligible original material: CC0-1.0.
See LICENSE and LICENSE_SCOPE.md. External products are not included or relicensed.
