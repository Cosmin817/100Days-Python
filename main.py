from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    # print(f"Your password is: {password}")
    password_entry.insert(index=0, string=f'{password}')
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    user_input_website = str(website_entry.get())
    user_input_email = str(email_entry.get())
    user_input_password = str(password_entry.get())
    warning_exists = 0

    warning_label = Label(text="", width=17)
    warning_label.grid(row=4, column=3)

    if (not user_input_password) or (not user_input_email) or (not user_input_password):
        messagebox.showerror(title="Error", message="There are empty fields !")
        warning_exists += 1
        return 0
    else:
        warning_exists = 0

    is_ok = messagebox.askokcancel(title=user_input_website,
                           message=f"Confirm:\n\nWebsite: {user_input_website}\n"
                                   f"Email: {user_input_email}\n"
                                   f"Password: {user_input_password}\n\nSave it or not ?"
                           )

    if is_ok:
        with open('data.txt', 'a') as data_file:
            data_file.write(f"{user_input_website} | {user_input_email} | {user_input_password}\n")
        website_entry.delete(first=0, last='end')
        password_entry.delete(first=0, last='end')
        website_entry.focus()

        if warning_exists == 0:
            warning_label.config(text="", width=17)


# ---------------------------- UI SETUP ------------------------------- #

# Main window
window = Tk()
window.title('Password Manager')
window.configure(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0,)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=30)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=30)
email_entry.grid(column=1, row=2)
email_entry.insert(index=0, string='cosmincmc@gmail.com')

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", width=17, command=generate_password)
generate_password_button.grid(row=3, column=3)

add_button = Button(text="Add", width=25, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
