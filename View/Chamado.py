# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Chamado.ui'
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
    QTextEdit, QVBoxLayout, QWidget)

class Ui_TelaChamado(object):
    def setupUi(self, TelaChamado):
        if not TelaChamado.objectName():
            TelaChamado.setObjectName(u"TelaChamado")
        TelaChamado.resize(1275, 455)
        TelaChamado.setMinimumSize(QSize(1275, 455))
        TelaChamado.setMaximumSize(QSize(1275, 560))
        self.centralwidget = QWidget(TelaChamado)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lb_sector = QLabel(self.frame)
        self.lb_sector.setObjectName(u"lb_sector")
        self.lb_sector.setGeometry(QRect(10, 14, 111, 20))
        self.cbb_client = QComboBox(self.frame)
        self.cbb_client.addItem("")
        self.cbb_client.addItem("")
        self.cbb_client.addItem("")
        self.cbb_client.addItem("")
        self.cbb_client.addItem("")
        self.cbb_client.addItem("")
        self.cbb_client.addItem("")
        self.cbb_client.addItem("")
        self.cbb_client.addItem("")
        self.cbb_client.setObjectName(u"cbb_client")
        self.cbb_client.setGeometry(QRect(10, 40, 341, 41))
        self.cbb_client.setMinimumSize(QSize(0, 41))
        self.cbb_client.setMaximumSize(QSize(16777215, 41))
        self.cbb_client.setSizeIncrement(QSize(0, 0))
        self.cbb_client.setAutoFillBackground(False)
        self.cbb_client.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.cbb_client.setDuplicatesEnabled(False)
        self.cbb_client.setModelColumn(0)
        self.lb_solution = QLabel(self.frame)
        self.lb_solution.setObjectName(u"lb_solution")
        self.lb_solution.setGeometry(QRect(30, 210, 101, 55))
        self.txt_solution = QTextEdit(self.frame)
        self.txt_solution.setObjectName(u"txt_solution")
        self.txt_solution.setGeometry(QRect(130, 210, 1121, 201))
        self.le_client = QLineEdit(self.frame)
        self.le_client.setObjectName(u"le_client")
        self.le_client.setGeometry(QRect(370, 40, 200, 41))
        self.le_client.setMinimumSize(QSize(0, 41))
        self.le_client.setMaximumSize(QSize(16777215, 41))
        self.le_client.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.lb_client = QLabel(self.frame)
        self.lb_client.setObjectName(u"lb_client")
        self.lb_client.setGeometry(QRect(370, 14, 81, 21))
        self.lb_star_customer = QLabel(self.frame)
        self.lb_star_customer.setObjectName(u"lb_star_customer")
        self.lb_star_customer.setGeometry(QRect(590, 14, 201, 21))
        self.le_start_customer = QLineEdit(self.frame)
        self.le_start_customer.setObjectName(u"le_start_customer")
        self.le_start_customer.setGeometry(QRect(590, 40, 200, 41))
        self.le_start_customer.setMinimumSize(QSize(0, 41))
        self.le_start_customer.setMaximumSize(QSize(16777215, 41))
        self.le_start_customer.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.lb_problem = QLabel(self.frame)
        self.lb_problem.setObjectName(u"lb_problem")
        self.lb_problem.setGeometry(QRect(20, 130, 101, 55))
        self.txt_problem = QTextEdit(self.frame)
        self.txt_problem.setObjectName(u"txt_problem")
        self.txt_problem.setGeometry(QRect(130, 130, 1121, 51))
        self.le_end_customer = QLineEdit(self.frame)
        self.le_end_customer.setObjectName(u"le_end_customer")
        self.le_end_customer.setGeometry(QRect(13, 460, 161, 41))
        self.le_end_customer.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.lb_end_customer = QLabel(self.frame)
        self.lb_end_customer.setObjectName(u"lb_end_customer")
        self.lb_end_customer.setGeometry(QRect(13, 430, 141, 31))
        self.lb_time_customer = QLabel(self.frame)
        self.lb_time_customer.setObjectName(u"lb_time_customer")
        self.lb_time_customer.setGeometry(QRect(210, 430, 161, 31))
        self.le_time_customer = QLineEdit(self.frame)
        self.le_time_customer.setObjectName(u"le_time_customer")
        self.le_time_customer.setGeometry(QRect(210, 460, 161, 41))
        self.le_time_customer.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.cbb_level = QComboBox(self.frame)
        self.cbb_level.addItem("")
        self.cbb_level.addItem("")
        self.cbb_level.addItem("")
        self.cbb_level.addItem("")
        self.cbb_level.addItem("")
        self.cbb_level.addItem("")
        self.cbb_level.addItem("")
        self.cbb_level.addItem("")
        self.cbb_level.addItem("")
        self.cbb_level.setObjectName(u"cbb_level")
        self.cbb_level.setGeometry(QRect(420, 460, 401, 41))
        self.cbb_level.setMinimumSize(QSize(0, 41))
        self.cbb_level.setMaximumSize(QSize(16777215, 41))
        self.cbb_level.setSizeIncrement(QSize(0, 0))
        self.cbb_level.setAutoFillBackground(False)
        self.cbb_level.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.cbb_level.setDuplicatesEnabled(False)
        self.cbb_level.setModelColumn(0)
        self.lb_level = QLabel(self.frame)
        self.lb_level.setObjectName(u"lb_level")
        self.lb_level.setGeometry(QRect(420, 430, 211, 21))
        self.btn_end = QPushButton(self.frame)
        self.btn_end.setObjectName(u"btn_end")
        self.btn_end.setGeometry(QRect(1140, 30, 100, 45))
        self.btn_end.setMinimumSize(QSize(100, 45))
        self.btn_end.setMaximumSize(QSize(100, 45))
        self.btn_end.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.btn_end.setFont(font)
        self.btn_end.setStyleSheet(u"QPushButton{\n"
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
        self.btn_end.setInputMethodHints(Qt.ImhNone)
        icon = QIcon()
        icon.addFile(u"../src/icon_remove.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_end.setIcon(icon)
        self.btn_end.setIconSize(QSize(20, 20))
        self.btn_save = QPushButton(self.frame)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(870, 450, 100, 45))
        self.btn_save.setMinimumSize(QSize(100, 45))
        self.btn_save.setMaximumSize(QSize(100, 45))
        self.btn_save.setBaseSize(QSize(0, 0))
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet(u"QPushButton{\n"
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
        self.btn_save.setInputMethodHints(Qt.ImhNone)
        icon1 = QIcon()
        icon1.addFile(u"../src/icon_add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon1)
        self.btn_save.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.frame)

        self.frame_footer = QFrame(self.centralwidget)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setMinimumSize(QSize(0, 35))
        self.frame_footer.setMaximumSize(QSize(16777215, 35))
        self.frame_footer.setStyleSheet(u"background-color: #0954B2;\n"
"border-radius: 2px;\n"
"")
        self.frame_footer.setFrameShape(QFrame.StyledPanel)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_footer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_commom = QLabel(self.frame_footer)
        self.lb_commom.setObjectName(u"lb_commom")
        self.lb_commom.setMinimumSize(QSize(0, 35))
        self.lb_commom.setMaximumSize(QSize(16777215, 35))
        self.lb_commom.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: #fff;\n"
"")
        self.lb_commom.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_commom)


        self.verticalLayout.addWidget(self.frame_footer)

        TelaChamado.setCentralWidget(self.centralwidget)

        self.retranslateUi(TelaChamado)

        QMetaObject.connectSlotsByName(TelaChamado)
    # setupUi

    def retranslateUi(self, TelaChamado):
        TelaChamado.setWindowTitle(QCoreApplication.translate("TelaChamado", u"MainWindow", None))
        self.lb_sector.setText(QCoreApplication.translate("TelaChamado", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Municipio:</span></p></body></html>", None))
        self.cbb_client.setItemText(0, "")
        self.cbb_client.setItemText(1, QCoreApplication.translate("TelaChamado", u"FLOWDOCS", None))
        self.cbb_client.setItemText(2, QCoreApplication.translate("TelaChamado", u"FOLHA", None))
        self.cbb_client.setItemText(3, QCoreApplication.translate("TelaChamado", u"GERENTE", None))
        self.cbb_client.setItemText(4, QCoreApplication.translate("TelaChamado", u"RECEP\u00c7\u00c3O", None))
        self.cbb_client.setItemText(5, QCoreApplication.translate("TelaChamado", u"SERVICE DESK", None))
        self.cbb_client.setItemText(6, QCoreApplication.translate("TelaChamado", u"SIS-SIE-SAS", None))
        self.cbb_client.setItemText(7, QCoreApplication.translate("TelaChamado", u"SSE-SED-PORTAL-PATRIMONIO", None))
        self.cbb_client.setItemText(8, QCoreApplication.translate("TelaChamado", u"TRIBUT\u00c1RIO", None))

        self.cbb_client.setPlaceholderText(QCoreApplication.translate("TelaChamado", u"Todos", None))
        self.lb_solution.setText(QCoreApplication.translate("TelaChamado", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Solu\u00e7\u00e3o:</span></p></body></html>", None))
        self.le_client.setPlaceholderText("")
        self.lb_client.setText(QCoreApplication.translate("TelaChamado", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Cliente:</span></p></body></html>", None))
        self.lb_star_customer.setText(QCoreApplication.translate("TelaChamado", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Inicio Atendimento</span></p></body></html>", None))
        self.le_start_customer.setPlaceholderText("")
        self.lb_problem.setText(QCoreApplication.translate("TelaChamado", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Problema</span></p></body></html>", None))
        self.le_end_customer.setPlaceholderText("")
        self.lb_end_customer.setText(QCoreApplication.translate("TelaChamado", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Fim Atendimento</span></p></body></html>", None))
        self.lb_time_customer.setText(QCoreApplication.translate("TelaChamado", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Tempo Atendimento</span></p></body></html>", None))
        self.le_time_customer.setPlaceholderText("")
        self.cbb_level.setItemText(0, "")
        self.cbb_level.setItemText(1, QCoreApplication.translate("TelaChamado", u"FLOWDOCS", None))
        self.cbb_level.setItemText(2, QCoreApplication.translate("TelaChamado", u"FOLHA", None))
        self.cbb_level.setItemText(3, QCoreApplication.translate("TelaChamado", u"GERENTE", None))
        self.cbb_level.setItemText(4, QCoreApplication.translate("TelaChamado", u"RECEP\u00c7\u00c3O", None))
        self.cbb_level.setItemText(5, QCoreApplication.translate("TelaChamado", u"SERVICE DESK", None))
        self.cbb_level.setItemText(6, QCoreApplication.translate("TelaChamado", u"SIS-SIE-SAS", None))
        self.cbb_level.setItemText(7, QCoreApplication.translate("TelaChamado", u"SSE-SED-PORTAL-PATRIMONIO", None))
        self.cbb_level.setItemText(8, QCoreApplication.translate("TelaChamado", u"TRIBUT\u00c1RIO", None))

        self.cbb_level.setPlaceholderText(QCoreApplication.translate("TelaChamado", u"Todos", None))
        self.lb_level.setText(QCoreApplication.translate("TelaChamado", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Nivel de dificuldade</span></p></body></html>", None))
        self.btn_end.setText(QCoreApplication.translate("TelaChamado", u"Finalizar", None))
        self.btn_save.setText(QCoreApplication.translate("TelaChamado", u"Salvar", None))
        self.lb_commom.setText(QCoreApplication.translate("TelaChamado", u"Utilitario de servi\u00e7os - vers\u00e3o 0.0.1", None))
    # retranslateUi

