'''This program tells the position and RGB at current coordinates of your mouse.'''

import pyautogui
from Tkinter import *
from time import sleep

def Start(pos):
    pyautogui.FAILSAFE = False
    global root, running
    im=pyautogui.screenshot()
    pos['text']=str(pyautogui.position())
    rgb['text']=str(im.getpixel(pyautogui.position()))
    root.update_idletasks()
    root.after(10, lambda:Start(pos))

s= "Screen Resolution-"+ str(pyautogui.size())
root=Tk()
root.minsize(width=310, height="20")
root.title("Where is my mouse? RGB?")
Label(root, text=s, font="Verdana 10 bold").pack()

Label(root, text='Mouse Position-', font="Verdana 10 bold").pack()
pos=Label(root, text='Starting...', font="Verdana 20 bold")
pos.pack()
Label(root, text='RGB at this point-', font="Verdana 10 bold").pack()
rgb=Label(root, text='Starting...', font="Verdana 20 bold")
rgb.pack()
Label(root, text="-Tushar", font="Verdana 10 bold").pack()
Start(pos)
root.mainloop()
