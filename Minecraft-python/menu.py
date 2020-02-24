# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui',
# licensing of 'menu.ui' applies.
#
# Created: Mon Sep 23 16:47:57 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(906, 519)
        Form.setMinimumSize(QtCore.QSize(906, 519))
        Form.setMaximumSize(QtCore.QSize(906, 519))
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 906, 519))
        self.label_2.setStyleSheet("image: url(textures/ui/background.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 50, 501, 171))
        self.label.setStyleSheet("image: url(textures/ui/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 224, 499, 51))
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_3.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_3.setStyleSheet("border-image: url(textures/ui/button1.png);\n"
"font: 75 8pt \"System\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 360, 499, 41))
        self.pushButton.setStyleSheet("border-image: url(textures/ui/button1.png);\n"
"font: 75 8pt \"System\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 428, 499, 41))
        self.pushButton_4.setStyleSheet("border-image: url(textures/ui/button1.png);\n"
"font: 75 8pt \"System\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 290, 499, 51))
        self.pushButton_2.setStyleSheet("border-image: url(textures/ui/button1.png);\n"
"font: 75 8pt \"System\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Minecraft python", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Form", "Play singleplayer", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "Texture Pack", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("Form", "Quit", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "Multiplayer", None, -1))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    #logik
    def bp1():
        Form.setWindowOpacity(0.1)
        import main
        Form.setWindowOpacity(1.0)
        pass
    def bp2():
        pass
    def bp3():
        pass
    def bp4():
        exit()
        pass
    ui.pushButton_4.clicked.connect( bp4 )
    ui.pushButton_3.clicked.connect( bp1 )
    #end
    sys.exit(app.exec_())




