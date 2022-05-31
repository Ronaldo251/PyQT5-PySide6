#////////////////////////////////////////////
#
# BY: RONALDO DE OLIVEIRA FRAGA
# PROJETO FEITO UTILIZANDO: Qt Designer e PySide6
#
#////////////////////////////////////////////

from qt_core import *

#IMPORT PAGES
from gui.pages.ui_pages import Ui_application_pages

#JANELA PRINCIPAL
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
        
        #PARAMETROS DO TAMANHO DA JANELA
        parent.resize(1200,720)
        parent.setMinimumSize(960,540)

        #WIDGET CENTRAL
        self.central_frame = QFrame()
        #self.central_frame.setStyleSheet("background-color: #282a36")

        #CREATE MAIN LAYOUT(MENU)
        self.main_layout = QHBoxLayout(self.central_frame)  #Caso queira o layout na vertical basta trocar QHBoxLayout por QVBoxLayout e trocar o setMaximumWidth
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        #MENU LATERAL ESQUERDA
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)  #Caso escolha layout vertical trocar setMaximumWidth por setMaximumHeight e mudar QHBoxLayout por QVBoxLayout
        self.left_menu.setMinimumWidth(50)  

        #LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)

        #TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        self.left_menu_top_frame.setStyleSheet(" #left_menu_top_frame {background-color: red;}")


        #TOP FRAME LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)

        #TOP BUTTONS
        self.togle_button = QPushButton("Toggle")
        self.bt1 = QPushButton("1")
        self.bt2 = QPushButton("2")

        #ADD BUTTON TO LAYOUT
        self.left_menu_top_layout.addWidget(self.togle_button)
        self.left_menu_top_layout.addWidget(self.bt1)
        self.left_menu_top_layout.addWidget(self.bt2)

        #MENU SPACER
        self.left_menu_spacer = QSpacerItem(20,20,QSizePolicy.Minimum, QSizePolicy.Expanding)

        #BOTTOM FRAME MENU
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        self.left_menu_bottom_frame.setStyleSheet("#left_menu_bottom_frame {background-color: red; }")

        
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0,0,0,0)
        self.left_menu_bottom_layout.setSpacing(0)

        

        #BOTTOM BUTTONS
        self.settings_btn = QPushButton("Settings")

        #ADD BUTTON TO LAYOUT
        self.left_menu_bottom_layout.addWidget(self.settings_btn)

        #LABEL VERSION
        self.left_menu_label_version = QLabel("v1.0.0")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet("color: #c3ccdf")

        #ADD LABEL VERSION TO LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)

        #CONTEÚDO
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        #CONTEUDO DO LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        #BARRA SUPERIOR
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_label_layout = QHBoxLayout(self.top_bar)
        self.top_label_layout.setContentsMargins(10,0,10,0)

        #LABEL ESQUERDA SUPERIOR
        self.top_label_left = QLabel("Aplicação PySide6")

        #ESPAÇADOR SUPERIOR
        self.top_spacer = QSpacerItem(20,20,QSizePolicy.Expanding, QSizePolicy.Minimum)

        #LABEL DIREITA SUPERIOR
        self.top_label_right = QLabel("| Página Inicial")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        #ADICIONAR AO LAYOUT SUPERIOR
        self.top_label_layout.addWidget(self.top_label_left)
        self.top_label_layout.addItem(self.top_spacer)
        self.top_label_layout.addWidget(self.top_label_right)

        #PAGINAS DO APP
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2;") 
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_3)
        #BARRA INFERIOR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")

        self.bottom_label_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_label_layout.setContentsMargins(10,0,10,0)

        #LABEL ESQUERDA INFERIOR
        self.bottom_label_left = QLabel("Aplicação PySide6 Feita Por: Ronaldo Fraga")

        #ESPAÇADOR INFERIOR
        self.bottom_spacer = QSpacerItem(20,20,QSizePolicy.Expanding, QSizePolicy.Minimum)

        #LABEL DIREITA INFERIOR
        self.bottom_label_right = QLabel("@2021")
        self.bottom_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        #ADICIONAR AO LAYOUT INFERIOR
        self.bottom_label_layout.addWidget(self.bottom_label_left)
        self.bottom_label_layout.addItem(self.bottom_spacer)
        self.bottom_label_layout.addWidget(self.bottom_label_right)

        #ADICIONAR AO CONTEUDO DO LAYOUT
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        #ADD WIDGETS NO APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        #WIDGET CENTRAL
        parent.setCentralWidget(self.central_frame)