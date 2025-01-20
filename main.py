from tkinter import *
import random

# Create window
root = Tk()

# Dimensions of the tkinter window (dimensions are set in pixels)
root.geometry("800x600")

# Sets the background color for our window
root.configure(bg="green")

# Title of game window
root.title("Dice Board")

# Prevents maximizing of window avoiding any labels overlapping
root.resizable(0, 0)

# List of dice faces and corresponding numbers
dice_face = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

# Creating function to roll the dices
def roll():
    # Generate random indices for the dice faces
    dice1_index = random.randint(0, 5)
    dice2_index = random.randint(0, 5)
    
    # Update dice faces
    dice_label.configure(text=f'{dice_face[dice1_index]} {dice_face[dice2_index]}')
    
    # Update corresponding numbers
    number_label_1.configure(text=f'Dice 1: {dice1_index + 1}')
    number_label_2.configure(text=f'Dice 2: {dice2_index + 1}')
    number_label_3.configure(text=f'Dice Total: {dice1_index + dice2_index + 2}')

# Button to roll the dice
button = Button(
    root,
    text="Roll!",
    width=10,
    height=2,
    font=15,
    bg="goldenrod",
    bd=2,
    command=roll
)

# Button position
button.pack(padx=10, pady=15)

# Adding dice face label
dice_label = Label(root, font=("times", 250), bg="green", fg="white")
dice_label.pack()

# Adding labels for dice numbers
number_label_1 = Label(root, font=("times", 20), bg="green", fg="white")
number_label_1.pack()

number_label_2 = Label(root, font=("times", 20), bg="green", fg="white")
number_label_2.pack()

number_label_3 = Label(root, font=("times", 20), bg="green", fg="white")
number_label_3.pack()

# Start the Tkinter event loop
root.mainloop()
