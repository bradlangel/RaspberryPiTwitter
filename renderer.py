from Tkinter import *

class Renderer():    
    def __init__(self, backgroundColor = '#373737'):
        self.backgroundColor = backgroundColor
        
        self.Setup()
        self.Canvas()

    def Setup(self):
        self.root = Tk()
        
        self.screenWidth = self.root.winfo_screenwidth() *.5
        self.screenHeight = self.root.winfo_screenheight()
        
        self.root.overrideredirect(1)
        self.root.geometry('%dx%d+%d+%d' % (self.screenWidth, self.screenHeight, self.screenWidth, 0))
        self.root.configure(background = self.backgroundColor)
        
    def Canvas(self):
        self.canvas = Canvas(
            background = self.backgroundColor,
            borderwidth = -5,
            height = 500,
            relief= 'flat',
            width = 500)

        self.canvas.pack(expand = 1, fill = BOTH)

    def Draw(self):
        self.root.mainloop()
