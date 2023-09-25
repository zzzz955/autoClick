from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, QFrame

import dialogs
from dialogs import hot_Keys


class main_ui(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        frame1 = QFrame()
        frame1_layout1 = QVBoxLayout()
        frame1_layout2 = QHBoxLayout()
        frame1_layout3 = QHBoxLayout()
        frame2 = QFrame()
        frame2_layout1 = QVBoxLayout()
        frame2_layout2 = QHBoxLayout()
        label1 = QLabel('<b>실행 키 : <b>')
        self.lineedit1 = QLineEdit()
        label2 = QLabel('<b>종료 키 : <b>')
        self.lineedit2 = QLineEdit()
        btn1 = QPushButton('핫키 설정')

        label3 = QLabel('<b>[현재 마우스 좌표]<b>')
        self.label4 = QLabel('x, y')

        layout.addLayout(layout2)
        layout2.addWidget(frame1)
        frame1.setLayout(frame1_layout1)
        frame1_layout1.addLayout(frame1_layout2)
        frame1_layout2.addWidget(label1)
        frame1_layout2.addWidget(self.lineedit1)
        frame1_layout1.addLayout(frame1_layout3)
        frame1_layout3.addWidget(label2)
        frame1_layout3.addWidget(self.lineedit2)
        frame1_layout1.addWidget(btn1)

        layout2.addWidget(frame2)
        frame2.setLayout(frame2_layout1)
        frame2_layout1.addLayout(frame2_layout2)
        frame2_layout2.addWidget(label3)
        frame2_layout2.addWidget(self.label4)

        self.setLayout(layout)

        btn1.clicked.connect(self.conn_hotkey_dialog)

        self.lineedit1.setReadOnly(True)
        self.lineedit2.setReadOnly(True)

    def conn_hotkey_dialog(self):
        dialog = hot_Keys()
        dialog.data_submitted.connect(self.on_data_submitted)
        dialog.exec()

    def on_data_submitted(self, start_key, end_key):
        self.lineedit1.setText(start_key)
        self.lineedit2.setText(end_key)