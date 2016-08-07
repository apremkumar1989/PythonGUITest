import Tkinter

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.num1Var = Tkinter.StringVar()
        self.num1Var.set(0)
        self.num1 = Tkinter.Entry(self,textvariable=self.num1Var)
        self.num1.grid(column=0,row=0,sticky='EW')

        self.num2Var = Tkinter.StringVar()
        self.num2Var.set(0)
        self.num2 = Tkinter.Entry(self,textvariable=self.num2Var)
        self.num2.grid(column=0,row=1,sticky='EW')

        button = Tkinter.Button(self,text=u"Add numbers",command=self.OnButtonClick)
        button.grid(column=1,row=0)

        self.resultVar = Tkinter.StringVar()
        self.resultVar.set(0)
        self.addResult = Tkinter.Entry(self,textvariable=self.resultVar)
        self.addResult.grid(column=0,row=2,sticky='EW')

    def OnButtonClick(self):
        print "You clicked the button !"
        print self.num1Var.get()
        self.resultVar.set(int(self.num1Var.get()) + int(self.num2Var.get()))

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my addition app')
    app.mainloop()