import tkinter
import movieList
from PIL import ImageTk,Image

class insertPanel:
    #button:movie poster        title           cast
    PosterButton=None
    rootCanvas=None
    Movie=None
    row=0
    TitleText=None
    titleNcastFrame=None
    castText=None
    castButton=None
    titleButton=None
    posterHeight=10
    root=None
    emailID=""
    def __init__(self,root,Movie,canvas,row,emailID):
        self.emailID=emailID
        self.root=root
        self.rootCanvas=canvas
        self.Movie=Movie
        self.row=row
        self.rootCanvas.pack()

        self.setPoster()
        self.setTitleNCastFrame()
        self.setTitleButton()
        self.setTitle()
        self.setCastButton()
        self.setCast()

    def setPoster(self):
        self.PosterButton=tkinter.Button(self.rootCanvas,text=self.Movie.title,command=lambda:self.nextWindow())
        self.PosterButton.grid(row=self.row,column=0)

    def setTitleNCastFrame(self):
        self.titleNcastFrame=tkinter.Frame(self.rootCanvas)
        self.titleNcastFrame.grid(row=self.row,column=1)

    def setTitleButton(self):
        self.titleButton = tkinter.Button(self.titleNcastFrame, text='Title', width=5, height=2)
        self.titleButton.grid(row=0, column=1)

    def setTitle(self):
        self.TitleText=tkinter.Text(self.titleNcastFrame,width=len(self.Movie.title),height=2)
        self.TitleText.insert('insert',self.Movie.title)
        self.TitleText.config(state=tkinter.DISABLED)
        self.TitleText.grid(row=1,column=1)

    def setCastButton(self):
        self.castButton=tkinter.Button(self.titleNcastFrame,text='Cast',width=4,height=2)
        self.castButton.grid(row=2,column=1)

    def setCast(self):
        self.castText=tkinter.Text(self.titleNcastFrame,width=len(self.Movie.cast)//3,height=4)
        self.castText.insert('insert',self.Movie.cast)
        self.castText.config(state=tkinter.DISABLED)
        self.castText.grid(row=3,column=1)


    def nextWindow(self):
        import seat
        global Framelist
        self.root.destroy()
        print("Movie= ",self.Movie.title)
        #for ele in Framelist:
         #   ele.rootCanvas.pack_forget()
        seat.create(self.Movie.title,self.emailID)
Framelist = []

def create(root,emailID):
    row=0
    #root.geometry('800x600')
    canvas=tkinter.Canvas(root)
    canvas.pack()
    MovieList = movieList.getMovieList()
    global Framelist
    for movie in MovieList:
        Framelist.append(insertPanel(root,movie,canvas,row,emailID))
        row+=1
    root.mainloop()
    return canvas

if __name__=='__main__':
    pass