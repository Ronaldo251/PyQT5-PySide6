# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesVVxEPl.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *
class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(1084, 803)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        application_pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        application_pages.addWidget(self.page_3)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.horizontalLayout = QHBoxLayout(self.page_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.paginainicial = QFrame(self.page_1)
        self.paginainicial.setObjectName(u"paginainicial")
        self.paginainicial.setMinimumSize(QSize(500, 70))
        self.paginainicial.setMaximumSize(QSize(500, 70))
        self.paginainicial.setFrameShape(QFrame.StyledPanel)
        self.paginainicial.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.paginainicial)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.paginainicial)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.paginainicial)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 36))
        self.lineEdit.setMaximumSize(QSize(16777215, 36))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(68, 71, 90);\n"
"	padding: 8px;\n"
"	border: 2px solid #c3ccdf;	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.btn_change_text = QPushButton(self.paginainicial)
        self.btn_change_text.setObjectName(u"btn_change_text")
        self.btn_change_text.setMinimumSize(QSize(120, 36))
        self.btn_change_text.setMaximumSize(QSize(16777215, 36))
        self.btn_change_text.setStyleSheet(u"QPushButton{\n"
" 	background-color: #44475a;\n"
"	border: 2px solid #c3ccdf;	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 127);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(85, 255, 0);\n"
"}")

        self.gridLayout.addWidget(self.btn_change_text, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.horizontalLayout.addWidget(self.paginainicial)

        application_pages.addWidget(self.page_1)

        self.retranslateUi(application_pages)

        application_pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.label_2.setText(QCoreApplication.translate("application_pages", u"Widgets", None))
        self.label_3.setText(QCoreApplication.translate("application_pages", u"Configura\u00e7\u00f5es", None))
        self.label.setText(QCoreApplication.translate("application_pages", u"Ol\u00e1, digite seu nome", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("application_pages", u"Digite aqui seu texto...", None))
        self.btn_change_text.setText(QCoreApplication.translate("application_pages", u"Alterar Texto", None))
    # retranslateUi

