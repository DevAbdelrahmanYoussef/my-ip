import os
import tkinter as tk
from tkinter import messagebox


app = tk.Tk()
app.title("what's my Ip")
def get_ip1():
	os.system('ifconfig|grep inet > ip1.txt')
	a = open('ip1.txt','r')
	for x in a :
		messagebox.showinfo('my ip',x)
btn = tk.Button(app,text='Get My Ip Linux',command=get_ip1).pack()
def get_ip2():
	os.system('ipconfig|grep inet > ip2.txt')
	a = open('ip2.txt','r')
	for x in a :
		messagebox.showinfo('my ip',x)
btn = tk.Button(app,text='Get My Ip windows',command=get_ip2).pack()
app.mainloop()