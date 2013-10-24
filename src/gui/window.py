# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../designer/katch.ui'
#
# Created: Thu Oct 24 16:29:54 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setStyleSheet(_fromUtf8(""))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.mainLayout = QtGui.QHBoxLayout()
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.connectionWidget = QtGui.QWidget()
        self.connectionWidget.setObjectName(_fromUtf8("connectionWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.connectionWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Connection = QtGui.QGroupBox(self.connectionWidget)
        self.Connection.setMinimumSize(QtCore.QSize(70, 150))
        self.Connection.setMaximumSize(QtCore.QSize(380, 100))
        self.Connection.setStyleSheet(_fromUtf8(""))
        self.Connection.setObjectName(_fromUtf8("Connection"))
        self.verticalLayout = QtGui.QVBoxLayout(self.Connection)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.Connection)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.ipAddressEdit = QtGui.QLineEdit(self.Connection)
        self.ipAddressEdit.setObjectName(_fromUtf8("ipAddressEdit"))
        self.horizontalLayout_3.addWidget(self.ipAddressEdit)
        self.connectButton = QtGui.QPushButton(self.Connection)
        self.connectButton.setStyleSheet(_fromUtf8("background-color: rgb(85, 85, 255);"))
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.horizontalLayout_3.addWidget(self.connectButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_2 = QtGui.QLabel(self.Connection)
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.Connection)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.connectionWidget)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)
        self.mainLayout.addWidget(self.stackedWidget)
        self.playerBox = QtGui.QGroupBox(Form)
        self.playerBox.setStyleSheet(_fromUtf8(""))
        self.playerBox.setObjectName(_fromUtf8("playerBox"))
        self.mainLayout.addWidget(self.playerBox)
        self.horizontalLayout_2.addLayout(self.mainLayout)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.Connection.setTitle(_translate("Form", "Connection", None))
        self.label.setText(_translate("Form", "Connection to peer (IP address):", None))
        self.connectButton.setText(_translate("Form", "Connect", None))
        self.label_2.setText(_translate("Form", " A peer can connect to you before you enter an address", None))
        self.playerBox.setTitle(_translate("Form", "Players", None))

