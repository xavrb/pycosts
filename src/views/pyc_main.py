import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QSplashScreen
from PyQt5.QtGui import QPixmap
from pycosts import Ui_MainWindow
import time


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        
def main():
    app = QApplication(sys.argv)


    splash_pix = QPixmap("./assets/splash_loading.png")
    splash = QSplashScreen(splash_pix)
    splash.show()
    app.processEvents()

    # Simulate something that takes time
    time.sleep(2)
    splash.hide()
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
