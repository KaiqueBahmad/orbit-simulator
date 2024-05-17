import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from orbit_screen import Ui_Dialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Orbit Simulator")
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
""" 
    def mousePressEvent(self, event: QMouseEvent):
        if QMouseEvent == Qt.MouseButton.LeftButton:
            float  cordIni = QMouseEvent.globalPosition """
        
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()