import tkinter
import os

os.system("clear")

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(400,400)


# Label
my_label = tkinter.Label(text="I am a label",font=("Arial", 34,"bold"))

my_label.pack()
my_label.config(text = "New text with config")


def button_click():
    ans = inp.get()
    my_label["text"] = ans


button = tkinter.Button(text="Click ME!",command=button_click)
button.pack()

inp = tkinter.Entry(width=10)
inp.pack()



# all ways on the end
window.mainloop()