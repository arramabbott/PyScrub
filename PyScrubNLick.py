from Tkinter import Tk, Frame, BOTH, Menu, Text
import Image
import tkFileDialog 
import tkMessageBox as box
from PIL import Image
from PIL.ExifTags import TAGS
 
class PyScrubImg(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="gray")   
        self.parent = parent
        self.mainWindow()
    
    def mainWindow(self):
        self.parent.title("PyScrubImg")
        self.pack(fill=BOTH, expand=1)
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Clean Image", command=self.OnCleanImg)
        fileMenu.add_command(label="Check Image Tags", command=self.OngetImgExifData)        
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

    def openFile(self):
        fileTypes = [('JPEG / JFIF','*.jpg'), ('All files', '*.*')]
        dialog = tkFileDialog.Open(self, filetypes = fileTypes)
        inputFile = dialog.show()
        return inputFile

    def OnCleanImg(self):
    	self.openFile()
        if inputFile != '':
            imgFile = self.cleanImg(inputFile)

    def cleanImg(self,fileName):
        image = Image.open(fileName)
        data = list(image.getdata())
        cleanImg = Image.new(image.mode, image.size)
        cleanImg.putdata(data)
        cleanImg.save(fileName)
        box.showinfo("Information", "Image " + str(fileName) + " cleaned")

    def OngetImgExifData(self):
        fileTypes = [('JPEG / JFIF','*.jpg'), ('All files', '*.*')]
        dialog = tkFileDialog.Open(self, filetypes = fileTypes)
        inputFile = dialog.show()
        if inputFile != '':
            data = {}
            img = Image.open(inputFile)
            info = img._getexif()
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                data[decoded] = value
                print str(tag)  + ' : ' + str(value)
            box.showinfo("Information" , data)

    def onExit(self):
        self.quit()

def main():
	root = Tk()
	root.geometry("250x150+300+300")
	app = PyScrubImg(root)
	text = Text(root, state='disabled', width=80, height=24, wrap='none')
	text.grid()
	root.mainloop()

if __name__ == '__main__':
    main()