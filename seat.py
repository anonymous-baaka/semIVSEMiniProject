
if __name__!='__main__':
    import tkinter
    ButtonList=[]
    remainingSeats=1
    selectedSeatList=[]
    rowNumber=0

    def toggle(toggle_btn):
        global remainingSeats
        global selectedSeatList
        global root
        if toggle_btn.config('relief')[-1] == 'sunken':
            toggle_btn.config(relief="raised")
            remainingSeats+=1
            insertRemainingText(root,remainingSeats)
            #remove button from selected list
            for button in selectedSeatList:
                if button==toggle_btn:
                    selectedSeatList.remove(button)
            print(selectedSeatList)
            print("deselected")
            insertAmountText(root)
        else:
            if remainingSeats>0:
                toggle_btn.config(relief="sunken")
                remainingSeats-=1
                insertRemainingText(root,remainingSeats)
                selectedSeatList.append(toggle_btn)
                print(selectedSeatList)
                print("selected")
                insertAmountText(root)

    def insertButton(frame):     #frame
        global ButtonList
        global rowNumber
        for i in range(7):
            ButtonRow=[]
            for j in range(10):
                ButtonRow.append(tkinter.Button(frame,width=8,height=4,text=str(chr(i+65))+str(j),command=lambda row=i,column=j:seatSelected(row,column),relief="raised"))
                ButtonRow[-1].grid(row=i+1,column=j,padx=2,pady=2)
            ButtonList.append(ButtonRow)
            rowNumber+=10
            #tkinter.Button(root).pack()
    def seatSelected(i,j):
        print(i,j)
        global remainingSeats
        toggle(ButtonList[i][j])

    def insertTextBox(root,text):
        textbox=tkinter.Text(root,width=15,height=2)
        textbox.insert('insert',text)
        textbox.config(state=tkinter.DISABLED)
        textbox.grid(row=0,column=0)

    def insertRemainingText(root,remainingSeats):
        global rowNumber
        textbox = tkinter.Text(root, width=15, height=2)
        textbox.insert('insert', str(remainingSeats))
        textbox.config(state=tkinter.DISABLED)
        textbox.grid(row=0, column=2)

    def submitClicked(frame,root,title,emailID):
        global remainingSeats
        global selectedSeatList
        seatListText=[]
        print("remainig seats= ",remainingSeats)
        if remainingSeats==0:
            ##
            print("Selected Seats= ")
            for seat in selectedSeatList:
                s=seat['text']
                seatListText.append(s)
            print("\nSuccess")
            import paymentWindow
            frame.destroy()
            root.destroy()
            paymentWindow.create(tkinter.Tk(),title,selectedSeatList,emailID,seatListText)
    def insertSubmitButton(frame,root,title,emailID):
        global rowNumber
        global remainingSeats
        global selectedSeatList

        submitButtton=tkinter.Button(frame,width=8,height=5,command=lambda:submitClicked(frame,root,title,emailID),text="Submit")
        submitButtton.grid(row=rowNumber,column=4)

    def setRemainingText():
        global remainingSeats
        global optionsMenu
        global selectedSeatList
        global root
        print("insdie")

        print(type(optionsMenu))
        maxNumberOfSeats=int(optionsMenu['text'])
        print("Mx= ",maxNumberOfSeats)
        print("selected= ",len(selectedSeatList))
        remainingSeats=maxNumberOfSeats-len(selectedSeatList)
        insertRemainingText(root,remainingSeats)
        #insertAmountText(root)

    def insertOptionsMenu(root):
        options=[int(x) for x in range(1,10)]
        variable=tkinter.StringVar(root)
        variable.set(options[0])
        menu=tkinter.OptionMenu(root,variable,*options,command=lambda a:setRemainingText())
        menu.grid(row=0,column=1)
        return menu

    def insertAmountText(root):
        global selectedSeatList
        global costPerTicket
        global tax

        stringText=tkinter.Text(root,height=1,width=len('Total Amount='))
        stringText.insert('insert','Total Amount=')
        stringText.config(state=tkinter.DISABLED)
        stringText.grid(row=2,column=0)

        text=str(len(selectedSeatList)*costPerTicket+tax*len(selectedSeatList)*costPerTicket)
        amountText=tkinter.Text(root,height=2,width=len(text))
        amountText.insert('insert',text)
        amountText.config(state=tkinter.DISABLED)
        amountText.grid(row=2,column=1)

    costPerTicket=200
    tax=0.18
    root = tkinter.Tk()
    optionsMenu=None
    def create(title,emailID):
        global root
        global remainingSeats
        insertTextBox(root,'select seats')
        global optionsMenu
        optionsMenu=insertOptionsMenu(root)
        print("here")
        insertRemainingText(root,remainingSeats)

        frame=tkinter.Frame(root)
        insertButton(frame)
        insertAmountText(root)
        insertSubmitButton(frame,root,title,emailID)

        frame.grid(row=1,column=0)


        root.mainloop()
