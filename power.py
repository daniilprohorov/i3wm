#!/usr/bin/python3
from tkinter import *
import subprocess
def sleep(*args):
    subprocess.call(["systemctl", "suspend"])
    exit(0)

def hibernate(*args):
    subprocess.call(["systemctl", "hibernate"])
    exit(0)

def poweroff(*args):
    subprocess.call(["shutdown", "-h", "now"])
    exit(0)

def reboot(*args):
    subprocess.call(["reboot"])
    exit(0)


root = Tk()

button0=Button(root, text=' (h) Hibernate ', width=25, height=5, bg='black', fg='white', font='monospace 10', command=hibernate)
button0.pack(side='top')

button1=Button(root, text=' (s) Sleep ', width=25, height=5, bg='black', fg='white', font='monospace 10', command=sleep)
button1.pack(side='top')

button2=Button(root, text=' (p) Poweroff ', width=25, height=5, bg='black', fg='white', font='monospace 10', command=poweroff)
button2.pack(side='bottom')

button3 = Button(root, text=' (r) Reboot ', width=25, height=5, bg='black', fg='white', font='monospace 10', command=reboot)
button3.pack(side='bottom')

root.bind('h', hibernate)
root.bind('s', sleep)
root.bind('p', poweroff)
root.bind('r', reboot)

root.mainloop()

