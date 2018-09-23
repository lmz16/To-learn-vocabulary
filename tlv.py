from PyQt5 import QtCore, QtGui, QtWidgets
import sys,random

import tlv_ui,tlv_core

app=QtWidgets.QApplication(sys.argv)

ui_mainwindow=tlv_ui.mymainwindow()
ui_inputbox=tlv_ui.myinputbox()
ui_choosebox=tlv_ui.mychoosebox(ui_mainwindow.tempdic)
ui_messagebox=tlv_ui.mymessagebox()
ui_answerbox=tlv_ui.myanswerbox(ui_mainwindow.tempdic)
ui_promptbox=tlv_ui.mypromptbox()

ui_mainwindow.pushButton.clicked.connect(lambda:ui_inputbox.start(ui_mainwindow))
ui_mainwindow.pushButton_2.clicked.connect(ui_choosebox.show)

ui_inputbox.pushButton.clicked.connect(lambda:ui_inputbox.inputcomplete(ui_mainwindow))

ui_choosebox.pushButton.clicked.connect(lambda:ui_choosebox.choosecomplete(ui_messagebox,ui_answerbox))

ui_answerbox.pushButton.clicked.connect(lambda:tlv_core.AnswerButtonSlot(ui_answerbox,0,ui_promptbox))
ui_answerbox.pushButton_2.clicked.connect(lambda:tlv_core.AnswerButtonSlot(ui_answerbox,1,ui_promptbox))
ui_answerbox.pushButton_3.clicked.connect(lambda:tlv_core.AnswerButtonSlot(ui_answerbox,2,ui_promptbox))
ui_answerbox.pushButton_4.clicked.connect(lambda:tlv_core.AnswerButtonSlot(ui_answerbox,3,ui_promptbox))

sys.exit(app.exec_())
