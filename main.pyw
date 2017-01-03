import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QApplication
#from PyQt5 import QtCore, QtGui

from View import MainWindow


class BookManager(QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(BookManager, self).__init__(parent)
        self.setupUi(self)
        self.actionExit.triggered.connect(qApp.quit)


if __name__ == '__main__':
    a = QApplication(sys.argv)
    app = BookManager()
    app.show()
    a.exec_()
