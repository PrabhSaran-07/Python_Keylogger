from pynput.mouse import Listener

def mouse_position(x,y):#x->distance from left to write and y->distance from top to bottom
    print("Position of current mouse {0}".format((x,y)))
with Listener(on_move=mouse_position) as l:
    l.join()