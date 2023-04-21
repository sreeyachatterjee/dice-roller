#importing the modules
from tkinter import *
import tkinter
from PIL import Image
from PIL import ImageTk
import random


#toplevel widget representing main window
root = tkinter.Tk()
root.geometry('1920x1080')
root.title('Dice Roller')


#adding label into the frame
l0 = tkinter.Label(root, text="")
l0.pack()



l1 = tkinter.Label(root, text="This is a dice simulator\n Try your luck!", fg = "black", bg = "white",font = "Helvetica 16 bold italic" )
l1.pack()


#images
dice = ['die1.jpg', 'die2.jpg','die3.jpg','die4.jpg', 'die5.jpg','die6.jpg']



#simulating the images as random from 1 to 6
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))


label1 = tkinter.Label(root, image = image1)
label1.image = image1
#packing a widget in the parent widget
label1.pack(side = LEFT, expand = True)
label2 = tkinter.Label(root, image = image2)
label2.image = image2
#packing a widget in the parent widget
label2.pack(side = RIGHT, expand = True)


def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    #keep a reference
    label1.image = image1
    
    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image = image2)
    #keep a reference
    label2.image = image2

button = tkinter.Button(root,text="Roll the dice now", fg= 'white', bg = 'black', command = rolling_dice)
button.pack(expand= True)


#calling the tkinter loop
root.mainloop()