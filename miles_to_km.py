from tkinter import *

CONVERSTION_CONSTANT = 1.609347218694


def calculate_km_on_click():
    nr_of_miles = int(miles_input.get())
    nr_of_km = nr_of_miles * CONVERSTION_CONSTANT
    result_label.config(text=f"{nr_of_km}")


windows = Tk()
windows.title("Mile to km Converter")
windows.minsize(width=300, height=100)
windows.config(padx=20, pady=20)

# Miles LABEL
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Entry (nr of miles)
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Equal LABEL
miles_label = Label(text="is equal to")
miles_label.grid(column=0, row=2)

# Result LABEL
result_label = Label(text="0")
result_label.grid(column=1, row=1)

# Km LABEL
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate BUTTON
calculate_button = Button(text="Calculate", command=calculate_km_on_click)
calculate_button.grid(column=1, row=2)

windows.mainloop()
