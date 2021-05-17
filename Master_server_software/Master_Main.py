import sys
from Test_table import MyTable
from Master_server_ui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QFont
from PyQt5.QtCore import Qt

pe_red = QPalette()
pe_red.setColor(QPalette.WindowText, Qt.red)

pe_green = QPalette()
pe_green.setColor(QPalette.WindowText, Qt.green)

pe_yel = QPalette()
pe_yel.setColor(QPalette.WindowText, Qt.yellow)


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # self.thread = Update_data()
        # self.thread.sinOut.connect(self.test_Add)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyMainForm()
    mainWindow.show()
    sys.exit(app.exec_())

