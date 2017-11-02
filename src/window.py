# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_QtBio(object):
    def setupUi(self, QtBio):
        QtBio.setObjectName(_fromUtf8("QtBio"))
        QtBio.setEnabled(True)
        QtBio.resize(1333, 614)
        QtBio.setAnimated(True)
        QtBio.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(QtBio)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 241, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.SubmitButton = QtGui.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(1160, 230, 131, 61))
        self.SubmitButton.setObjectName(_fromUtf8("SubmitButton"))
        self.translate_to_rna_RadioBtn = QtGui.QRadioButton(self.centralwidget)
        self.translate_to_rna_RadioBtn.setGeometry(QtCore.QRect(40, 250, 191, 27))
        self.translate_to_rna_RadioBtn.setObjectName(_fromUtf8("translate_to_rna_RadioBtn"))
        self.result_textEdit = QtGui.QTextEdit(self.centralwidget)
        self.result_textEdit.setEnabled(False)
        self.result_textEdit.setGeometry(QtCore.QRect(40, 320, 1251, 191))
        self.result_textEdit.setObjectName(_fromUtf8("result_textEdit"))
        self.sequence_textEdit = QtGui.QTextEdit(self.centralwidget)
        self.sequence_textEdit.setGeometry(QtCore.QRect(30, 50, 1261, 171))
        self.sequence_textEdit.setObjectName(_fromUtf8("sequence_textEdit"))
        QtBio.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(QtBio)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1333, 36))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        QtBio.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(QtBio)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        QtBio.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(QtBio)
        QtCore.QMetaObject.connectSlotsByName(QtBio)

    def retranslateUi(self, QtBio):
        QtBio.setWindowTitle(_translate("QtBio", "QtBio", None))
        self.label.setText(_translate("QtBio", "DNA Sequence (>ATGC)", None))
        self.SubmitButton.setText(_translate("QtBio", "Submit", None))
        self.translate_to_rna_RadioBtn.setText(_translate("QtBio", "Translate to RNA", None))
        self.menuMenu.setTitle(_translate("QtBio", "Menu", None))

