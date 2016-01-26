from Tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.creatWidgets()

    def creatWidgets(self):
        self.helloLabel = Label(self, text='hello lili')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='quit', command=self.quit)
        self.quitButton.pack()

app = Application()

app.master.title('hellome')

app.mainloop()
