import tkinter 
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login Form")
window.geometry("340x440")
window.configure(bg="#333333")

def login():
    username = "johnsmith"
    password = "12345"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success",message="Great! Welcome Back")
    else:
        messagebox.showerror(title="Invalid Login",message="Invalid Login Credentials")


frame = tkinter.Frame(bg="#333333")

login_label = tkinter.Label(frame, text="Login",bg="#333333",fg="#07BF38", font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username",bg="#333333", fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame,font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*",font=("Arial", 16))
password_label = tkinter.Label(frame, text="Password",fg="#FFFFFF",bg="#333333", font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login",bg="#07BF38",fg="#FFFFFF",font=("Arial", 16),command=login)



login_label.grid(row=0,column=0, columnspan=2, sticky="news",pady=40)
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1,pady=20)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1,pady=20)
login_button.grid(row=3,column=0,columnspan=2, pady=30)

frame.pack()

window.mainloop()

# tkinter structure:
# create window (foo)
# foo.title(string) , foo.geometry(string), foo.configure(bg=string)
# bottom of file -> foo.mainloop()

# extra stuff to add
# add a label | label = tkinter.Label(parent, text=string), label.pack() | or label.grid(row=int, column=int)

# Add 2 labels, login_label, username_label

# add 2 entries, username, password | tkinter.Entry(parent, show=str)

# add one label for the password

# add a login button | tkinter.Button(parent, text=str)

# grid everything
# login label(row=0, column=0, columnspan=2)
# row 1 -> username_label
# row 1, col 1 -> username_entry
# row 2, col 0 -> password_label
# row 2, col 1 -> password entry
# row 3, col 0, column span 2 -> login button

# change the foreground of the login label | tkinter.Label(stuff, fg=str)

# change bg of 3 labels to match window background

# change foreground of other 2 labels username and password 

# change the button color | bg=#FF3399 | fg=white

# make the login label sticky | foo.grid(stuff, sticky=str) > if str = "news" then take up space north east west south

# change font size for login_label | tkinter.Label(stuff, font("fontName" -> str, fontSize -> int))

# username and password get 16 size font

# username and password entries also get 16 size font

# button gets 16 size font

# Add spacing to the login label | foo.grid(stuff, pady=int)

# give the button y padding of 30

# y pad of 20 for the two entries

# login label color to button background color

# add a frame | frame = tkinter.Frame()

# make the frame the parent where the window was the parent

# pack the frame

# change the background color of the frame

#add a command to the button | tkinter.Button(stuff, command=functionName -> no "()")

# in the login function create a sample username and password

# get the username entry text using foo.get() to check for equality

# add a message box
# from tkinter import messagebox
# add a messagebox if successful login | messagebox.showinfo(title=str,message=str)

# add an error message for wrong credentials
