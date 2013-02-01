# set position and size of a Tkinter window
# also set the position of any widgets using place(x, y) layout

from tkinter import *

# create the root window
root = Tk()
# optionally give it a title
root.title("My Title")

# set the root window's height, width and x,y position
# x and y are the coordinates of the upper left corner
w = 300
h = 200
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("640x480")

# use a colorful frame
#frame = tk.Frame(root, bg='green')
#frame.pack(fill='both', expand='yes')
backgroundImage = PhotoImage(file="slots.gif")
backgroundLabel = Label(root,  width=640, height=280, background="red")
backgroundLabel.configure(image = backgroundImage, width=640, height=480)
backgroundLabel.image= backgroundImage
backgroundLabel.pack()



# position a label on the frame using place(x, y)
# place(x=0, y=0) would be the upper left frame corner
label = Label(backgroundLabel, text="Hello Python Programmer!")
label.place(x=20, y=30)

# put the button below the label, change y coordinate
button = Button(backgroundLabel, text="Spin", bg='yellow', width=6, height=3)
button.place(x=508, y=403)

button2 = Button(backgroundLabel, text="Spin", bg='yellow', width=6, height=3)
button2.place(x=518, y=413)

root.mainloop()