import tkinter as tk
import feedparser

feed = feedparser.parse("http://feeds.bbci.co.uk/news/world/rss.xml?")
root = tk.Tk()
deli = 100           # milliseconds of delay per character
svar = tk.StringVar()
labl = tk.Label(root, textvariable=svar, height=2, bd=0, fg="red", width=60, font=("Calbri", 40), background="Black",  )
entry = str()

def shif():
    shif.msg = shif.msg[1:] + shif.msg[0]
    svar.set(shif.msg)
    root.after(deli, shif)

def feedentry(entry):
    for post in feed.entries:
        entry += post.title + "     "

feedentry(entry)
print (entry)
shif.msg = entry
shif()
labl.pack()
root.mainloop()
