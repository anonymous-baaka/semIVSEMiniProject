import tkinter
class LoginScreen:
    Frame=None
    UsernameTextBox=None
    PasswordTextBox=None
    SubmitButton=None
    ButtonHeight=3
    ButtonWidth=10
    TextBoxHeight=3
    TextBoxWidth=50
    root=None
    invalidText=None
    emailID=""
    def __init__(self,root):
        self.root=root
        self.Frame=tkinter.Frame(root)
        self.Frame.pack()

        self.UsernameTextBox=tkinter.Text(self.Frame,width=self.TextBoxWidth,height=self.TextBoxHeight)
        self.UsernameTextBox.insert("insert",'atharvadhanvate@gmail.com')
        self.PasswordTextBox = tkinter.Text(self.Frame,width=self.TextBoxWidth,height=self.TextBoxHeight)
        self.PasswordTextBox.insert("insert", '1234')
        self.invalidText=tkinter.Text()

        self.UsernameTextBox.pack()
        self.PasswordTextBox.pack()

        self.SubmitButton=tkinter.Button(self.Frame,text='Submit',width=self.ButtonWidth,height=self.ButtonHeight,command=lambda:self.__credentailValidator())
        self.SubmitButton.pack()

    #check for credentials: next screen if corect else invalid. called when submit clicked
    def __credentailValidator(self):
        correctUsername='atharvadhanvate@gmail.com'
        correctPass='1234'

        inputUsername = self.UsernameTextBox.get("1.0", tkinter.END).strip()
        inputPass = self.PasswordTextBox.get("1.0", tkinter.END).strip()

        self.invalidText.pack_forget()

        print("ipUsr=",inputUsername)
        print("ipPass=",inputPass)
        if correctUsername==inputUsername and correctPass==inputPass:
            print("Success")
            self.__validCredentails()
        else:
            print("Fail")
            self.__invalidCredentials()

    def __invalidCredentials(self):
        self.invalidText=tkinter.Text(self.Frame,height=self.TextBoxHeight//2,width=self.TextBoxWidth)
        self.invalidText.insert('insert','Invalid username or password. Try again')
        self.invalidText.config(state=tkinter.DISABLED)
        self.invalidText.pack()

    def __validCredentails(self):
        self.emailID=self.UsernameTextBox.get("1.0", tkinter.END).strip()
        self.Frame.pack_forget()
        import movieSelection
        canvas=movieSelection.create(self.root,self.emailID)
        #self.root.destroy()

    #def CreateNewAcc(self):


rootHeight=400
rootWidth=800
root=tkinter.Tk()
root.geometry('{}x{}'.format(rootWidth,rootHeight))
root.config(bg='white')
screen=LoginScreen(root)
root.mainloop()