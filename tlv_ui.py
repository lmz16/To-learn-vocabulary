from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
import json
import sys,random
import tlv_core

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(190, 259)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 20, 91, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 90, 91, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 160, 91, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "输入"))
        self.pushButton_2.setText(_translate("MainWindow", "测试"))
        self.pushButton_3.setText(_translate("MainWindow", "退出"))

class Ui_Input(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 278)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 301, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 400, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 160, 301, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 220, 91, 30))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "单词的英文"))
        self.label_2.setText(_translate("Form", "单词的中文(用‘，’隔开每个释义)"))
        self.pushButton.setText(_translate("Form", "完成"))


class Ui_Choose(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(273, 131)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(30, 50, 41, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(120, 50, 41, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(200, 50, 41, 31))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 90, 91, 30))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 20, 131, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton.setText(_translate("Form", "10"))
        self.radioButton_2.setText(_translate("Form", "20"))
        self.radioButton_3.setText(_translate("Form", "30"))
        self.pushButton.setText(_translate("Form", "完成"))
        self.label.setText(_translate("Form", "请选择测试题数"))

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(237, 80)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 151, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 40, 91, 30))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "您还未选择测试题数"))
        self.pushButton.setText(_translate("Dialog", "确定"))


class Ui_Answerbox(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(343, 326)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 20, 281, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 120, 121, 81))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 120, 121, 81))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 210, 121, 81))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 210, 121, 81))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 90, 91, 21))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class Ui_Prompt(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(390, 151)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 371, 81))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 110, 91, 30))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "确定"))


class mymainwindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mymainwindow,self).__init__()
        self.setupUi(self)
        center(self)
        self.show()
        self.pushButton_3.clicked.connect(self.close)
        self.filename='worddata'
        with open(self.filename,'r') as f_obj:
            self.tempdic=json.load(f_obj)


class myinputbox(QtWidgets.QMainWindow,Ui_Input):
    def __init__(self):
        super(myinputbox,self).__init__()
        self.setupUi(self)
        center(self)
        self.filename='worddata'
        self.tempdic={}

    def keyPressEvent(self,event):
        if(event.key()==16777220):
            if(QtWidgets.QWidget.hasFocus(self.lineEdit)):
                QtWidgets.QWidget.setFocus(self.lineEdit_2)
            else:
                if(self.lineEdit.text()):
                    self.tempdic[self.lineEdit.text()]=self.lineEdit_2.text().split('，')
                    self.lineEdit.clear()
                    self.lineEdit_2.clear()
                    QtWidgets.QWidget.setFocus(self.lineEdit)

    def inputcomplete(self,mainwindow):
        with open(self.filename,'w') as f_obj:
            json.dump(self.tempdic,f_obj)
        mainwindow.tempdic=self.tempdic
        self.close()

    def start(self,mainwindow):
        self.show()
        self.tempdic=mainwindow.tempdic


class mychoosebox(QtWidgets.QWidget,Ui_Choose):
    def __init__(self,dic):
        super().__init__()
        self.setupUi(self)
        center(self)
        self.questionNum=0
        self.radioButton_4.hide()
        self.tempdic=dic

    def choosecomplete(self,messagebox,answerbox):
        if(self.radioButton.isChecked()|self.radioButton_2.isChecked()| \
            self.radioButton_3.isChecked()):
            self.questionNum=self.radioButton.isChecked()*10+ \
            self.radioButton_2.isChecked()*20+ \
            self.radioButton_3.isChecked()*30
            self.radioButton_4.setChecked(True)
            answerbox.setFromCb(self.questionNum, \
            tlv_core.wordGrouping(self.tempdic,self.questionNum))
            answerbox.changeContent1()
            answerbox.show()
            self.close()
        else:
            messagebox.show()


class mymessagebox(QtWidgets.QWidget,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        center(self)


class myanswerbox(QtWidgets.QWidget,Ui_Answerbox):
    def __init__(self,dic):
        super().__init__()
        self.setupUi(self)
        center(self)
        self.questionNum=0
        self.count=0
        self.tempdic=dic
        self.wordGroup=[]
        self.answer=0

    def setFromCb(self,qn,wg):
        self.questionNum=qn
        self.wordGroup=wg

    def changeContent1(self):
        self.count=self.count+1
        self.label.setText('        '+str(self.count)+'/'+str(self.questionNum))
        self.answer=random.randint(0,3)
        self.pushButton.setText(tlv_core.wordWrap(tlv_core.chList2str \
        (self.tempdic[self.wordGroup[self.count-1][0]]),10))
        self.pushButton_2.setText(tlv_core.wordWrap(tlv_core.chList2str \
        (self.tempdic[self.wordGroup[self.count-1][1]]),10))
        self.pushButton_3.setText(tlv_core.wordWrap(tlv_core.chList2str \
        (self.tempdic[self.wordGroup[self.count-1][2]]),10))
        self.pushButton_4.setText(tlv_core.wordWrap(tlv_core.chList2str \
        (self.tempdic[self.wordGroup[self.count-1][3]]),10))
        self.textBrowser.setPlainText( \
        '请选择'+self.wordGroup[self.count-1][self.answer]+'的汉语意思')


class mypromptbox(QtWidgets.QWidget,Ui_Prompt):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        center(self)
        self.pushButton.clicked.connect(self.close)


def center(widget):
    screen = QDesktopWidget().screenGeometry()
    size = widget.geometry()
    widget.move((screen.width() - size.width()) / 2, \
    (screen.height() - size.height()) / 2)
