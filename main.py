#////////////////////////////////////////////
#
# BY: RONALDO DE OLIVEIRA FRAGA
# PROJETO FEITO UTILIZANDO: Qt Designer and PySide6
#
#////////////////////////////////////////////

#IMPORTANDO MODULOS
import sys
import os

#IMPORTANDO QTCORE
from qt_core import *

#IMPORTAR JANELA INICIAL
from gui.windows.main_window.ui_main_window import *

#MENU PRINCIPAL

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #TITULO DA JANELA PRINCIPAL
        self.setWindowTitle("Curso PySide")

        #SETUP JANELA INICIAL
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self) 
        
        #TOGGLE BUTTON
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        #HOME BUTTON
        self.ui.bt1.clicked.connect(self.show_page_1)

        #WIDGET BUTTON
        self.ui.bt2.clicked.connect(self.show_page_2)

        #SETTINGS BUTTON
        self.ui.settings_btn.clicked.connect(self.show_page_3)

        #CHANGE TEXT
        self.ui.ui_pages.btn_change_text.clicked.connect(self.change_text)
        #EXIBE A JANELA DA APLICAÇÂO
        self.show()

    def change_text(self):
        text = self.ui.ui_pages.lineEdit.text()
        new_text = "Olá, " + text
        self.ui.ui_pages.label.setText(new_text)

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.bt1.set_active(True)

    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.bt2.set_active(True)

    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.settings_btn.set_active(True)

    def toggle_button(self):
        #GET MENU WIDTH
        menu_width = self.ui.left_menu.width()

        #CHECK WIDTH
        width = 50
        if menu_width == 50:
            width = 240
        #START ANIMATION
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start() 
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())