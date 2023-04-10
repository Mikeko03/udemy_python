import tkinter

def calc(miles:int):
    label
    return miles*1.6

print(calc(10))
# main window init and config
window = tkinter.Tk()
window.title("Mile to Kilometer converter")
window.minsize(width=500,height=500)

# adding label on top
my_label_1 = tkinter.Label(font=("Arial", 34, "bold"))
my_label_1["text"] = 
my_label_1.place(x=10,y=40)

button = tkinter.Button(text="Click ME!",command=calc)
button.pack()

entry = tkinter.Entry(width=5)
#entry.insert(-1, string = "Hello this is box" )
print(entry.get())
entry.place(x=195,y=150)



#text = tkinter.Text(width=30, height=3)
#text.focus()
#text.insert("1.0" ,"Hello There")
#text.pack()
#
#spinbox = tkinter.Spinbox(from_=0, to=10, width=5,)
#spinbox.pack()
#
#scale = tkinter.Scale(from_=100, to=0)
#scale.pack()


window.mainloop()