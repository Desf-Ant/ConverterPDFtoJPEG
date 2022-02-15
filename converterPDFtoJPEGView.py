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

        self.fromLabel = QtWidgets.QLabel("From Folder")
        self.fromEdit = QtWidgets.QLineEdit()
        self.fromEdit.setReadOnly(True)

        self.indexBeginLabel = QtWidgets.QLabel("index begin")
        self.indexEndLabel = QtWidgets.QLabel("index end")
        self.fromPrefixLabel = QtWidgets.QLabel("Image Prefix:")
        self.fromPrefixInput = QtWidgets.QLineEdit()
        self.fromIndexBegin = QtWidgets.QSpinBox()
        self.fromIndexBegin.setMaximum(999999)
        self.fromIndexEnd = QtWidgets.QSpinBox()
        self.fromIndexEnd.setMaximum(999999)

        self.separator = QtWidgets.QWidget()
        self.separator.setStyleSheet("background-color:black;")

        self.destLabel = QtWidgets.QLabel("Destination Folder")
        self.destEdit = QtWidgets.QLineEdit()
        self.destEdit.setReadOnly(True)

        self.destPrefixLabel = QtWidgets.QLabel("Image Prefix:")
        self.destindexBeginLabel = QtWidgets.QLabel("index begin")
        self.destPrefixInput = QtWidgets.QLineEdit()
        self.destIndexBegin = QtWidgets.QSpinBox()
        self.destIndexBegin.setMaximum(999999)

        self.separator2 = QtWidgets.QWidget()
        self.separator2.setStyleSheet("background-color:black;")

        self.convertButton = QtWidgets.QPushButton("Convert")
        self.progress = QtWidgets.QProgressBar()
        self.progress.setAlignment(QtCore.Qt.AlignCenter)

    def initLayout(self, MainWindow) :
        self.vbox = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vbox.addWidget(self.fromLabel)
        self.vbox.addWidget(self.destLabel)
        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox2 = QtWidgets.QHBoxLayout()
        self.hbox3 = QtWidgets.QHBoxLayout()
        self.hbox4 = QtWidgets.QHBoxLayout()

        self.hbox1.addWidget(self.fromLabel)
        self.hbox1.addWidget(self.fromEdit)

        self.hbox2.addWidget(self.fromPrefixLabel)
        self.hbox2.addWidget(self.fromPrefixInput)
        self.hbox2.addWidget(self.indexBeginLabel)
        self.hbox2.addWidget(self.fromIndexBegin)
        self.hbox2.addWidget(self.indexEndLabel)
        self.hbox2.addWidget(self.fromIndexEnd)

        self.hbox3.addWidget(self.destLabel)
        self.hbox3.addWidget(self.destEdit)

        self.hbox4.addWidget(self.destPrefixLabel)
        self.hbox4.addWidget(self.destPrefixInput)
        self.hbox4.addWidget(self.destindexBeginLabel)
        self.hbox4.addWidget(self.destIndexBegin)

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self.separator)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addWidget(self.separator2)
        self.vbox.addWidget(self.convertButton)
        self.vbox.addWidget(self.progress)


    def initConnect(self) :
        self.fromEdit.selectionChanged.connect(self.openFolderfrom)
        self.destEdit.selectionChanged.connect(self.openFolderdest)
        self.convertButton.clicked.connect(self.tapOnConvertButton)
        self.fromIndexBegin.valueChanged.connect(self.fromIndexBeginChanged)
        self.fromIndexEnd.valueChanged.connect(self.fromIndexEndChanged)
        self.destIndexBegin.valueChanged.connect(self.destIndexBeginChanged)
        self.destPrefixInput.textChanged.connect(self.refreshPrefix)
        self.fromPrefixInput.textChanged.connect(self.refreshPrefix)

    def openFolderfrom(self) :
        fname = QtWidgets.QFileDialog.getExistingDirectory()
        if fname :
            self.fromEdit.setText(fname)
            self.core.sendfromFolder(fname)

    def openFolderdest(self) :
        fname = QtWidgets.QFileDialog.getExistingDirectory()
        if fname :
            self.destEdit.setText(fname)
            self.core.senddestFolder(fname)

    def fromIndexBeginChanged(self, value) :
        self.core.sendfromIndexBegin(value)

    def fromIndexEndChanged(self, value) :
        self.core.sendfromIndexEnd(value)

    def destIndexBeginChanged(self, value) :
        self.core.senddestIndexBegin(value)

    def refreshIndexfrom(self, indexBegin, indexEnd) :
        self.fromIndexEnd.setValue(indexEnd)

    def refreshPrefix(self) :
        self.core.sendPrefix(self.fromPrefixInput.text(), self.destPrefixInput.text())

    def tapOnConvertButton(self) :
        self.core.checkAllData()

    def showAlert(self, message) :
        u_dialog = QtWidgets.QDialog()
        dialog = converterPDFtoJPEGAlertDialog.ConverterPDFtoJPEGAlertDialog(u_dialog, message)
        u_dialog.exec_()

    def setValueProgressBar(self, val, max) :
        self.progress.setValue(val/max*100)


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
