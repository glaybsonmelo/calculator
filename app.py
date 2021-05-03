import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QSizePolicy


class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator v1.0')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.numb_color = r'background: lightblue; color: black; font-weight: 700;'
        self.simb_color = r'background: royalblue; color: white; font-weight: 700;'

        self.setCentralWidget(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            r'* {background: white; color: #000; font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.add_btn(QPushButton('7'), 1, 0, 1, 1, style=self.numb_color)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1, style=self.numb_color)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1, style=self.numb_color)
        self.add_btn(QPushButton('/'), 1, 3, 1, 1, style=self.simb_color)
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1, lambda: self.display.setText(''),
            r'background: blueviolet; color: #fff; font-weight: 700;')

        self.add_btn(QPushButton('4'), 2, 0, 1, 1, style=self.numb_color)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1, style=self.numb_color)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1, style=self.numb_color)
        self.add_btn(QPushButton('*'), 2, 3, 1, 1, style=self.simb_color)
        self.add_btn(
            QPushButton('←'), 2, 4, 1, 1, lambda: self.display.setText(
                self.display.text()[:-1]),
                 r'background: blueviolet; color: #fff; font-weight: 700;')

        self.add_btn(QPushButton('1'), 3, 0, 1, 1, style=self.numb_color)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1, style=self.numb_color)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1, style=self.numb_color)
        self.add_btn(QPushButton('-'), 3, 3, 1, 1, style=self.simb_color)

        self.add_btn(QPushButton(' '), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1, style=self.numb_color)
        self.add_btn(QPushButton('.'), 4, 2, 1, 1, style=self.simb_color)
        self.add_btn(QPushButton('+'), 4, 3, 1, 1, style=self.simb_color)
        self.add_btn(QPushButton('='), 3, 4, 2, 1,
            self.eval_igaul,
             r'background: springgreen; color: black; font-weight: 700;')


    def add_btn(self, btn, row, col, rowspan, colspan, func=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not func:
            btn.clicked.connect(
            lambda: self.display.setText(self.display.text() + btn.text())
            )
        else:
            btn.clicked.connect(func)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        if style:
            btn.setStyleSheet(style)
    
    def eval_igaul(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except (SyntaxError, TypeError):
            print(self.display.setText('Conta inválida.'))


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    qt.exec_()
