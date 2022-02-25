from PyQt5 import QtWidgets
from PyQt5 import QtCore
from pdf2image import convert_from_path
import pdf2image
import converterPDFtoJPEGView
import sys
import os

class ConverterPDFtoJPEGCore:

    def __init__(self) :
        self.view = None
        self.fromFolder = ""
        self.destFolder = ""
        self.fromPrefix = ""
        self.destPrefix = ""
        self.fromIndexBegin = 0
        self.fromIndexEnd = 0
        self.destIndexBegin = 0
        self.thread = None

    def setView(self, view):
        self.view = view

    def sendfromFolder(self, path) :
        self.fromFolder = path

    def senddestFolder(self, path) :
        self.destFolder = path

    def sendPrefix(self, fromPrefix, destPrefix) :
        self.fromPrefix = fromPrefix
        self.destPrefix = destPrefix

    def sendfromIndexBegin(self, index) :
        self.fromIndexBegin = int(index)
        self.refreshfromIndex()

    def sendfromIndexEnd(self, index) :
        self.fromIndexEnd = int(index)
        self.refreshfromIndex()

    def senddestIndexBegin(self, index) :
        self.destIndexBegin = int(index)

    def refreshfromIndex(self) :
        if self.fromIndexBegin == 0 : self.view.refreshIndexfrom(self.fromIndexBegin, self.fromIndexEnd)
        elif self.fromIndexBegin > self.fromIndexEnd: self.view.refreshIndexfrom(self.fromIndexBegin, self.fromIndexBegin+1)

    def checkAllData(self) :
        if self.fromFolder == "" : self.view.showAlert("from Folder is Missing")
        elif self.destFolder == "" : self.view.showAlert("dest Folder is Missing")
        else  : self.startConvertion()

    def startConvertion(self) :
        self.dir = os.listdir(self.fromFolder)
        self.view.setValueProgressBar(0,100)
        self.thread = QtCore.QThread()
        self.thread.started.connect(self.convert)
        self.thread.start()

    def convert(self) :
        j = self.destIndexBegin

        if self.fromIndexBegin == self.fromIndexEnd : # si les index de début et de fin sont les memes, importer tous les pdf
            for i, file in enumerate(self.dir,1) :
                if file[:len(self.fromPrefix)] == self.fromPrefix and file[-4:] == ".pdf" :
                    print(self.fromFolder+"\\"+file)
                    pdf = convert_from_path(self.fromFolder+"\\"+file, dpi=300)
                    j = self.convertIntoJPG(pdf, i)
                    self.view.setValueProgressBar(i,len(self.dir))
        else :
            for i in range(self.fromIndexBegin, self.fromIndexEnd+1) :
                if self.fromPrefix+self.reIndex(i)+".pdf" not in self.dir :
                    self.view.showAlert(self.fromPrefix+self.reIndex(i)+".pdf is missing")
                    return -1
            for i in range(self.fromIndexBegin, self.fromIndexEnd+1) :
                # pdf = wi(filename=self.fromFolder+"\\"+self.fromPrefix+self.reIndex(i)+".pdf").convert("jpeg")
                pdf = convert_from_path(self.fromFolder+"\\"+self.fromPrefix+self.reIndex(i)+".pdf", dpi=300)
                j = self.convertIntoJPG(pdf, i)
                self.view.setValueProgressBar(i,len(self.dir))
        self.thread.exit()

    def convertIntoJPG(self, sequence, index) :
        for img in sequence :
            # page = wi(image=img)
            # page.save(filename=self.destFolder+"\\"+self.destPrefix+self.reIndex(index)+".jpg")
            img.save(self.destFolder+"\\"+self.destPrefix+self.reIndex(index)+".jpg", "JPEG")
            index +=1
        return index

    def reIndex(self, i) :
        index = str(i)
        while len(index) < 4:
            index = "0"+index
        return index

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = converterPDFtoJPEGView.Ui_MainWindow()
    core = ConverterPDFtoJPEGCore()
    ui.setupUi(MainWindow)
    ui.setCore(core)
    core.setView(ui)
    MainWindow.show()
    sys.exit(app.exec_())
