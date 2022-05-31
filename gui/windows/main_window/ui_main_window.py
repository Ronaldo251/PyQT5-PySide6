#////////////////////////////////////////////
#
# BY: RONALDO DE OLIVEIRA FRAGA
# PROJETO FEITO UTILIZANDO: Qt Designer e PySide6
#
#////////////////////////////////////////////

from qt_core import *

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
        #LABEL ESQUERDA
        self.top_label_left = QLabel("Aplicação PySide6")

        #ESPAÇADOR SUPERIOR
        self.top_spacer = QSpacerItem(20,20,QSizePolicy.Expanding, QSizePolicy.Minimum)

        #LABEL DIREITA
        self.top_label_right = QLabel("| Página Inicial")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        #ADICIONAR AO LAYOUT
        self.top_label_layout.addWidget(self.top_label_left)
        self.top_label_layout.addItem(self.top_spacer)
        self.top_label_layout.addWidget(self.top_label_right)

        #PAGINAS DO APP
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2;") 

        #BARRA INFERIOR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")

        self.bottom_label_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_label_layout.setContentsMargins(10,0,10,0)
        #LABEL ESQUERDA
        self.bottom_label_left = QLabel("Aplicação PySide6 baio esq")

        #ESPAÇADOR SUPERIOR
        self.bottom_spacer = QSpacerItem(20,20,QSizePolicy.Expanding, QSizePolicy.Minimum)

        #LABEL DIREITA
        self.bottom_label_right = QLabel("@2021")
        self.bottom_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

        #ADICIONAR AO LAYOUT
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