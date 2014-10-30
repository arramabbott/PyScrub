from Tkinter import Tk, Frame, BOTH, Menu, Text
import Image
import tkFileDialog 
import tkMessageBox as box

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
        fileMenu.add_command(label="Open Image", command=self.OnOpenImg)
        fileMenu.add_command(label="Check Image", command=self.OngetImgData)        
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

    def OnOpenImg(self):
        fileTypes = [('JPEG / JFIF','*.jpg'), ('All files', '*.*')]
        dialog = tkFileDialog.Open(self, filetypes = fileTypes)
        fl = dialog.show()
        if fl != '':
            imgFile = self.cleanImg(fl)

    def cleanImg(self,fileName):
		image = Image.open(fileName)
		data = list(image.getdata())
		cleanImg = Image.new(image.mode, image.size)
		cleanImg.putdata(data)
		cleanImg.save(fileName)
		box.showinfo("Information", "Image " + str(fileName) + " cleaned")
	
    def OngetImgData(self):
		fileTypes = [('Image Files', '*.jpg'), ('All files', '*.*')]
		dialog = tkFileDialog.Open(self, filetypes = fileTypes)
		fl = dialog.show()
		if fl != '':
			imgFile = self.getImgData(fl)
  
    def getImgData(self, fileName):
		img = Image.open(fileName)
		exif_data = img._getexif()
		for key,value in exif_data.items():
			print value
		box.showinfo("Information" , exif_data)

    def onExit(self):
        self.quit()

def main():
	root = Tk()
	root.geometry("250x150+300+300")
	app = PyScrubImg(root)
	root.mainloop()

if __name__ == '__main__':
    main()