from tkinter import *
import hashlib

#Creating a Window with help of Tk() function
window = Tk()
window.config(bg="#E8E8E8")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.geometry("%dx%d" % (width, height))

#Facebook Label and Tagline
facebook = Label(window, text="facebook",bg="#E8E8E8", font=("Klavika", 50, 'bold'), fg="#427bff")
facebook.place(x=150, y=210)

tagline1 = Label(window, text="Facebook helps you connect and share",bg="#E8E8E8", font="Leelawadee 20 ", fg="black")
tagline1.place(x=150, y=290)

tagline2 = Label(window, text="with the people in your life.", bg="#E8E8E8" , font="Leelawadee 20 ", fg="black")
tagline2.place(x=150, y=323)

#Creating a Canvas for widgets
canvas = Canvas(window, width=415, height=320, bg="#fffcfc")
canvas.place(x=750, y=175)

#Creating section for username and password
username = Entry(window, width=28, font=("Verdana", 15), bg="#E8E8E8", fg="#999999")
username.insert(10, 'Mobile number or email address')
username.place(x=775, y=207, height=50)

password = Entry(window, show="*", width=28, font=("Verdana", 15),  bg="#E8E8E8", fg="#999999")
password.insert(10, 'Password')
password.place(x=775, y=267, height=50)

# Define a function to display messages at the top right corner of the screen
def show_message(text, color):
    message = Label(window, text="", font=("Verdana", 15), fg=color, bg="#E8E8E8")
    message = Label(window, text=text, font=("Verdana", 15), fg=color, bg="#E8E8E8")
    message.place(x=window.winfo_width()-message.winfo_width()-320, y=20, height=30)

def login():
    # Get the entered username and password
    entered_username = username.get()
    entered_password = password.get()

    # Hash the entered password with SHA-256
    entered_password_hash = hashlib.sha256(entered_password.encode()).hexdigest()

    # Check if the user exists in the users file and the entered password matches the stored password
    with open('users.txt', 'r') as f:
        for line in f:
            username_hash, password_hash = line.strip().split(':')[1].split(',')
            if hashlib.sha256(entered_username.encode()).hexdigest() == username_hash and entered_password_hash == password_hash:
                # Display a success message and show a button for signout
                show_message("You have been signed in!", "#008ad3")
                # signout = Button(window, text="Sign Out", bg="#008ad3", font=("Klavika", 20, 'bold'), fg="white", height=0, border=0)
                # signout.place(x=775, y=380, height=50)
                return

    # If the user doesn't exist or the password doesn't match, display an error message
    show_message("Invalid username or password", "red")

def create_new_account():
    # Get the entered username and password
    entered_username = username.get()
    entered_password = password.get()

    # Hash the entered password with SHA-256
    entered_password_hash = hashlib.sha256(entered_password.encode()).hexdigest()

    # Check if the user already exists in the users file
    with open('users.txt', 'r') as f:
        for line in f:
            username_hash, _ = line.strip().split(':')[1].split(',')
            if hashlib.sha256(entered_username.encode()).hexdigest() == username_hash:
                # If the user already exists, display an error message
                show_message("Username already exists", "red")
                # message = Label(window, text="Username already exists", font=("Verdana", 20), fg="red", bg="#E8E8E8")
                # message.place(x=775, y=340, height=30)
                return

    # If the user doesn't exist, add the new user to the users file
    with open('users.txt', 'a') as f:
        f.write(entered_username + ',' + entered_password + ':' + hashlib.sha256(entered_username.encode()).hexdigest() + ',' + entered_password_hash + '\n')

    # Display a success message and show a button for signout

    show_message("Account created successfully!", "#008ad3")
    # message = Label(window, text="Account created successfully!", font=("Verdana", 20), fg="#008ad3", bg="#E8E8E8")
    # message.place(x=775, y=340, height=30)
    # signout = Button(window, text="Sign Out", bg="#008ad3", font=("Klavika", 20, 'bold'), fg="white", height=0, border=0)
    # signout.place(x=775, y=380, height=50)

#Creating Login Button
login = Button(window, text="                  Login                ", bg="#008ad3", font=("Klavika", 20, 'bold'), fg="white", height=0, border=0, command=login)
login.place(x=775, y=327, height=50)

forget = Button(window, text="Forgotten Password?", bg="white", font=("Klavika", 10), fg="#008ad3", height=1, border=0)
forget.place(x=900, y=377, height=20)

#Button for New Accoun
newAcc = Button(window, text="Create New Account", bg="#93c572", font=("Klavika", 20, 'bold'), fg="white", height=1, border=0, command=create_new_account)
newAcc.place(x=820, y=420, height=50)

#Button for Creating a Page
page = Button(window, text="Create a Page", bg="#E8E8E8" ,font=("Klavika", 10, "bold"), fg="black", height=1, border=0)
page.place(x=810, y=500, height=20)

label = Label(window, text="for a celebrity, band or business", bg="#E8E8E8" ,font=("Klavika", 10), fg="black")
label.place(x=910, y=500)


mainloop()
