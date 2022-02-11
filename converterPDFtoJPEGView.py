from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import converterPDFtoJPEGCore
import converterPDFtoJPEGAlertDialog
import sys

class Ui_MainWindow(object):
    def __init__(self):
        self.core = None

    def setupUi(self, MainWindow) :
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 246)
        self.initComponents(MainWindow)
        self.initLayout(MainWindow)
        self.initConnect()

    def setCore(self, core) :
        self.core = core

    def initComponents(self, MainWindow) :
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.destLabel = QtWidgets.QLabel("Destination Folder")
        self.destEdit = QtWidgets.QLineEdit()
        self.destEdit.setReadOnly(True)

        self.indexBeginLabel = QtWidgets.QLabel("index begin")
        self.indexEndLabel = QtWidgets.QLabel("index end")
        self.destPrefixLabel = QtWidgets.QLabel("Image Prefix:")
        self.destPrefixInput = QtWidgets.QLineEdit()
        self.destIndexBegin = QtWidgets.QSpinBox()
        self.destIndexBegin.setMaximum(999999)
        self.destIndexEnd = QtWidgets.QSpinBox()
        self.destIndexEnd.setMaximum(999999)

        self.separator = QtWidgets.QWidget()
        self.separator.setStyleSheet("background-color:black;")

        self.fromLabel = QtWidgets.QLabel("From Folder")
        self.fromEdit = QtWidgets.QLineEdit()
        self.fromEdit.setReadOnly(True)

        self.fromPrefixLabel = QtWidgets.QLabel("Image Prefix:")
        self.fromindexBeginLabel = QtWidgets.QLabel("index begin")
        self.fromPrefixInput = QtWidgets.QLineEdit()
        self.fromIndexBegin = QtWidgets.QSpinBox()
        self.fromIndexBegin.setMaximum(999999)

        self.separator2 = QtWidgets.QWidget()
        self.separator2.setStyleSheet("background-color:black;")

        self.convertButton = QtWidgets.QPushButton("Convert")

    def initLayout(self, MainWindow) :
        self.vbox = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vbox.addWidget(self.destLabel)
        self.vbox.addWidget(self.fromLabel)
        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox2 = QtWidgets.QHBoxLayout()
        self.hbox3 = QtWidgets.QHBoxLayout()
        self.hbox4 = QtWidgets.QHBoxLayout()

        self.hbox1.addWidget(self.destLabel)
        self.hbox1.addWidget(self.destEdit)

        self.hbox2.addWidget(self.destPrefixLabel)
        self.hbox2.addWidget(self.destPrefixInput)
        self.hbox2.addWidget(self.indexBeginLabel)
        self.hbox2.addWidget(self.destIndexBegin)
        self.hbox2.addWidget(self.indexEndLabel)
        self.hbox2.addWidget(self.destIndexEnd)

        self.hbox3.addWidget(self.fromLabel)
        self.hbox3.addWidget(self.fromEdit)

        self.hbox4.addWidget(self.fromPrefixLabel)
        self.hbox4.addWidget(self.fromPrefixInput)
        self.hbox4.addWidget(self.fromindexBeginLabel)
        self.hbox4.addWidget(self.fromIndexBegin)

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self.separator)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addWidget(self.separator2)
        self.vbox.addWidget(self.convertButton)


    def initConnect(self) :
        self.destEdit.selectionChanged.connect(self.openFolderDest)
        self.fromEdit.selectionChanged.connect(self.openFolderFrom)
        self.convertButton.clicked.connect(self.tapOnConvertButton)
        self.destIndexBegin.valueChanged.connect(self.destIndexBeginChanged)
        self.destIndexEnd.valueChanged.connect(self.destIndexEndChanged)
        self.fromIndexBegin.valueChanged.connect(self.fromIndexBeginChanged)

    def openFolderDest(self) :
        fname = QtWidgets.QFileDialog.getExistingDirectory()
        if fname :
            self.destEdit.setText(fname)
            self.core.sendDestFolder(fname)

    def openFolderFrom(self) :
        fname = QtWidgets.QFileDialog.getExistingDirectory()
        if fname :
            self.fromEdit.setText(fname)
            self.core.sendFromFolder(fname)

    def destIndexBeginChanged(self, value) :
        self.core.sendDestIndexBegin(value)

    def destIndexEndChanged(self, value) :
        self.core.sendDestIndexEnd(value)

    def fromIndexBeginChanged(self, value) :
        self.core.sendFromIndexBegin(value)

    def refreshIndexDest(self, indexBegin, indexEnd) :
        self.destIndexEnd.setValue(indexEnd)

    def tapOnConvertButton(self) :
        self.core.checkAllData()

    def showAlert(self, message) :
        u_dialog = QtWidgets.QDialog()
        dialog = converterPDFtoJPEGAlertDialog.ConverterPDFtoJPEGAlertDialog(u_dialog, message)
        u_dialog.exec_()


if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    core = converterPDFtoJPEGCore.ConverterPDFtoJPEGCore()
    ui.setupUi(MainWindow)
    ui.setCore(core)
    core.setView(ui)
    MainWindow.show()
    sys.exit(app.exec_())
