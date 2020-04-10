import tkinter
import feedparser
import webbrowser
import os
import tkinter as tk
from tkinter import ttk


class RSSticker(tk.Frame):
    entry_headline = "[insert headline here]"
    entry_url = "[insert url here]"

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.build_window()
        self.popup_window = ttk.Label(self.master)
        self.pack()

    def build_window(self):
        self.popup_window["test"] = self.entry_headline
        self.popup_window.pack(side="top")
        self.popup_window.bind("<Button-1>", lambda e, popup_window=self.entry_url:
        self.open_article(self.entry_url))
        self.pack()

    # def refresh(self):
    # will show the cycled headlines

    # def open_article(self, url):
    # popup_window = webbrowser.open_new(url)
    # self.popup_window.update()

    # def style(self):
    # will show styled window


if __name__ == "__main__":
    root = tk.Tk()
    root.title("RSSticker")
    app = RSSticker(master=root)
    app.mainloop()