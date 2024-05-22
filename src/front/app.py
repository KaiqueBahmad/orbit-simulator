import sys
import Receiver

from PySide6.QtCore import QSize, Qt, QThreadPool
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from orbit_screen import Ui_Dialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Orbit Simulator")
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()  
        receiverThread = Receiver.Receiver()
        self.threadpool.start(receiverThread.run)      
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()