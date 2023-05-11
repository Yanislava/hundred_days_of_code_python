from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    website_entry.delete(0, END)
    password_entry.delete(0, END)

    data_entry = f'{website} | {email} | {password}\n'

    with open('data.txt', 'a') as f:
        f.write(data_entry)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)

tomato_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=tomato_img)
#timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
username_label = Label(text='Email/Username:')
username_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, 'user@domain.com')

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

# Button
password_button = Button(text='Generate Password', width=11)
password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
