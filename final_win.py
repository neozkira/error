from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
      
from instr import *


class FinalWin(QWidget):
    def __init__(self, exp):
        ''' окно, в котором проводится опрос '''
        super().__init__()


        # создаём и настраиваем графические элементы:
        self.initUI()


        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
        
        # старт:
        self.show()

        self.exp = exp
    def initUI(self):
        ''' создаёт графические элементы '''
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)


        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)        
        self.setLayout(self.layout_line)


    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def results(self):
        if self.exp.age <7:
            self.index = 0
            return 'нет данныз для такого возраста'
        self.index=(4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if self.exp.age ==7 or self.exp.age ==8:
            if self.index >=21:
                return txt_res1
            elif self.index <21 and self.index >=17:
                return txt_res2
            elif self.index < 18 and self.index >=12:
                return txt_res3
            elif self.index < 12 and self.index >=6.5:
                return txt_res4
            else:
                return txt_res5