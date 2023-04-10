import tkinter


window = tkinter.Tk()
window.title("M to Km")
window.minsize(250,160)

###
def calc():
    ans = float(inp.get())
    label_ans["text"] = round(ans*1.6, 1)

inp = tkinter.Entry(width=10)
inp.place(x=30,y=30)

label_miles = tkinter.Label()
label_miles["text"] = "Miles"
label_miles.place(x=160,y=30)


label_eq = tkinter.Label()
label_eq["text"] = "is equal to"
label_eq.place(x=30,y=60)

label_ans = tkinter.Label()
label_ans["text"] = "0.0"
label_ans.place(x=110,y=60)

label_km = tkinter.Label()
label_km["text"] = "Km"
label_km.place(x=160,y=60)


button = tkinter.Button(text="Calc!",command=calc)
button.place(x=110,y=100)
#label
#label
#label
#button

###
window.mainloop()