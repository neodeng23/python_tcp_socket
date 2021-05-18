import sys
from Master_server_ui import Ui_MainWindow
from Update_data import Update_data
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
        self.thread = Update_data()
        self.thread.start()

    def closeEvent(self, event):
        result = QMessageBox.question(self, "注意：", "您真的要关闭窗体吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.thread.server_stop()
            self.thread.quit()
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyMainForm()
    mainWindow.show()
    sys.exit(app.exec_())
