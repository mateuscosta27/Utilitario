# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_TelaCadastro(object):
    def setupUi(self, TelaCadastro):
        if not TelaCadastro.objectName():
            TelaCadastro.setObjectName(u"TelaCadastro")
        TelaCadastro.resize(1050, 450)
        TelaCadastro.setMinimumSize(QSize(1050, 450))
        TelaCadastro.setMaximumSize(QSize(1050, 450))
        self.centralwidget = QWidget(TelaCadastro)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1050, 450))
        self.centralwidget.setMaximumSize(QSize(1050, 450))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.cbb_sector = QComboBox(self.frame)
        self.cbb_sector.addItem("")
        self.cbb_sector.addItem("")
        self.cbb_sector.addItem("")
        self.cbb_sector.addItem("")
        self.cbb_sector.addItem("")
        self.cbb_sector.addItem("")
        self.cbb_sector.addItem("")
        self.cbb_sector.addItem("")
        self.cbb_sector.addItem("")
        self.cbb_sector.setObjectName(u"cbb_sector")
        self.cbb_sector.setGeometry(QRect(540, 80, 341, 55))
        self.cbb_sector.setMinimumSize(QSize(0, 55))
        self.cbb_sector.setMaximumSize(QSize(16777215, 55))
        self.cbb_sector.setSizeIncrement(QSize(0, 0))
        self.cbb_sector.setAutoFillBackground(False)
        self.cbb_sector.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.cbb_sector.setDuplicatesEnabled(False)
        self.cbb_sector.setModelColumn(0)
        self.btn_add = QPushButton(self.frame)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(370, 350, 100, 45))
        self.btn_add.setMinimumSize(QSize(100, 45))
        self.btn_add.setMaximumSize(QSize(100, 45))
        self.btn_add.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: insetset;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_add.setInputMethodHints(Qt.ImhNone)
        icon = QIcon()
        icon.addFile(u"./src/icon_add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add.setIcon(icon)
        self.btn_add.setIconSize(QSize(20, 20))
        self.lb_name = QLabel(self.frame)
        self.lb_name.setObjectName(u"lb_name")
        self.lb_name.setGeometry(QRect(96, 84, 71, 41))
        self.le_name = QLineEdit(self.frame)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setGeometry(QRect(170, 77, 200, 55))
        self.le_name.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.lb_sector = QLabel(self.frame)
        self.lb_sector.setObjectName(u"lb_sector")
        self.lb_sector.setGeometry(QRect(476, 84, 71, 41))
        self.le_branchIn = QLineEdit(self.frame)
        self.le_branchIn.setObjectName(u"le_branchIn")
        self.le_branchIn.setGeometry(QRect(170, 180, 200, 55))
        self.le_branchIn.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.lb_branchIn = QLabel(self.frame)
        self.lb_branchIn.setObjectName(u"lb_branchIn")
        self.lb_branchIn.setGeometry(QRect(16, 185, 151, 41))
        self.lb_branchEx = QLabel(self.frame)
        self.lb_branchEx.setObjectName(u"lb_branchEx")
        self.lb_branchEx.setGeometry(QRect(386, 185, 151, 41))
        self.le_branchEx = QLineEdit(self.frame)
        self.le_branchEx.setObjectName(u"le_branchEx")
        self.le_branchEx.setGeometry(QRect(540, 180, 200, 55))
        self.le_branchEx.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.lb_cellPhone = QLabel(self.frame)
        self.lb_cellPhone.setObjectName(u"lb_cellPhone")
        self.lb_cellPhone.setGeometry(QRect(751, 185, 80, 41))
        self.le_cellPhone = QLineEdit(self.frame)
        self.le_cellPhone.setObjectName(u"le_cellPhone")
        self.le_cellPhone.setGeometry(QRect(836, 180, 200, 55))
        self.le_cellPhone.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.btn_update = QPushButton(self.frame)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setGeometry(QRect(480, 350, 100, 45))
        self.btn_update.setMinimumSize(QSize(100, 45))
        self.btn_update.setMaximumSize(QSize(100, 45))
        self.btn_update.setBaseSize(QSize(0, 0))
        self.btn_update.setFont(font)
        self.btn_update.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: insetset;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_update.setInputMethodHints(Qt.ImhNone)
        icon1 = QIcon()
        icon1.addFile(u"./src/icon_edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update.setIcon(icon1)
        self.btn_update.setIconSize(QSize(20, 20))
        self.btn_remove = QPushButton(self.frame)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setGeometry(QRect(590, 350, 100, 45))
        self.btn_remove.setMinimumSize(QSize(100, 45))
        self.btn_remove.setMaximumSize(QSize(100, 45))
        self.btn_remove.setBaseSize(QSize(0, 0))
        self.btn_remove.setFont(font)
        self.btn_remove.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #F2163E;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #BF0404;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: insetset;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_remove.setInputMethodHints(Qt.ImhNone)
        icon2 = QIcon()
        icon2.addFile(u"./src/icon_remove.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove.setIcon(icon2)
        self.btn_remove.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.frame)

        self.fram_footer = QFrame(self.centralwidget)
        self.fram_footer.setObjectName(u"fram_footer")
        self.fram_footer.setMinimumSize(QSize(0, 35))
        self.fram_footer.setMaximumSize(QSize(16777215, 35))
        self.fram_footer.setStyleSheet(u"background-color: #0954B2;\n"
"border-radius: 2px;\n"
"")
        self.fram_footer.setFrameShape(QFrame.StyledPanel)
        self.fram_footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fram_footer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_commom = QLabel(self.fram_footer)
        self.lb_commom.setObjectName(u"lb_commom")
        self.lb_commom.setMinimumSize(QSize(0, 35))
        self.lb_commom.setMaximumSize(QSize(16777215, 35))
        self.lb_commom.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: #fff;\n"
"")
        self.lb_commom.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_commom)


        self.verticalLayout.addWidget(self.fram_footer)

        TelaCadastro.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaCadastro)

        QMetaObject.connectSlotsByName(TelaCadastro)
    # setupUi

    def retranslateUi(self, TelaCadastro):
        TelaCadastro.setWindowTitle(QCoreApplication.translate("TelaCadastro", u"Cadastro", None))
        self.cbb_sector.setItemText(0, "")
        self.cbb_sector.setItemText(1, QCoreApplication.translate("TelaCadastro", u"FLOWDOCS", None))
        self.cbb_sector.setItemText(2, QCoreApplication.translate("TelaCadastro", u"FOLHA", None))
        self.cbb_sector.setItemText(3, QCoreApplication.translate("TelaCadastro", u"GERENTE", None))
        self.cbb_sector.setItemText(4, QCoreApplication.translate("TelaCadastro", u"RECEP\u00c7\u00c3O", None))
        self.cbb_sector.setItemText(5, QCoreApplication.translate("TelaCadastro", u"SERVICE DESK", None))
        self.cbb_sector.setItemText(6, QCoreApplication.translate("TelaCadastro", u"SIS-SIE-SAS", None))
        self.cbb_sector.setItemText(7, QCoreApplication.translate("TelaCadastro", u"SSE-SED-PORTAL-PATRIMONIO", None))
        self.cbb_sector.setItemText(8, QCoreApplication.translate("TelaCadastro", u"TRIBUT\u00c1RIO", None))

        self.cbb_sector.setPlaceholderText(QCoreApplication.translate("TelaCadastro", u"Todos", None))
        self.btn_add.setText(QCoreApplication.translate("TelaCadastro", u"Adicionar", None))
        self.lb_name.setText(QCoreApplication.translate("TelaCadastro", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Nome:</span></p></body></html>", None))
        self.le_name.setPlaceholderText("")
        self.lb_sector.setText(QCoreApplication.translate("TelaCadastro", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Setor:</span></p></body></html>", None))
        self.le_branchIn.setInputMask("")
        self.le_branchIn.setPlaceholderText(QCoreApplication.translate("TelaCadastro", u"Somente numeros", None))
        self.lb_branchIn.setText(QCoreApplication.translate("TelaCadastro", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Ramal Interno:</span></p></body></html>", None))
        self.lb_branchEx.setText(QCoreApplication.translate("TelaCadastro", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Ramal Externo:</span></p></body></html>", None))
        self.le_branchEx.setInputMask("")
        self.le_branchEx.setPlaceholderText(QCoreApplication.translate("TelaCadastro", u"Somente numeros", None))
        self.lb_cellPhone.setText(QCoreApplication.translate("TelaCadastro", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Celular:</span></p></body></html>", None))
        self.le_cellPhone.setInputMask(QCoreApplication.translate("TelaCadastro", u"(##)# ####-####", None))
        self.le_cellPhone.setPlaceholderText(QCoreApplication.translate("TelaCadastro", u"Somente numeros", None))
        self.btn_update.setText(QCoreApplication.translate("TelaCadastro", u"Atualizar", None))
        self.btn_remove.setText(QCoreApplication.translate("TelaCadastro", u"Remover", None))
        self.lb_commom.setText(QCoreApplication.translate("TelaCadastro", u"Utilitario de servi\u00e7os - vers\u00e3o 0.0.1", None))
    # retranslateUi

