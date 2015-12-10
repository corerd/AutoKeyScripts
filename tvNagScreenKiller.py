# TeamViewer sponsored session auto-close
# link: https://autohotkey.com/board/topic/113190-teamviewer-sponsored-session-auto-close-nag-screen-killer/

# Wait for a specific window
# RegX: http://stackoverflow.com/a/9350443

import time

WAIT_TIMEOUT = 30
wtitle = 'Sponsored session'
wclass = 'TeamViewer.exe.Wine'
wtitle_regx = '(.*?%s*)' % wtitle
wfound = False
while not wfound:
    # Wait for window with the given wtitle and wclass
    wexist = window.wait_for_exist(wtitle_regx, WAIT_TIMEOUT)
    if not wexist:
        break
    window.activate(wtitle)
    time.sleep(1)
    if wclass == window.get_active_class():
        wfound = True
if wfound is True:
    keyboard.send_keys('<enter>')
