#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Hi everyone, 
This project is in progress ..........
This is a simple UI developed to do some basic bioinformatics analysis using Python3, PyQt4 & Qt Designer 
"""
__author__  = "Mohamed Hamidat, C# and python Developer, hamidatmohamed@yahoo.fr"

from PyQt4 import QtGui, QtCore
from window import Ui_QtBio
import bio_validators
import bio_convertors

HEIGHT = 800
WIDTH = 1350
COLOR_ERROR = QtGui.QColor("red")
COLOR_SUCCESS = QtGui.QColor("green")

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_QtBio()
        self.ui.setupUi(self)
        self.setFixedSize(WIDTH, HEIGHT)
        self.ui.SubmitButton.clicked.connect(self.process_sequence)

    def process_sequence(self):
        """
        get dna sequence from text editor 
        check if sequence is valid 
        raise ValueError if not valid
        """
        dna = self.ui.sequence_textEdit.toPlainText()
        message_color = COLOR_ERROR
        messages = ["please check an option"]
        try:
            if bio_validators.is_valid_dna(dna): 
                message_color = COLOR_SUCCESS
                if self.ui.translate_to_rna_RadioBtn.isChecked():
                    messages[0] = bio_convertors.dna_to_rna(dna)
                elif self.ui.translate_to_prot_RadioBtn.isChecked():
                    messages = bio_convertors.dna_to_protein(dna)
                
        except ValueError as ex:
            messages[0] = (str(ex))

        self.display_result(messages, message_color)

    def display_result(self, messages, message_color):
        self.ui.result_textEdit.setEnabled(True)
        self.ui.result_textEdit.clear()
        self.ui.result_textEdit.setTextColor(message_color)
        self.ui.result_textEdit.setText("\n".join(messages))
        

        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

