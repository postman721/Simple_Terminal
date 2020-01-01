#Simple Terminal Copyright (c) 2020 JJ Posti <techtimejourney.net> 
#This program comes with ABSOLUTELY NO WARRANTY; 
#for details see: http://www.gnu.org/copyleft/gpl.html. 
#This is free software, and you are welcome to redistribute it under 
#GPL Version 2, June 1991")
import os,sys; from PyQt5.QtCore import *; from PyQt5.QtGui import * ;from PyQt5.QtWidgets import *
class Main(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
#Title & Window definitions		
        self.setWindowTitle("Simple Terminal")
        self.setFixedSize(900, 700)          
        self.move(QApplication.desktop().screen().rect().center()- self.rect().center())
        self.setStyleSheet("color:#ffffff; background-color:#353535; border: 2px solid #353535; border-radius: 3px;font-size: 12px;")
#Process,widget,Layout
        self.process = QProcess(self)
        self.terminal = QWidget(self)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.terminal)
        self.process.start('rxvt',['-fg', 'white', '-bg', 'black', '-embed',str(int(self.winId()))])               
if __name__ == '__main__':
    app = QApplication(sys.argv); window = Main(); window.show(); sys.exit(app.exec_())
