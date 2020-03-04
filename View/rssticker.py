from tkinter import *
from tkinter import ttk
import webbrowser

# https://www.csestack.org/code-python-to-open-url-in-browser/

def callback(url):
    webbrowser.open_new_tab(url)


def render(content):

    feedTitle = content['feed']['title']
    summary = content.get("entries")[0].get("summary")
    link = content.get("entries")[0].get("link")

    root = Tk()
    root.title(feedTitle)
    link = ttk.Label(root, text=summary, foreground="blue", cursor="hand2")
    link.pack()
    link.bind("<Button-1>", lambda e: callback(link))
    link.config(font=("Courier", 18, "bold"))

    # for e in content.entries:
    #     print(e.title_detail.value)
    #     print(e.title_detail.base)


    link.config(wraplength=500)
    link.config(justify=CENTER)
    root.mainloop()
