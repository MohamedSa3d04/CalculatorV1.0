#Very updated Calculator
#Needed libraries
from tkinter import *
from tkinter import ttk
from time import sleep
import pymysql

root = Tk()
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.geometry('830x650+380+80')
        self.root.title('myCalculator')
        self.root.resizable(False,False)
        self.root.config(background='#A6ACAF')
        Head = Label(self.root,
        text='[Calculator V1.0]',
        bg='#34495E',
        font=('monospace',14),
        fg='white'
        )
        Head.pack(fill=X)

        #Input&Output text label
        self.PreviousOP = 'PreviousOP'
        self.ANSlbl = Label(root, text=self.PreviousOP, bg='#A6ACAF', font=('monospace',15), fg='black')
        self.ANSlbl.place(x=19,y=25)
        self.equation = StringVar()
        self.maintxt = Entry(root, font=(70), textvariable=self.equation, bg='#E5E8E8', fg='#99A3A4', justify='left', width=72)
        self.maintxt.insert(3,'Type the function ex:2 * 3')
        self.maintxt.place(x=19,y= 50, height=50)
        self.maintxt.bind('<FocusIn>',self.Write_Func)
        
        #ButtonsNumberFrame
        nums_Frame = Frame(root, width=550, height=400, bg='#E5E8E8')
        nums_Frame.place(x=19,y=130)

        #ButtonsNumber
        sevenButton = Button(nums_Frame, text='7', font=(30), justify='center', width=9, bg='#34495E', fg='white', border=None,cursor='hand2', command=lambda:self.btnClick('7'))
        sevenButton.place(x=29,y=30)
        
        fourButton = Button(nums_Frame, text='4', font=(30), justify='center', width=9, bg='#34495E', fg='white', border=None,cursor='hand2', command=lambda:self.btnClick('4'))
        fourButton.place(x=29,y=150)
        
        oneButton = Button(nums_Frame, text='1', font=(30), justify='center', width=9, bg='#34495E', fg='white', border=None,cursor='hand2', command=lambda:self.btnClick('1'))
        oneButton.place(x=29,y=270)
        
        eightButton = Button(nums_Frame, text='8', font=(30), justify='center', width=9, bg='#34495E', fg='white', border=None,cursor='hand2', command=lambda:self.btnClick('8'))
        eightButton.place(x=220,y=30)
        
        fiveButton = Button(nums_Frame, text='5', font=(30), justify='center', width=9, bg='#34495E', fg='white', border=None,cursor='hand2', command=lambda:self.btnClick('5'))
        fiveButton.place(x=220,y=150)
        
        twoButton = Button(nums_Frame, text='2', font=(30), justify='center', width=9, bg='#34495E', fg='white', border=None,cursor='hand2', command=lambda:self.btnClick('2'))
        twoButton.place(x=220,y=270)
        
        nineButton = Button(nums_Frame, text='9', font=(30), justify='center', width=9, bg='#34495E', fg='white', border=None,cursor='hand2', command=lambda:self.btnClick('9'))
        nineButton.place(x=411,y=30)
        
        sexButton = Button(nums_Frame, text='6', font=(30), justify='center', width=9, bg='#34495E', fg='white', border=None,cursor='hand2', command=lambda:self.btnClick('6'))
        sexButton.place(x=411,y=150)
        
        threeButton = Button(nums_Frame, text='3', font=(30), justify='center', width=9, bg='#34495E', fg='white', border=None,cursor='hand2', command=lambda:self.btnClick('3'))
        threeButton.place(x=411,y=270)
        
        zeroButton = Button(nums_Frame, text='0', font=(30), justify='center', width=9, bg='#D35400', fg='white', border=1,cursor='hand2', command=lambda:self.btnClick('0'))
        zeroButton.place(x=29,y=350)
        
        dotButton = Button(nums_Frame, text='.', font=(30), justify='center', width=9, bg='#D35400', fg='white', border=None,cursor='hand2', command=lambda:self.btnClick('.'))
        dotButton.place(x=220,y=350)

        CEButton = Button(nums_Frame, text='CE', font=(30), justify='center', width=9, bg='#D35400', fg='white', border=None,cursor='hand2', command=lambda:self.btnClick('DEL'))
        CEButton.place(x=411,y=350)
        

        #ButtonsOperationsFrame
        OPs_frame = Frame(root, width=215, height=400, bg='#FEF5E7')
        OPs_frame.place(x=590,y=130)

        sumButton = Button(OPs_frame, text='+', font=(30), justify='center', width=6, bg='#34495E', fg='white', border=1,cursor='hand2' , command=lambda:self.btnClick('+'))
        sumButton.place(x=23,y=30)

        mulButton = Button(OPs_frame, text='*', font=(30), justify='center', width=6, bg='#34495E', fg='white', border=1,cursor='hand2', command=lambda:self.btnClick('*') )
        mulButton.place(x=23,y=150)

        expButton = Button(OPs_frame, text='^', font=(30), justify='center', width=6, bg='#34495E', fg='white', border=1,cursor='hand2', command=lambda:self.btnClick('**') )
        expButton.place(x=23,y=270)

        subButton = Button(OPs_frame, text='-', font=(30), justify='center', width=6, bg='#34495E', fg='white', border=1,cursor='hand2', command=lambda:self.btnClick('-') )
        subButton.place(x=120,y=30)

        divButton = Button(OPs_frame, text='/', font=(30), justify='center', width=6, bg='#34495E', fg='white', border=1,cursor='hand2', command=lambda:self.btnClick('/') )
        divButton.place(x=120,y=150)

        modButton = Button(OPs_frame, text='%', font=(30), justify='center', width=6, bg='#34495E', fg='white', border=1,cursor='hand2', command=lambda:self.btnClick('%') )
        modButton.place(x=120,y=270)

        self.equalButton = Button(OPs_frame, text='=', font=(30), justify='center', width=6, bg='red', fg='white', border=1,cursor='hand2',command=self.Equal)
        self.equalButton.place(x=23,y=350)

        ANSButton = Button(OPs_frame, text='ANS', font=(30), justify='center', width=6, bg='#D35400', fg='white', border=1,cursor='hand2', command=lambda:self.btnClick('ANS'))
        ANSButton.place(x=120,y=350)

   
        
    #Proccess Functions
    def Write_Func (self, ev):
        if (self.equation.get() !=None and self.equation.get()[0] == 'T'):
            self.maintxt.delete(0,END)
            self.maintxt.insert(1,' ')
            self.maintxt.config(fg='black')


    #When click on buttons:
    def btnClick (self, btn):
        if (self.equation.get() !=None and self.equation.get()[0] == 'T'):
            self.Write_Func(None)

        if btn == "DEL":
            self.maintxt.delete(0,END)
            self.maintxt.insert(1,' ')
            self.maintxt.config(fg='black')
        elif btn != 'ANS':
            self.equation.set(f'{self.equation.get()}{btn}')
            self.maintxt.insert(END,"")
            self.equalButton.focus()
        else:
            self.equation.set(f'{self.equation.get()} {str(self.Answer)}')
            self.maintxt.insert(END," ")
            self.equalButton.focus()


    def Equal(self):
        self.ANSlbl.config(text = self.equation.get())
        self.Answer = eval(self.equation.get())
        self.maintxt.delete(0,END)
        self.maintxt.insert(1,str(self.Answer))
        










myCalc = Calculator(root)
root.mainloop()

