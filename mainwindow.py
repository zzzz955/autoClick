import sys
import time
import pyautogui
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel,\
    QLineEdit, QHBoxLayout, QFrame
from qt_material import apply_stylesheet


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("오토 클릭")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        frame1 = QFrame()
        frame1_layout1 = QVBoxLayout()
        frame1_layout2 = QHBoxLayout()
        frame1_layout3 = QHBoxLayout()
        frame2 = QFrame()
        frame2_layout1 = QVBoxLayout()
        frame2_layout2 = QHBoxLayout()
        frame2_layout3 = QHBoxLayout()
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

        central_widget.setLayout(layout)

        self.status = self.statusBar()
        frame2.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        x, y = event.globalX(), event.globalY()
        self.status.showMessage(f"{x}, {y}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())