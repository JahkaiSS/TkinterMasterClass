# tkinter app that asks for the username and password, and outputs 
# a message if correct or incorrect

# username label / entry
# password label / entry
# submit button

import tkinter
from tkinter import messagebox


window = tkinter.Tk()
window.title("Login Form")
window.geometry("300x300")
window.configure(bg="black")

frame = tkinter.Frame(bg="black")

def login():
    username = "1"
    password = "1"
    usernameCorrect = username_entry.get() == username
    passwordCorrect = password_entry.get() == password
    if usernameCorrect and passwordCorrect:
        messagebox.showinfo(title="Nice bro",message="You have loggged in successfully")
        window.quit()
        import pygame
        pygame.init()
        pygame.display.init()
        screen = pygame.display.set_mode([1920,1080])
        clock = pygame.time.Clock()
        FPS = 60
        r = 20
        g = 20
        
        while True:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                    exit()
                if event.type == pygame.KEYUP and keys[pygame.K_ESCAPE]:
                    quit()
                    exit()
            screen.fill([r,20,20],[0,0,screen.get_width()/2,screen.get_height()])
            if r > 100:
                r = 0
            r += 1
            screen.fill([90,g,13],[screen.get_width()/2,0,screen.get_width()/2 ,screen.get_height()])
            if g > 90:
                g = 20
            g += 1
            pygame.display.update()
            clock.tick(FPS)
    else:
        messagebox.showerror(title="Nah yo",message="Invalid Login")

login_label = tkinter.Label(frame,text="LOGIN", fg="lightgreen",bg="black",font=("Arial",30))
username_label    = tkinter.Label(frame,text="username",bg="black", fg="white",font=("Arial",16))
username_entry  = tkinter.Entry(frame)
password_label   = tkinter.Label(frame,text="password",bg="black", fg="white",font=("Arial",16))
password_entry   = tkinter.Entry(frame,show="*")
login_button    = tkinter.Button(frame,text="Login",bg="lightgreen",command=login)

login_label.grid(row=0,column=0,columnspan=2)
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1,pady=20)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1)
login_button.grid(row=3,column=0,columnspan=2)

frame.pack()

window.mainloop()
