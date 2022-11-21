from tkinter import *

window = Tk()
window.title("Tkinter test")
window.config(padx=10, pady=10)

distance = Entry(width=30, )
distance.grid(column=1, row=0)

def calcul():
    r = distance.get()
    if r.isdigit():
        r = round(int(r) * 1.609)
    result_display.config(text=r)


miles = Label(text="Miles")
miles.grid(column=2, row=0)


result = Label(text="Is equal to")
result.grid(column=0, row=1)

result_display = Label(text=00)
result_display.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calcul)
calculate_button.grid(column=1, row=2)
def calcul():
    return int(distance.get())
























window.mainloop()
