from PyQt5.QtWidgets import*
import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog
from math import *


class Calculator(QWidget):
    def __init__(self):
        super(Calculator,self).__init__()


        self.panel = QLineEdit()

        self.resultPanel = QLabel()


#=============================================================================================================================

        self.equalBtn = QPushButton("=")
        self.clrBtn = QPushButton("C")
        self.plusBtn = QPushButton("+")
        self.DelBtn = QPushButton("DEL")
#=============================================================================================================================
        self.minusBtn = QPushButton("-")
        self.divideBtn = QPushButton("/")
        self.multiBtn = QPushButton("*")
        self.rootBtn = QPushButton("v")
#============================================================================================================================
        self.cosBtn  = QPushButton("cos")
        self.tanBtn = QPushButton("tan")
        self.sinBtn = QPushButton("sin")
        self.Bbtn = QPushButton("(")
        self.Bbtn2 = QPushButton(")")
        self.Ebtn = QPushButton("e")
#=================================================================================================================================
        self.but1 = QPushButton("1")
        self.but2 = QPushButton("2")
        self.but3 = QPushButton("3")
        self.but4 = QPushButton("4")
        self.but5 = QPushButton("5")
        self.but6 = QPushButton("6")
        self.but7 = QPushButton("7")
        self.but8 = QPushButton("8")
        self.but9 = QPushButton("9")
        self.but0 = QPushButton("0")
        self.PiBtn = QPushButton("p")
        self.log10btn = QPushButton("log10")
        self.AnsBtn = QPushButton("Ans")

#==========================================================Error dialog============================================================
        self.error_dialog =QErrorMessage()
#=================================================================================================================================
        self.init_ui()

    def init_ui(self):
        vlayout = QVBoxLayout()
        hlayout = QHBoxLayout()
        hlayout2 = QHBoxLayout()
        hlayout3 = QHBoxLayout()
        hlayout4 = QHBoxLayout()
        hlayout5 = QHBoxLayout()


        hlayout2.addWidget(self.multiBtn)
        hlayout.addWidget(self.clrBtn)
        hlayout.addWidget(self.plusBtn)
        hlayout.addWidget(self.rootBtn)
        hlayout.addWidget(self.DelBtn)

        hlayout2.addWidget( self.minusBtn)
        hlayout2.addWidget(self.divideBtn)
        hlayout.addWidget(self.equalBtn)
        hlayout2.addWidget(self.log10btn)
        hlayout.addWidget(self.Ebtn)
        #hlayout2.addWidget(self.AnsBtn)



        hlayout3.addWidget( self.cosBtn)
        hlayout3.addWidget(self.tanBtn)
        hlayout3.addWidget(self.sinBtn)
        hlayout3.addWidget(self.Bbtn)
        hlayout3.addWidget(self.Bbtn2)

        hlayout4.addWidget(self.but1)
        hlayout4.addWidget(self.but2)
        hlayout4.addWidget(self.but3)
        hlayout4.addWidget(self.but4)
        hlayout4.addWidget(self.but5)

        hlayout5.addWidget(self.but6)
        hlayout5.addWidget(self.but7)
        hlayout5.addWidget(self.but8)
        hlayout5.addWidget(self.but9)
        hlayout5.addWidget(self.but0)
        hlayout5.addWidget(self.PiBtn)




        vlayout.addWidget(self.panel)
        vlayout.addWidget(self.resultPanel)

        vlayout.addLayout(hlayout)
        vlayout.addLayout(hlayout2)
        vlayout.addLayout(hlayout3)
        vlayout.addLayout(hlayout4)
        vlayout.addLayout(hlayout5)



        self.setLayout(vlayout)
        self.equalBtn.clicked.connect(self.equalbtnf)
        self.clrBtn.clicked.connect(self.Clearbtnf)
    #==========================================symbols===========================================================================
        self.minusBtn.clicked.connect(lambda x:self.Stringbtnf(self.minusBtn.text()))
        self.plusBtn.clicked.connect(lambda x:self.Stringbtnf(self.plusBtn.text()))
        self.multiBtn.clicked.connect(lambda x:self.Stringbtnf(self.multiBtn.text()))
        self.divideBtn.clicked.connect(lambda x:self.Stringbtnf(self.divideBtn.text()))
        self.rootBtn.clicked.connect(lambda x:self.Stringbtnf("sqrt("))
        self.cosBtn.clicked.connect(lambda x:self.Stringbtnf("cos("))
        self.sinBtn.clicked.connect(lambda x:self.Stringbtnf("sin("))
        self.tanBtn.clicked.connect(lambda x:self.Stringbtnf("tan("))
        self.Bbtn.clicked.connect(lambda x:self.Stringbtnf(self.Bbtn.text()))
        self.Bbtn2.clicked.connect(lambda x:self.Stringbtnf(self.Bbtn2.text()))
        self.log10btn.clicked.connect(lambda x:self.Stringbtnf("log10("))
        self.Ebtn.clicked.connect(lambda x:self.Stringbtnf("e"))

    #==========================================Numbers============================================================================
        self.but1.clicked.connect(lambda x:self.Stringbtnf(self.but1.text()))
        self.but2.clicked.connect(lambda x: self.Stringbtnf(self.but2.text()))
        self.but3.clicked.connect(lambda x: self.Stringbtnf(self.but3.text()))
        self.but4.clicked.connect(lambda x: self.Stringbtnf(self.but4.text()))
        self.but5.clicked.connect(lambda x: self.Stringbtnf(self.but5.text()))
        self.but6.clicked.connect(lambda x: self.Stringbtnf(self.but6.text()))
        self.but7.clicked.connect(lambda x: self.Stringbtnf(self.but7.text()))
        self.but8.clicked.connect(lambda x: self.Stringbtnf(self.but8.text()))
        self.but9.clicked.connect(lambda x: self.Stringbtnf(self.but9.text()))
        self.but0.clicked.connect(lambda x: self.Stringbtnf(self.but0.text()))
        self.PiBtn.clicked.connect(lambda x: self.Stringbtnf("p"))
        self.DelBtn.clicked.connect(self.DelBtnf)
        self.AnsBtn.clicked.connect(self.AnsBtnf)
    #==============================================================================================================================
        self.setWindowTitle("Calculator")
        self.show()

    def Stringbtnf(self,txt):

        op = self.panel.text() + txt
        self.panel.setText(op)

    def equalbtnf(self):

        try:
            op = self.panel.text()
            p = 3.141592
            e = 2.718281
            op1 = str(eval(op))
            self.resultPanel.setText(op1)


        except ZeroDivisionError:
            error = sys.exc_info()[0]
            self.resultPanel.setText("Division By Zero")


        except SyntaxError:
            error = sys.exc_info()[0]
            self.resultPanel.setText("Syntax Error")

        except Exception as e:
            error = sys.exc_info()[0]
            self.error_dialog.showMessage("""An un expected error has ocuured.
             This message only appears when there is a system error
              If restarting the app does not fix this please contact us"""  )
            self.error_dialog.setWindowTitle("Error" + " " + str(e))




    def Clearbtnf(self):
        self.resultPanel.setText("  ")
        self.panel.setText("  ")

    def DelBtnf(self):
        home = self.panel.text()
        op = home[0:len(home) - 1]
        self.panel.setText(op)
    def AnsBtnf(self):
       pass





app = QApplication(sys.argv)
Calc = Calculator()
sys.exit(app.exec_())
