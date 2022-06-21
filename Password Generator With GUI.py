from tkinter import *
import string
from random import randint, choice

def generate_password():
    password_min = 8
    password_max = 99
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range (randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    with open("Lastpass.txt", "w") as f:
        f.write(password)
def generate_password2():
    password_min = 8
    password_max = 99
    all_chars = string.ascii_letters
    password = "".join(choice(all_chars) for x in range (randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    with open("Lastpass.txt", "w") as f:
        f.write(password)
def generate_password3():
    password_min = 8
    password_max = 99
    all_chars = string.ascii_letters + string.digits
    password = "".join(choice(all_chars) for x in range (randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    with open("Lastpass.txt", "w") as f:
        f.write(password)


window = Tk()
window.title("Password Generator")
window.geometry("1920x1080")
window.minsize(1000, 600)
window.wm_attributes("-topmost", 1)
window.configure(bg = '#4065A4')

frame = Frame(window, bg='#4065A4')



salut = Label(frame, text="Your generated password will be showed here:", font=("Helvetica", 20), bg='#4065A4', fg='white')
salut.pack()

password_entry = Entry(frame, text="Mot de passe", font=("Helvetica", 20), bg='#4065A4', fg='white')
password_entry.pack()

Moche = Label(frame, text="Press the button below to generate a password with letters, punctuations and special characters", font=("Helvetica", 20), bg='#4065A4', fg='white')
Moche.pack()

button = Button(frame, text="Generate", font=("Helvetica", 20), bg='#4065A4', fg='red', command=generate_password)
button.pack(fill=X)

Moche = Label(frame, text="Press the button below to generate a password with only letters", font=("Helvetica", 20), bg='#4065A4', fg='white')
Moche.pack()

button = Button(frame, text="Generate", font=("Helvetica", 20), bg='#4065A4', fg='red', command=generate_password2)
button.pack(fill=X)

Moche = Label(frame, text="Press the button below to generate a password with letters and numbers", font=("Helvetica", 20), bg='#4065A4', fg='white')
Moche.pack()

button = Button(frame, text="Generate", font=("Helvetica", 20), bg='#4065A4', fg='red', command=generate_password3)
button.pack(fill=X)

Moche = Label(frame, text="", font=("Helvetica", 20), bg='#4065A4', fg='white')
Moche.pack()

Moche = Label(frame, text="Password generator made by Luca.", font=("Helvetica", 20), bg='#4065A4', fg='white')
Moche.pack()

frame.pack(expand=YES)


window.mainloop()
