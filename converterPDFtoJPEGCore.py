from PyQt5 import QtWidgets
import converterPDFtoJPEGView
import sys

class ConverterPDFtoJPEGCore:

    def __init__(self) :
        self.view = None
        self.destFolder = ""
        self.fromFolder = ""
        self.destPrefix = ""
        self.fromPrefix = ""
        self.destIndexBegin = 0
        self.destIndexEnd = 0
        self.fromIndexBegin = 0

    def setView(self, view):
        self.view = view

    def sendDestFolder(self, path) :
        self.destFolder = path

    def sendFromFolder(self, path) :
        self.fromFolder = path

    def sendPrefix(self, destPrefix, fromPrefix) :
        self.destPrefix = destPrefix
        self.fromPrefix = fromPrefix

    def sendDestIndexBegin(self, index) :
        self.destIndexBegin = index
        self.refreshDestIndex()

    def sendDestIndexEnd(self, index) :
        self.destIndexEnd = index
        self.refreshDestIndex()

    def sendFromIndexBegin(self, index) :
        self.fromIndexBegin = index

    def refreshDestIndex(self) :
        if self.destIndexBegin == 0 : self.view.refreshIndexDest(self.destIndexBegin, self.destIndexEnd)
        elif self.destIndexBegin > self.destIndexEnd: self.view.refreshIndexDest(self.destIndexBegin, self.destIndexBegin+1)

    def checkAllData(self) :
        if self.destFolder == "" : self.view.showAlert("Destination Folder is Missiong")
        elif self.fromFolder == "" : self.view.showAlert("From Folder is Missiong")


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
