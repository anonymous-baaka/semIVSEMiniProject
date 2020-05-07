import tkinter

if __name__!='__main__':
    class ConfirmationScreen:
        rootCanvas=None
        successText=None
        successString=""
        mailText=None
        mailString=""
        finishButton=None
        title=""
        selectedSeatList=""
        def __init__(self,canvas,title,selectedSeatList):    #canvas
            self.title=title
            self.selectedSeatList=selectedSeatList

            self.successString="Tickets Booked Successfully"
            self.rootCanvas=canvas
            self.successText=tkinter.Text(self.rootCanvas,width=len(self.successString),height=2)
            self.successText.insert('insert',self.successString)
            self.successText.config(state=tkinter.DISABLED)
            self.successText.pack()

            self.mailString="Booking details have been sent to your email id"
            self.mailText=tkinter.Text(self.rootCanvas,width=len(self.mailString),height=2)
            self.mailText.insert('insert',self.mailString)
            self.mailText.config(state=tkinter.DISABLED)
            self.mailText.pack()

            self.finishButton=tkinter.Button(self.rootCanvas,width=8,height=3,command=lambda:self.finishclicked(),text="Finish")
            self.finishButton.pack()

        def finishclicked(self):
            self.rootCanvas.destroy()

    def create(root,title,selectedSeatList):
        print("confirmition screen")
        print('seats= ')
        print(type(selectedSeatList[0]))
        #for ele in selectedSeatList:
         #   print(ele['text'],end=" ")
        root.geometry('400x300')
        ConfirmationScreen(root,title,selectedSeatList)
        root.mainloop()
