'''

This is the source code for making GUI in Python assignment

'''

# Import libraries
from tkinter import *
import random

# Initialize Tkinter
w = Tk()
w.title('Color')
w.geometry('300x200')
w['bg'] = '#ffffff'

# Variable
label_text = StringVar()
color_entry = StringVar()


# Functions to apply color
def apply_color():
    color = color_entry.get()
    w['bg'] = '#{}'.format(color)

# Function to random color generator
def generate_color():
    # randomize the hex code
    r = lambda: random.randint(0,255)
    color_entry.set('%02X%02X%02X' % (r(),r(),r()))

    # Apply color
    apply_color()

# Label
label = Label(
    w,
    textvariable=label_text,
    anchor=CENTER
)
label_text.set('Enter color hex code')
label.pack()

# Entry Widget
entry = Entry(
    w,
    textvariable=color_entry,
    width=20
)

entry.insert(0, 'ffffff')
entry.pack()

# Apply color button
button = Button(
    w,
    text='Apply',
    width=15,
    command=apply_color
)
button.pack()

# Random color generator button
# Button
button = Button(
    w,
    text='Random',
    width=15,
    command=generate_color
)
button.pack()

w.columnconfigure(0, weight=1)
w.rowconfigure(0, weight=1)
# Run the program infinitely
w.mainloop()


