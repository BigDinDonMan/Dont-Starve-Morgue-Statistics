from sys import argv, exit

from PyQt5.QtWidgets import *

from ApplicationGlobals import ApplicationGlobals
from MainWindow import MainWindow
from Morgue import Morgue

def appInit() -> None:
    ApplicationGlobals.getInstance()
    Morgue.getInstance()

def main() -> None:
    appInit()
    app = QApplication(argv)
    window = MainWindow("Don't Starve Morgue")
    window.show()
    exit(app.exec_())

if __name__ == '__main__':
    main()