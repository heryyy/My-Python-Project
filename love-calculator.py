from tkinter import *
import random
root = Tk()
# Defining the size, width=400, height=240
root.geometry('400x240')
# Title 
root.title('Love Calculator❤️❤️')

def calculate_love():
    # value will contain digits between 0-9
    st = '0123456789'
    # result will be in double digits
    digit = 2
    temp = "".join(random.sample(st, digit))
    result.config(text=temp)


# Heading on Top
heading = Label(root, text='Love Calculator????')
heading.pack()

# Slot/input for the first name
slot1 = Label(root, text="Nama Kamu:")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()

# Slot/input for the partner name
slot2 = Label(root, text="Nama crush/pacar kamu:")
slot2.pack()
name2 = Entry(root, border=5)
name2.pack()

bt = Button(root, text="Hitung", height=1,
            width=7, command=calculate_love)
bt.pack()

# Text on result slot
result = Label(root, text='Persentase kecocokan:')
result.pack()

# Starting the GUI
root.mainloop()