from cgitb import text
from curses import window
import tkinter as tk
#from PIL import Image, ImageTk

# define custom function
def calculateArea():
    try:
        sideA = float(txtSideA.get()) #get sideA from its textbox
        sideB = float(txtSideB.get()) #get sideB from its textbox
        area = 0.5 * sideA * sideB #implemet an equation given varibles
        lblAnswer.config(text=area) #output the solution to the answer to the answe label

    except ValueError:
        lblAnswer.config(text="ERRROR: Please enter numbers!")

# window properties
window = tk.Tk() #function that can build a window
window.title("Advanced Tkinter Tutorial")
window.geometry("600X400") #pixels, 1" = 100px
window.configure(bg='#336699')

# create lables

# create textboxes

# create buttons

# add GUI items to agrid