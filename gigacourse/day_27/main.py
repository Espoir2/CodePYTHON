from tkinter import *

window = Tk()
window.title("Tkinter test")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

my_label = Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.grid(column=1, row=20)


def button_clicked():
    my_label_2 = Label(text=input.get(), font=("Arial", 24, "italic"))
    my_label_2.grid(column=1, row=10)
    # my_label_2["text"] = "New text"
    # my_label_2.config(text="New text config")


# Button
my_but = Button(text="Click me", command=button_clicked)
my_but.grid(column=1, row=1)
my_but.config(pady=5)

# Entry
input = Entry(width=50)
input.grid(column=1, row=6)


window.mainloop()
