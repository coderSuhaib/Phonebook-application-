# Python Ver: 3.6.2
#
# Author: Suhaib Al-Tamimi
#
# Purpose: Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#          using tkinter parent and child relationships.
#
# Tested OS: This code was written and tested to work with mac OS 10.12.6.


from tkinter import *
import tkinter as tk

# Import my 2 other files that support this forms
import phonebook_gui
import phonebook_func


# The parent window for our class 
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)


        # define our master frame configuration
        self.master = master
        self.master.minsize(550,350)
        self.master.maxsize(550,350)
        # This CenterWindow method will center our app on the user's screen
        self.master.title('The Tkinter Phonebook Demo')
        self.master.configure(bg='#F0F0F0')

        
        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        phonebook_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()  # This is the syntax that we use to create a window with tkinter 
    App = ParentWindow(root) # we call the class the App and attached the root inorder to create the window and pass it to our class. 
    root.mainloop() #this takes the first window root and fire it over and over other wise it would
                    # display and then disapear right away. so we put it in a loop.
