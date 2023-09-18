from tkinter import *

windows = Tk()
windows.title("My first GUI Program")
windows.minsize(width=500, height=300)
windows.config(padx=100, pady=100)

# Label
my_label = Label(text="I am a Label", font=('Arial', 24, "bold"))
# my_label.pack()
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New text")

# Button


def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

# Button
button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# New Button
new_button = Button(text="Click me", command=button_clicked)
# button.pack()
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=20)
# input.pack()
input.grid(column=3, row=2)

windows.mainloop()
