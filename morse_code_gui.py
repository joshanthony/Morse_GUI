import sys
import time
import RPi.GPIO as GPIO

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

pin_red = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_red, GPIO.OUT)

MORSE_CODE = {  'A':'.-',
                'B':'-...',
                'C':'-.-.',
                'D':'-..',
                'E':'.',
                'F':'..-.',
                'G':'--.',
                'H':'....',
                'I':'..',
                'J':'.---',
                'K':'-.-',
                'L':'.-..',
                'M':'--',
                'N':'-.',
                'O':'---',
                'P':'.--.',
                'Q':'--.-',
                'R':'.-.',
                'S':'...',
                'T':'-',
                'U':'..-',
                'V':'...-',
                'W':'.--',
                'X':'-..-',
                'Y':'-.--',
                'Z':'--..' }


class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def moseCodeConverter(self, msg):
        code = ''
        for m in msg:
            code += MORSE_CODE[m.upper()] + ' '
        return code

    def moseCodeBroadcast(self, code):
        for c in code:
            if c == " ":
                time.sleep(0.3)
            if c == ".":
                GPIO.output(pin_red, GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(pin_red, GPIO.LOW)
                time.sleep(0.3)
            if c == "-":
                GPIO.output(pin_red, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(pin_red, GPIO.LOW)
                time.sleep(0.3)

    def initUI(self):
        self.prompt = QLabel("Convert text to morse code:")
        self.textbox = QLineEdit(self)
        self.btn = QPushButton('Convert', self)
        self.confirmation = QLabel("")

        # connect button to function on_click
        self.btn.clicked.connect(self.onClick)

        grid = QGridLayout(self)

        self.setWindowTitle('Task 5.3')

        grid.addWidget(self.prompt, 1, 0)
        grid.addWidget(self.textbox, 2, 0)
        grid.addWidget(self.btn, 3, 0)
        grid.addWidget(self.confirmation, 4, 0)
        self.show()

    @pyqtSlot()
    def onClick(self):
        msg = self.textbox.text()
        self.textbox.setText("")
        code = self.moseCodeConverter(msg)
        self.moseCodeBroadcast(code)
        self.confirmation.setText(msg + " was converted to morse code")

if __name__ == '__main__':
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    ex = MorseCode()
    sys.exit(app.exec_())