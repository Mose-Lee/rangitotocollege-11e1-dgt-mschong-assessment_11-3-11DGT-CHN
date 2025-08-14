from tkinter import *
win = Tk()
win.title("Mose")
win.geometry("500x400")
#label


#entry
entry = Entry(win, width=30,font=("Arial", 14))
entry.pack()
#def help function
def help():
    text = entry.get()
    if text:
        btn.config(text="You entered: " + text)
        print("You entered:", text)
    else:
        print("please enter something")
#button
btn = Button(win)
btn.config(text="Click Here")
btn.config(command=help)
btn.pack()

win.mainloop()
  
