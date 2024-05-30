import sys
import orbit_screen
from Receiver import Receiver
from PySide6.QtCore import QSize, Qt, QThreadPool, QEvent
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from orbit_screen import Ui_Dialog
import threading

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Orbit Simulator")
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        receiverInstance = Receiver(self.ui)
        thread = threading.Thread(target=receiverInstance.run)
        thread.start()
        #self.threadpool = QThreadPool()  
        #self.threadpool.start(receiverThread.run)      
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
#app.aboutToQuit.connect(Ui_Dialog.closeThreads)
