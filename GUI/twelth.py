from tkinter import *
import tkinter.messagebox

root =Tk()
tkinter.messagebox.showinfo('Window Title','Abhinandan you are right')
answer = tkinter.messagebox.askquestion('Question 1','Do you Like silly Faces?')
if answer == 'yes':
	print("B--D")
root.mainloop()