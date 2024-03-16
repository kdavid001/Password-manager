from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for items in range(randint(8, 10))]
    password_symbols = [choice(symbols) for items in range(randint(2, 4))]
    password_numbers = [choice(numbers) for items in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    # this next line automatically copies the generated password.
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    web = website.get()
    email = user.get()
    passw = password_entry.get()

    new_data = {
        web: {
            "email": email,
            "password": passw,
        }
    }

    if len(web) == 0 or len(email) == 0 or len(passw) == 0:
        messagebox.showinfo(title='Oops', message=f"Cannot save empty data \nEmail: {email} \n Password:{passw}")

    else:
        try:
            with open("data.json", "r") as data_file:

                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website.delete(0, END)
            password_entry.delete(0, END)

    # open and read the file after the appending:


# ---------------------------- search for password ------------------------------- #

def search():
    website_entry = website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title=website_entry,
                            message=f"No Results for '{website_entry}'\n check the spelling or try a new search")

    else:
        if website_entry in data:
            email = data[website_entry]["email"]
            password = data[website_entry]["password"]
            messagebox.showinfo(title=website_entry, message=f"\nEmail: {email} \n Password:{password}")
        else:
            messagebox.showinfo(title=website_entry,
                                message=f"No Results for '{website_entry}'\n check the spelling or try a new search")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="website:", fg="black", bg="white")
website_label.grid(column=0, row=1)
user_label = Label(text="Email/Username:", fg="black", bg="white")
user_label.grid(column=0, row=2)
password_label = Label(text="password:", fg="black", bg="white")
password_label.grid(column=0, row=3)

website = Entry(width=21, bg="white", highlightthickness=0, fg='black')
website.grid(column=1, row=1)
website.focus()

user = Entry(width=39, bg="white", highlightthickness=0, fg='black')
user.grid(column=1, columnspan=2, row=2)
user.insert(0, "korededavid@gmail.com")

password_entry = Entry(width=21, bg="white", highlightthickness=0, fg='black')
password_entry.grid(column=1, row=3)

generate_btn = Button(text="Generate Password", highlightthickness=0, highlightbackground="white", command=generate)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, highlightthickness=0, highlightbackground="white", command=add)
add_btn.grid(column=1, columnspan=2, row=4)

search_btn = Button(text="search", width=13 ,highlightthickness=0, highlightbackground="white", command=search)
search_btn.grid(column=2, row=1)

window.mainloop()
