from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QDialog, QFrame, QMessageBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp


class hot_Keys(QDialog):
    data_submitted = pyqtSignal(str, str)
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        frame1 = QFrame()
        frame1_layout1 = QVBoxLayout()
        frame1_layout2 = QHBoxLayout()
        frame1_layout3 = QHBoxLayout()
        frame1_layout4 = QHBoxLayout()
        label1 = QLabel('<b>실행 키 설정 : Ctrl +<b>')
        self.lineedit1 = QLineEdit()
        label2 = QLabel('<b>종료 키 설정 : Ctrl +<b>')
        self.lineedit2 = QLineEdit()
        btn1 = QPushButton('적용')
        btn2 = QPushButton('취소')

        layout.addLayout(layout2)
        layout2.addWidget(frame1)
        frame1.setLayout(frame1_layout1)
        frame1_layout1.addLayout(frame1_layout2)
        frame1_layout2.addWidget(label1)
        frame1_layout2.addWidget(self.lineedit1)
        frame1_layout1.addLayout(frame1_layout3)
        frame1_layout3.addWidget(label2)
        frame1_layout3.addWidget(self.lineedit2)
        frame1_layout1.addLayout(frame1_layout4)
        frame1_layout4.addWidget(btn1)
        frame1_layout4.addWidget(btn2)
        self.setLayout(layout)

        btn1.clicked.connect(self.fending_val)
        btn2.clicked.connect(self.reject)

        regex = QRegExp("^[a-zA-Z]{1}$")  # 영문자만 입력 허용
        validator = QRegExpValidator(regex)
        self.lineedit1.setValidator(validator)
        self.lineedit2.setValidator(validator)

    def fending_val(self):
        if self.lineedit1.text().upper() == self.lineedit2.text().upper():
            QMessageBox.warning(self, '경고', '시작과 종료 단축키가 동일할 수 없습니다.')
        elif self.lineedit1.text() and self.lineedit2.text():
            start_key, end_key = self.lineedit1.text().upper(), self.lineedit2.text().upper()
            self.data_submitted.emit(start_key, end_key)
            self.accept()
        else:
            QMessageBox.warning(self, '경고', '정확한 값이 입력 되었는지 확인해 주세요.')