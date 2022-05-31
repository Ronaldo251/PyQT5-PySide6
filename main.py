#////////////////////////////////////////////
#
#BY: RONALDO DE OLIVEIRA FRAGA
#PROJETO FEITO UTILIZANDO: Qt Designer and PySide6
#
#////////////////////////////////////////////

#IMPORT MODULES
import sys
import os

#IMPORT QTCORE
from qt_core import *

#IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import *

#MAIN MENU

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self) 



        #EXIBE A JANELA DA APLICAÇÂO
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())