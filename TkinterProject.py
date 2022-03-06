from tkinter import * #import all files from tkinter

root = Tk() #creates a window

#label widget creation
label = Label(root, text="Hello World!")
label1 = Label(root, text="Welcome")

#shoves the label onto the window
#label.pack()

#puts labels on a grid of the window
#label.grid(row=0, column=1)
#label1.grid(row=1, column=1)

#label widget creation and grid allocation 
#label = Label(root, text="Hello World!").grid(row=0, column=1)
#label1 = Label(root, text="Welcome").grid(row=1, column=1)

def myclick():
    mylabel = Label(root, text="Look I Clicked the button!")
    mylabel.pack()

#creates button with text
mybutton = Button(root, text="Click Me!", padx=50, pady=50, command=myclick, fg="black", bg="white") #state=DISABLED

#shoves button onto the window
mybutton.pack()

root.mainloop() #loops the window
