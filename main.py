import requests
from tkinter import *


def get_kayne_quote():
    my_request = requests.get('https://api.kanye.rest')
    data_my_request = my_request.json()
    canvas.itemconfig(canvas_text, text=f'"{data_my_request["quote"]}"')


window = Tk()
window.config(padx=50, pady=50)
window.title("Kayne Says ...")

canvas = Canvas(width=400, height=415)
canvas_image = PhotoImage(file='./images/background.png')
canvas.create_image(200, 200, image=canvas_image)
canvas_text = canvas.create_text(200, 170, text="", width=250, font=('Arial', '15', 'bold'), fill='white')
canvas.grid(row=0, column=0)

kayne_button = Button()
kayne_button_image = PhotoImage(file='./images/kanye.png')
kayne_button.config(image=kayne_button_image, borderwidth=0, command=get_kayne_quote)
kayne_button.grid(row=1, column=0)

window.mainloop()
