# https://pythonprogramming.altervista.org/a-simple-test-maker-with-python-and-tkinter/?doing_wp_cron=1587583767.8565831184387207031250

from tkinter import *
import tkinter as tk
# import feedparser

root = tk.Tk()
label = tk.Label(root, text="Coronavirus: UK deaths double in 24 hours", bg="gold", fg="blue", font="Arial 24")
label.pack()
text = tk.Text(root)
text.pack()
root.mainloop()

numdom = len(quest)
score = 0
num = 0
def d1():
	global num, score, entry
	if num == numdom:
		text.pack_forget()
		entry.pack_forget()
		button['text'] = f"Score {score}\n Click to Close this window"
		button['command'] = game_over
		button.pack()
		return
 
	if num == 0:
		answer_widget()
	root.geometry("200x200+100+200")
	text['height'] = 1
	text['bg'] = 'cyan'
	text['width'] = 50
	text.delete("1.0",tk.END)
	text.insert("1.0",quest[num][0])
	button.pack_forget()
	num+=1
 
def game_over():
	root.destroy()
 
def answer_widget():
	global entry
	entry = tk.Entry(root, textvariable=solution, bg="yellow", font="Arial 20")
	entry.pack()
	entry.bind("<Return>", lambda x: check())
	entry.focus()
 
def check():
	global n, score
	if solution.get() == quest[num-1][1]:
		text.insert(tk.END, "Right")
		score+=1
	else:
		text.insert(tk.END, "Wrong")
	solution.set("")
	d1()
 
root = tk.Tk()
label = tk.Label(root, text = """Test""", bg="coral", font="Arial 48")
label.pack()
rules = """Answer to the Following questions
 
Click on the button below to start
You will see a question
Write your answer and press Enter
"""
text = tk.Text(root, height=12,font="Arial 20")
text.insert("1.0", rules)
text.pack()
button = tk.Button(root, text="Click To Start", bg="black", fg="white", command=d1, font="Arial 20")
button.pack()
solution = tk.StringVar()
 
root.mainloop()

# def helloWorld(args):
#     if args.url is not None:
#         feed = feedparser(args.url[0])
#     elif args.file is not None:
#         feed = feedparser(args.file)
#     else:
#         feed = feedparser("http://feeds.feedburner.com/ign/all")

#     root = Tk()
#     var = StringVar()
#     label = Message(root, textvariable=var)  # relief=RAISED
#     var.set(feed)
#     window_text = var.get()
    
#     root.geometry("1000x500")

#     button = tk.Button(text="Click and Quit", command=root.quit)
#     button.pack()

#     label.pack()
#     root.mainloop()
#     return window_text

"""
while display is not quitting:
    while list is not finished:
        iterate through the list
    if the list does end:
        update the list
"""

