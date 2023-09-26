import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import main_ui
from clickFunc import click_Func
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from qt_material import apply_stylesheet


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("오토 클릭")
        ui = main_ui()
        self.click = click_Func()
        self.setCentralWidget(ui)

    def keyPressEvent(self, event):
        self.click.key_pressed(event.key())
        super().keyPressEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())