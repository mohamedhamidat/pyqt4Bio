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
from bio_validators import is_valid_dna
from bio_convertors import dna_to_rna, dna_to_protein
from bio_formators import clean_format_sequence

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
        message_color = COLOR_SUCCESS
        messages = ["please check an option"]
        try:
            if is_valid_dna(dna): 
                clean_dna = clean_format_sequence(dna)
                if self.ui.translate_to_rna_RadioBtn.isChecked():
                    messages[0] = dna_to_rna(clean_dna)
                elif self.ui.translate_to_prot_RadioBtn.isChecked():
                    messages = dna_to_protein(clean_dna)
                
                else: # no option has been checked than raise this exception
                    raise ValueError("please check an option")
                
                self.display_result(messages, message_color)    
            
        except ValueError as ex:
            self.display_error(str(ex))


    def display_result(self, messages, message_color):
        self.ui.result_textEdit.setEnabled(True)
        self.ui.result_textEdit.clear()
        self.ui.result_textEdit.setTextColor(message_color)
        self.ui.result_textEdit.setText("\n".join(messages))
    
    def display_error(self, message):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Warning)
        msg.setWindowTitle("Error has been raised")
        msg.setDetailedText(message)
        msg.exec_()
        

        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

