# Title: GUI Module
# Author(s): Alexie McDonald

# Import all relevant libraries: Tkinter for the GUI, PIL for the image drawing, graphicsDraw and generate hash for generation, and webbrowser to open help documentation
from tkinter import *
from PIL import Image, ImageTk
import graphicsDraw
from GenerateHash import *
import webbrowser

# Declare an overarching application class that will switch between screens during runtime
class SampleApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # Define a container, where several frames will be stacked, then brought to the forefront when required
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # Iterate over every frame
        for F in (StartPage, GUI):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # Put all of the pages in the same location. The one on the top of the stacking order will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        # Select the start opage
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        # Show a frame given the page name
        frame = self.frames[page_name]
        # Raise the frame to the top of the stack
        frame.tkraise()

class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # set the controller of the frame to the top level application controller.
        self.controller = controller
        # Open all images used in the Frame
        self.image2 = Image.open("./Images/button.png")
        self.image = Image.open("./Images/logo.png")
        self.photo = ImageTk.PhotoImage(self.image)
        # Convert image data to a Tkinter photoimage type
        self.photo2 = ImageTk.PhotoImage(self.image2)
        # Declare the widgets (buttons, labels, etc)
        self.logo = Label(self, image=self.photo)
        self.button = Label(self, image=self.photo2)
        self.generate = Button(self, image=self.photo2, command=lambda: controller.show_frame("GUI"))
        # Bind a function call to the button click event. In this case, it's an anonymous function that transitions to the main screen
        self.button.bind("<Button 1>", lambda self: controller.show_frame("GUI"))
        # Call the function to initialize the window
        self.init_window()

    def init_window(self):
        # Specify where the widgets will be placed
        self.logo.place(x=0, y=0)
        self.button.place(x=200, y=260)
    
class GUI(Frame):

    def __init__(self, parent, controller):
        # Retrieve all hash encodings avaliable on the current machine
        items = retrieve_available_hash_encodings()
        Frame.__init__(self, parent)
        self.controller = controller
        # Declare the variable that will keep track of the selected template
        self.variable = StringVar()
        self.variable.set("Random") # Set the dropdown to a default value
        self.hashes = StringVar()
        self.hashes.set("") # Set the dropdown to a default value
        # Initialize the two dropdown menus with the following options
        self.w = OptionMenu(self, self.variable, "Random", "Person", "Ghost")
        self.p = OptionMenu(self, self.hashes, *items)
        # Set the font of the dropdown menu selections
        self.w.config(font=('Roboto Thin',(13)))
        self.p.config(font=('Roboto Thin',(13)))
        # Open all images used in the Frame
        self.image = Image.open("./Images/inhash.png")
        self.image2 = Image.open("./Images/bodycol.png")
        self.image3 = Image.open("./Images/hatcol.png")
        self.image4 = Image.open("./Images/clothcol.png")
        self.image5 = Image.open("./Images/weaponcol.png")
        self.image6 = Image.open("./Images/templatecol.png")
        self.image7 = Image.open("./Images/filename.png")
        self.image8 = Image.open("./Images/button.png")
        self.image9 = Image.open("./Images/button2.png")
        self.image10 = Image.open("./Images/hashencodings.png")
        # Convert image data to a Tkinter photoimage type
        self.photo = ImageTk.PhotoImage(self.image)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.photo3 = ImageTk.PhotoImage(self.image3)
        self.photo4 = ImageTk.PhotoImage(self.image4)
        self.photo5 = ImageTk.PhotoImage(self.image5)
        self.photo6 = ImageTk.PhotoImage(self.image6)
        self.photo7 = ImageTk.PhotoImage(self.image7)
        self.photo8 = ImageTk.PhotoImage(self.image8)
        self.photo9 = ImageTk.PhotoImage(self.image9)
        self.photo10 = ImageTk.PhotoImage(self.image10)
        # Declare the widgets (buttons, labels, etc)
        self.button = Label(self, image=self.photo8)
        self.button2 = Label(self, image=self.photo9)
        # Bind a function call to the button click event. In this case, they are anonymous functions to generate the avatar and get help
        self.button.bind("<Button 1>", self.generate)
        self.button2.bind("<Button 1>", self.get_help)
        self.label = Label(self, image=self.photo)
        self.input_box = Entry(self)
        self.label2 = Label(self, image=self.photo2)
        self.input_box_2 = Entry(self)
        self.label3 = Label(self, image=self.photo3)
        self.input_box_3 = Entry(self)
        self.label4 = Label(self, image=self.photo6)
        self.input_box_4 = Entry(self)
        self.label5 = Label(self, image=self.photo7)
        self.input_box_5 = Entry(self)
        self.label6 = Label(self, image=self.photo10)
        self.gethelp = Button(self,text="Help", command=self.get_help)
        self.v = StringVar()
        self.v.set("")
        self.logo = Label(self, image=self.photo)
        self.help = Label(self, textvariable=self.v)
        self.generate = Button(self, text="Generate", command=self.generate)
        self.graphics = graphicsDraw.generateImage();
        # Call the function to initialize the window
        self.init_window()

    def init_window(self):

        # Specify where the widgets will be placed
        self.label.place(x=80, y=0)
        self.input_box.place(x=80, y=40)
        self.label5.place(x=80, y=60)
        self.input_box_5.place(x=80, y=100)
        self.label2.place(x=250, y=0)
        self.input_box_2.place(x=250, y=40)
        self.label3.place(x=250, y=60)
        self.input_box_3.place(x=250, y=100)
        self.label4.place(x=80, y=140)
        self.w.place(x=80, y=190)
        self.label6.place(x=250, y=140)
        self.button.place(x=190, y=270)
        self.button2.place(x=190, y=320)
        self.help.place(x=50, y=400)
        self.p.place(x=250, y=190)

    def generate(self, event):
        string = self.input_box.get()
        # Ensure that incorrect/incomplete values are caught and dealt with
        if (self.input_box_5.get() == ""):
            # Ensure that a file name is entered
            self.v.set("No File Name/Location entered. Please enter the name in the \"Output File\" Box")
        # Ensure that the colours given are in the proper hexadecimal format
        elif (len(self.input_box_2.get()) > 0 and (self.input_box_2.get()[0] != "#" or len(self.input_box_2.get()) != 7)):
            self.v.set("Body hex color is not of proper hex format. Please re-enter the value.")
        elif (len(self.input_box_3.get()) > 0 and (self.input_box_3.get()[0] != "#" or len(self.input_box_3.get()) != 7)):
            self.v.set("Hat hex color is not of proper hex format. Please re-enter the value.")
        else:
            # Call the generate image function with user parameters
            self.graphics.generate_and_return_image(self.input_box_5.get(), string, self.input_box_2.get(), self.input_box_3.get(), self.variable.get(), self.hashes.get())
        
    def get_help(self, event):
        # Open help documentation in a new browser window
        webbrowser.open('file://' + 'C:\\Users\\Alexie McDonald\\Documents\\3XA3_Group_9\\src\\Help Documentation\\helppage.html') 

if __name__.endswith('__main__'):
    # Run the main application
    app = SampleApp()
    # Set window dimensions
    app.geometry("500x430")
    # Set window title
    app.title("Ratava")
    # Set favicon to logo
    app.iconbitmap('./Images/icon.ico')
    # Execute application
    app.mainloop()
