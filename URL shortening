import tkinter
import pyshorteners

window = tkinter.Tk()
window.title("URL Shortener")
window.geometry("300x150")
window.configure()

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    shorturl_entry.insert(0,short_url)

longurl_label = tkinter.Label(window,text="Enter a long url pwease")
longurl_entry = tkinter.Entry(window)
shorturl_label = tkinter.Label(window, text="Output of Shortened URL")
shorturl_entry = tkinter.Entry(window)
shorten_button = tkinter.Button(window,text="Shorten URL",command=shorten)

longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shorten_button.pack()



window.mainloop()

"""
-long url label -> text enter long url
-long url entry
-short url label
-short url entry
-shorten_button

-pack it

-on click on the button add in a shorten command

-import shortener
-create a shortener object  | shortener = pyshorteners.Shortener()
-short_url = shortener.tinyurl.short(str URL)

-insert the shortened url into the second entry | entry.insert(loc -> int, str)
"""
