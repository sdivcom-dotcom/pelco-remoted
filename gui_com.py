import sys
import time
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QCheckBox
from commands import *


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.nameLabel4 = QLabel(self)
        self.nameLabel4.setText('Zoom')
        self.nameLabel4.move(90, 160)
        zoom_plus = QPushButton('Zoom plus', self)
        zoom_plus.move(30, 190)
        zoom_plus.clicked.connect(self.zoom_plus_action)

        zoom_minus = QPushButton('Zoom minus', self)
        zoom_minus.move(30, 240)
        zoom_minus.clicked.connect(self.zoom_minus_action)

        self.nameLabel5 = QLabel(self)
        self.nameLabel5.setText('Focus')
        self.nameLabel5.move(160, 160)
        focus_plus = QPushButton('Focus plus', self)
        focus_plus.move(150, 190)
        focus_plus.clicked.connect(self.focus_plus_action)

        focus_minus = QPushButton('Focus minus', self)
        focus_minus.move(150, 240)
        focus_minus.clicked.connect(self.focus_minus_action)

        self.nameLabel6 = QLabel(self)
        self.nameLabel6.setText('Runner')
        self.nameLabel6.move(395, 10)

        up = QPushButton('UP', self)
        up.move(380, 30)
        up.clicked.connect(self.up_action)

        down = QPushButton('Down', self)
        down.move(380, 110)
        down.clicked.connect(self.down_action)

        left = QPushButton('Left', self)
        left.move(320, 70)
        left.clicked.connect(self.left_action)

        right = QPushButton('Right', self)
        right.move(420, 70)
        right.clicked.connect(self.right_action)

        self.nameLabel1 = QLabel(self)
        self.nameLabel1.setText('Port:')
        self.line1 = QLineEdit(self)

        self.nameLabel2 = QLabel(self)
        self.nameLabel2.setText('Baud rate:')
        self.line2 = QLineEdit(self)

        self.nameLabel3 = QLabel(self)
        self.nameLabel3.setText('Address:')
        self.line3 = QLineEdit(self)

        self.nameLabel8 = QLabel(self)
        self.nameLabel8.setText('Random command:')
        self.line4 = QLineEdit(self)

        self.line1.move(80, 30)
        self.line1.resize(200, 32)
        self.nameLabel1.move(10, 35)

        self.line2.move(80, 70)
        self.line2.resize(200, 32)
        self.nameLabel2.move(10, 75)

        self.line3.move(80, 110)
        self.line3.resize(200, 32)
        self.nameLabel3.move(10, 115)

        self.line4.move(270, 205)
        self.line4.resize(100, 32)
        self.nameLabel8.move(250, 185)

        send = QPushButton('Send', self)
        send.move(270, 245)
        send.clicked.connect(self.send_action)

        self.nameLabel7 = QLabel(self)
        self.nameLabel7.setText('PELCO Protocol')
        self.nameLabel7.move(410, 160)

        self.checkbox = QCheckBox('Pelo-D', self)
        self.checkbox.stateChanged.connect(self.checkbox_d)
        check = self.checkbox.isChecked()

        self.checkbox2 = QCheckBox('Pelo-P', self)
        self.checkbox2.stateChanged.connect(self.checkbox_p)
        check2 = self.checkbox2.isChecked()

        self.checkbox.move(400, 190)
        self.checkbox2.move(400, 230)

        self.setGeometry(100, 100, 600, 300)
        self.setWindowTitle('pelco-remote v.0.1')
        self.show()

    def checkbox_d(self, checked):
        pass

    def checkbox_p(self, checked):
        pass

    def lines(self):
        val1 = self.line1.text()
        val2 = self.line2.text()
        val3 = self.line3.text()
        val_mas = [val1, val2, val3]
        return val_mas

    def zoom_plus_action(self):
        val_mas = self.lines()
        port = val_mas[0]
        baud = val_mas[1]
        address = val_mas[2]
        val = self.checkbox.isChecked()
        if val is True:
            protocol = "d"
        else:
            pass
        val2 = self.checkbox2.isChecked()
        if val2 is True:
            protocol = "p"
        else:
            pass
        zoom_plus(port, baud, address, protocol)

    def zoom_minus_action(self):
        val_mas = self.lines()
        port = val_mas[0]
        baud = val_mas[1]
        address = val_mas[2]
        val = self.checkbox.isChecked()
        if val is True:
            protocol = "d"
        else:
            pass
        val2 = self.checkbox2.isChecked()
        if val2 is True:
            protocol = "p"
        else:
            pass
        zoom_minus(port, baud, address, protocol)

    def focus_plus_action(self):
        val_mas = self.lines()
        port = val_mas[0]
        baud = val_mas[1]
        address = val_mas[2]
        val = self.checkbox.isChecked()
        if val is True:
            protocol = "d"
        else:
            pass
        val2 = self.checkbox2.isChecked()
        if val2 is True:
            protocol = "p"
        else:
            pass
        focus_plus(port, baud, address, protocol)

    def focus_minus_action(self):
        val_mas = self.lines()
        port = val_mas[0]
        baud = val_mas[1]
        address = val_mas[2]
        val = self.checkbox.isChecked()
        if val is True:
            protocol = "d"
        else:
            pass
        val2 = self.checkbox2.isChecked()
        if val2 is True:
            protocol = "p"
        else:
            pass
        focus_minus(port, baud, address, protocol)

    def up_action(self):
        val_mas = self.lines()
        port = val_mas[0]
        baud = val_mas[1]
        address = val_mas[2]
        val = self.checkbox.isChecked()
        if val is True:
            protocol = "d"
        else:
            pass
        val2 = self.checkbox2.isChecked()
        if val2 is True:
            protocol = "p"
        else:
            pass
        up(port, baud, address, protocol)

    def down_action(self):
        val_mas = self.lines()
        port = val_mas[0]
        baud = val_mas[1]
        address = val_mas[2]
        val = self.checkbox.isChecked()
        if val is True:
            protocol = "d"
        else:
            pass
        val2 = self.checkbox2.isChecked()
        if val2 is True:
            protocol = "p"
        else:
            pass
        down(port, baud, address, protocol)

    def left_action(self):
        val_mas = self.lines()
        port = val_mas[0]
        baud = val_mas[1]
        address = val_mas[2]
        val = self.checkbox.isChecked()
        if val is True:
            protocol = "d"
        else:
            pass
        val2 = self.checkbox2.isChecked()
        if val2 is True:
            protocol = "p"
        else:
            pass
        left(port, baud, address, protocol)

    def right_action(self):
        val_mas = self.lines()
        port = val_mas[0]
        baud = val_mas[1]
        address = val_mas[2]
        val = self.checkbox.isChecked()
        if val is True:
            protocol = "d"
        else:
            pass
        val2 = self.checkbox2.isChecked()
        if val2 is True:
            protocol = "p"
        else:
            pass
        right(port, baud, address, protocol)

    def send_action(self):
        val_mas = self.lines()
        port = val_mas[0]
        baud = val_mas[1]
        address = val_mas[2]
        command = self.line4.text()
        val = self.checkbox.isChecked()
        if val is True:
            protocol = "d"
        else:
            pass
        val2 = self.checkbox2.isChecked()
        if val2 is True:
            protocol = "p"
        else:
            pass
        random_command(port, baud, address, protocol, command)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
