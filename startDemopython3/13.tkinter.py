#!/usr/bin/python3

from tkinter import *

class Window(Frame):


	def __init__(self,master = None):
		Frame.__init__(self,master)
		self.master=master
		self.init_window()


	def init_window(self):
		self.master.title("GUI")
		self.pack(fill=BOTH,expand=1)
#		quitB=Button(self,text="quit",command=self.client_exit)
#		quitB.place(x=0,y=0)
		self.add_menu()

	def client_exit(self):
		exit();

	def add_menu(self):
		mainmenu=Menu(root, tearoff=0)
		self.master.config(menu=mainmenu)


		fileMenu=Menu(mainmenu)
		fileMenu.add_command(label="New", command=self.doNothing)
		fileMenu.add_command(label="Open", command=self.doNothing)
		fileMenu.add_command(label="Save", command=self.doNothing)
		fileMenu.add_command(label="Save as...", command=self.doNothing)
		fileMenu.add_command(label="Close", command=self.doNothing)


		projectMenu=Menu(mainmenu)
		projectMenu.add_command(label="java", command=self.doNothing)
		projectMenu.add_command(label="pyton", command=self.doNothing)
		projectMenu.add_command(label="ruby", command=self.doNothing)
		projectMenu.add_command(label="cpp", command=self.doNothing)
		projectMenu.add_command(label="c", command=self.doNothing)

		mainmenu.add_cascade(label='File',menu=fileMenu)
		mainmenu.add_cascade(label='Project',menu=projectMenu)

	def doNothing(self):
		print("doNoting")





root=Tk()

app=Window(root)

root.geometry("800x480")

root.mainloop()



