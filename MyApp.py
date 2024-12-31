from PyQt6.QtWidgets import QApplication, QMainWindow

from Chapter_1.Ex24.ui.MainWidowEx import MainWindowEx

app = QApplication([])
mainwindow = QMainWindow()
myui = MainWindowEx()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()