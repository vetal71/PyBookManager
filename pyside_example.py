import sys

from PySide.QtGui import *


class Form(QMainWindow):

    # конструктор
    def __init__(self):
        # конструктор базового класса
        super(Form, self).__init__()
        # вызов метода построения интерфейса
        self.initui()

        """
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type")
        self.lineedit.selectAll()

        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)

        self.lineedit.setFocus()
        """

    def initui(self):
        self.statusBar().showMessage("Готово")

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Библиотека книг")
        self.show()


def main():
    app = QApplication(sys.argv)
    form = Form()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
