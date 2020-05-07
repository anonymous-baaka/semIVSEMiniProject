import tkinter

if __name__!='__main__':
    class Payment:
        frame=None
        cardNumberText=[]
        cardNumberFrame=None
        CVVText=None
        parentWindow=None

        cardNumberString=''
        CVVString=''

        enterCardInfoText=None
        dashTextBox=[]

        enterCardNumberText=None
        baitText=None
        enterCVVText=None

        submitButton=None

        title=""
        selectedSeatList=[]

        emailID=""
        def __init__(self,root,title,selectedSeatList,emailID):
            self.title=title
            self.selectedSeatList=selectedSeatList
            self.emailID=emailID

            self.parentWindow=root
            self.frame=tkinter.Frame(self.parentWindow)
            self.frame.pack()
            self.cardNumberFrame=tkinter.Frame(self.frame,width=800,height=600)

            self.enterCardInfoText=tkinter.Text(self.frame,width=20,height=2)
            self.enterCardInfoText.insert('insert','Enter Card Details')
            self.enterCardInfoText.config(state=tkinter.DISABLED)



            # enter card info
            self.enterCardInfoText.pack()

            self.baitText = tkinter.Text(self.frame,width=60,height=0.1)
            self.baitText.insert('insert','-----------------------------------------------------------')
            self.baitText.config(state=tkinter.DISABLED)
            self.baitText.pack()

            #card number
            self.enterCardNumberText=tkinter.Text(self.frame,width=20,height=2)
            self.enterCardNumberText.insert('insert','Enter Card Number')
            self.enterCardNumberText.config(state=tkinter.DISABLED)
            self.enterCardNumberText.pack()

            #card number boxes
            self.cardNumberFrame.pack()
            for i in range(4):
                self.cardNumberText.append(tkinter.Text(self.cardNumberFrame, width=20, height=2))
                self.dashTextBox.append(tkinter.Text(self.cardNumberFrame,width=2,height=0.5))
                self.dashTextBox[-1].insert('insert','-')
                self.dashTextBox[-1].config(state=tkinter.DISABLED)

            for i in range(4):
                self.cardNumberText[i].pack(side=tkinter.LEFT)
                if i!=3:
                    self.dashTextBox[i].pack(side=tkinter.LEFT)


            #enter CVV text
            self.enterCVVText=tkinter.Text(self.frame,width=10,height=1)
            self.enterCVVText.insert('insert','Enter CVV')
            self.enterCVVText.pack()

            #CVV text
            self.CVVText=tkinter.Text(self.frame,width=5,height=2)
            self.CVVText.pack()

            self.submitButton=tkinter.Button(self.frame,width=6,height=3,text='Submit')
            self.submitButton.config(command=lambda:self.retreiveText())
            self.submitButton.pack()
           # self.cardNumberText.insert('insert','Enter Card Number')

        def retreiveText(self):     #get text from textboxes when submit clicked
            for i in range(4):
                self.cardNumberString+=self.cardNumberText[i].get("1.0", tkinter.END).strip()

            self.CVVString=self.CVVText.get("1.0", tkinter.END).strip()

            if self.__validate(self.cardNumberString,self.CVVString)==True:
                print(self.cardNumberString)
                global seatListText
                print("Success")
                import sendMail
                sendMail.sendMsg(self.title,self.selectedSeatList,self.emailID,seatListText)
                import confirmationScreen
                self.frame.destroy()
                confirmationScreen.create(self.parentWindow,self.title,self.selectedSeatList)

            else:
                print("invalid credentials. Please check card Number and CVV")

        def __validate(self,cardnumber,cvv):
            if len(cardnumber)==16 and len(cvv)==3:
                return True
            else:
                self.cardNumberString=self.CVVString=''
                return False
    seatListText=""
    def create(root,title,selectedSeatList,emailID,seatText):
        global seatListText
        seatListText=seatText

        #frame=tkinter.Frame(root)
        #frame.grid(row=0,column=0)
        Payment(root,title,selectedSeatList,emailID)
        root.mainloop()

