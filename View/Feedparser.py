import feedparser
import tkinter as tk
from View import settings

feed = feedparser.parse('http://www.repubblica.it/rss/homepage/rss2.0.xml')
feedShow = {'entries': [{feed['entries'][0]['title']}]}


class RSSTicker(tk.Text):
    def __init__(self, parent, **kw):
        super().__init__(parent, height=1, wrap="none", state='disabled', **kw)
        self.headlineIndex = 0
        self.text = ''
        self.pos = 0
        self.after_idle(self.updateHeadline)
        self.after_idle(self.tick)

    def updateHeadline(self):
        try:
            self.text += feed['entries'][self.headlineIndex]['title']
        except IndexError:
            self.headlineIndex = 0
            self.text = feed['entries'][self.headlineIndex]['title']

        self.headlineIndex += 1
        self.after(1000, self.updateHeadline)

    def tick(self):
        if self.pos < len(self.text):
            self.config(state='normal')
            self.insert('end', self.text[self.pos])
            self.pos += 1
            self.see('end')
            self.config(state='disabled')
            self.after(100, self.tick)

if __name__ == '__main__':
    root = tk.Tk()
    ticker = RSSTicker(root, bg='black', fg='white', font=("arial", 20))
    ticker.pack(side='top', fill='x')
    load= SettingsModel.load_settings(self)
    button = tk.Button(root, text="settings", bg="black", fg="white", font="Arial 10")
    button.pack()
    root.mainloop()