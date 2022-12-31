# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Principal.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.setWindowModality(Qt.ApplicationModal)
        Main.resize(1356, 686)
        Main.setIconSize(QSize(70, 70))
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_10 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 60))
        self.frame_top.setMaximumSize(QSize(16777215, 60))
        self.frame_top.setStyleSheet(u"background-color: #0954B2;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_btn_menu = QFrame(self.frame_top)
        self.frame_btn_menu.setObjectName(u"frame_btn_menu")
        self.frame_btn_menu.setMinimumSize(QSize(185, 60))
        self.frame_btn_menu.setMaximumSize(QSize(185, 60))
        self.frame_btn_menu.setStyleSheet(u"background-color:#0954B2;")
        self.frame_btn_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_btn_menu)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QPushButton(self.frame_btn_menu)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(75, 60))
        self.btn_menu.setMaximumSize(QSize(180, 60))
        self.btn_menu.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 15px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 5px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:#0954B2;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        icon = QIcon()
        icon.addFile(u"../src/icon_menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.btn_menu, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_btn_menu)

        self.frame_info = QFrame(self.frame_top)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setMinimumSize(QSize(0, 0))
        self.frame_info.setStyleSheet(u"background-color: rgb(9, 84, 178);")
        self.frame_info.setFrameShape(QFrame.NoFrame)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_info)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.btn_db = QPushButton(self.frame_info)
        self.btn_db.setObjectName(u"btn_db")
        self.btn_db.setMinimumSize(QSize(100, 45))
        self.btn_db.setMaximumSize(QSize(100, 45))
        self.btn_db.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_7.addWidget(self.btn_db, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.frame_info)


        self.verticalLayout_10.addWidget(self.frame_top)

        self.fram_bot = QFrame(self.centralwidget)
        self.fram_bot.setObjectName(u"fram_bot")
        self.fram_bot.setFrameShape(QFrame.NoFrame)
        self.fram_bot.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.fram_bot)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_side = QFrame(self.fram_bot)
        self.frame_side.setObjectName(u"frame_side")
        self.frame_side.setMinimumSize(QSize(230, 0))
        self.frame_side.setMaximumSize(QSize(0, 16777215))
        self.frame_side.setSizeIncrement(QSize(0, 0))
        self.frame_side.setStyleSheet(u"background-color: #FFF;\n"
"border: 2px solid;\n"
"border-left: none;\n"
"border-top: none;\n"
"border-bottom:none;\n"
"border-right-color: #0954B2;")
        self.frame_side.setFrameShape(QFrame.NoFrame)
        self.frame_side.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_side)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 45, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_buttons = QFrame(self.frame_side)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setStyleSheet(u"border:none;")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_buttons)
        self.verticalLayout.setSpacing(35)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 25, 0, 0)
        self.btn_ramais = QPushButton(self.frame_buttons)
        self.btn_ramais.setObjectName(u"btn_ramais")
        self.btn_ramais.setMinimumSize(QSize(200, 45))
        self.btn_ramais.setMaximumSize(QSize(200, 45))
        self.btn_ramais.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.btn_ramais.setFont(font)
        self.btn_ramais.setStyleSheet(u"QPushButton{\n"
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
        self.btn_ramais.setInputMethodHints(Qt.ImhNone)
        icon1 = QIcon()
        icon1.addFile(u"../src/icon_ramal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ramais.setIcon(icon1)
        self.btn_ramais.setIconSize(QSize(35, 35))

        self.verticalLayout.addWidget(self.btn_ramais)

        self.btn_chamados = QPushButton(self.frame_buttons)
        self.btn_chamados.setObjectName(u"btn_chamados")
        self.btn_chamados.setMinimumSize(QSize(200, 45))
        self.btn_chamados.setMaximumSize(QSize(200, 45))
        self.btn_chamados.setStyleSheet(u"QPushButton{\n"
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
        icon2 = QIcon()
        icon2.addFile(u"../src/icon_call.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_chamados.setIcon(icon2)
        self.btn_chamados.setIconSize(QSize(35, 35))

        self.verticalLayout.addWidget(self.btn_chamados)


        self.verticalLayout_2.addWidget(self.frame_buttons)

        self.verticalSpacer_2 = QSpacerItem(20, 383, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame_about = QFrame(self.frame_side)
        self.frame_about.setObjectName(u"frame_about")
        self.frame_about.setMinimumSize(QSize(0, 0))
        self.frame_about.setMaximumSize(QSize(16777215, 16777215))
        self.frame_about.setStyleSheet(u"background-color: rgb(9, 84, 178);")
        self.frame_about.setFrameShape(QFrame.NoFrame)
        self.frame_about.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_about)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 1)
        self.btn_about = QPushButton(self.frame_about)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setMinimumSize(QSize(225, 35))
        self.btn_about.setMaximumSize(QSize(230, 35))
        self.btn_about.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
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
"	background-color: #0954B2;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_about.setIconSize(QSize(25, 25))
        self.btn_about.setAutoDefault(True)
        self.btn_about.setFlat(False)

        self.horizontalLayout_12.addWidget(self.btn_about)


        self.verticalLayout_2.addWidget(self.frame_about)


        self.horizontalLayout.addWidget(self.frame_side)

        self.frame_content = QFrame(self.fram_bot)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setStyleSheet(u"background-color:#0954B2;")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_pages = QFrame(self.frame_content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"background-color: #fff;")
        self.frame_pages.setFrameShape(QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_page = QFrame(self.frame_pages)
        self.frame_page.setObjectName(u"frame_page")
        self.frame_page.setFrameShape(QFrame.StyledPanel)
        self.frame_page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.frame_page)
        self.pages.setObjectName(u"pages")
        self.page_ramal = QWidget()
        self.page_ramal.setObjectName(u"page_ramal")
        self.verticalLayout_7 = QVBoxLayout(self.page_ramal)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.fram_footer_pages = QFrame(self.page_ramal)
        self.fram_footer_pages.setObjectName(u"fram_footer_pages")
        self.fram_footer_pages.setMinimumSize(QSize(0, 100))
        self.fram_footer_pages.setMaximumSize(QSize(16777215, 100))
        self.fram_footer_pages.setFrameShape(QFrame.StyledPanel)
        self.fram_footer_pages.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.fram_footer_pages)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.cbb_select_setor = QComboBox(self.fram_footer_pages)
        self.cbb_select_setor.addItem("")
        self.cbb_select_setor.addItem("")
        self.cbb_select_setor.addItem("")
        self.cbb_select_setor.addItem("")
        self.cbb_select_setor.addItem("")
        self.cbb_select_setor.addItem("")
        self.cbb_select_setor.addItem("")
        self.cbb_select_setor.addItem("")
        self.cbb_select_setor.setObjectName(u"cbb_select_setor")
        self.cbb_select_setor.setMinimumSize(QSize(0, 60))
        self.cbb_select_setor.setMaximumSize(QSize(16777215, 60))
        self.cbb_select_setor.setSizeIncrement(QSize(0, 0))
        self.cbb_select_setor.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.cbb_select_setor, 0, 0, 1, 1)

        self.le_search_name = QLineEdit(self.fram_footer_pages)
        self.le_search_name.setObjectName(u"le_search_name")
        self.le_search_name.setMinimumSize(QSize(250, 60))
        self.le_search_name.setMaximumSize(QSize(16777215, 60))
        self.le_search_name.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.le_search_name, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.fram_footer_pages)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(450, 60))
        self.groupBox.setMaximumSize(QSize(450, 60))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_search = QPushButton(self.groupBox)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(100, 45))
        self.btn_search.setMaximumSize(QSize(100, 45))
        self.btn_search.setBaseSize(QSize(0, 0))
        self.btn_search.setFont(font)
        self.btn_search.setStyleSheet(u"QPushButton{\n"
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
        self.btn_search.setInputMethodHints(Qt.ImhNone)
        icon3 = QIcon()
        icon3.addFile(u"../src/icon_search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon3)
        self.btn_search.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.btn_search, 0, 0, 1, 1)

        self.btn_add = QPushButton(self.groupBox)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(100, 45))
        self.btn_add.setMaximumSize(QSize(100, 45))
        self.btn_add.setBaseSize(QSize(0, 0))
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
        icon4 = QIcon()
        icon4.addFile(u"../src/icon_add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add.setIcon(icon4)
        self.btn_add.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.btn_add, 0, 1, 1, 1)

        self.btn_alter = QPushButton(self.groupBox)
        self.btn_alter.setObjectName(u"btn_alter")
        self.btn_alter.setMinimumSize(QSize(100, 45))
        self.btn_alter.setMaximumSize(QSize(100, 45))
        self.btn_alter.setBaseSize(QSize(0, 0))
        self.btn_alter.setFont(font)
        self.btn_alter.setStyleSheet(u"QPushButton{\n"
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
        self.btn_alter.setInputMethodHints(Qt.ImhNone)
        icon5 = QIcon()
        icon5.addFile(u"../src/icon_edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alter.setIcon(icon5)
        self.btn_alter.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.btn_alter, 0, 2, 1, 1)

        self.btn_delete = QPushButton(self.groupBox)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMinimumSize(QSize(100, 45))
        self.btn_delete.setMaximumSize(QSize(100, 45))
        self.btn_delete.setBaseSize(QSize(0, 0))
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet(u"QPushButton{\n"
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
        self.btn_delete.setInputMethodHints(Qt.ImhNone)
        icon6 = QIcon()
        icon6.addFile(u"../src/icon_remove.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete.setIcon(icon6)
        self.btn_delete.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.btn_delete, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 2, 1, 1)


        self.verticalLayout_7.addWidget(self.fram_footer_pages)

        self.fram_table = QFrame(self.page_ramal)
        self.fram_table.setObjectName(u"fram_table")
        self.fram_table.setContextMenuPolicy(Qt.NoContextMenu)
        self.fram_table.setFrameShape(QFrame.StyledPanel)
        self.fram_table.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fram_table)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(55, 0, 55, 0)
        self.tb_ramal = QTableWidget(self.fram_table)
        if (self.tb_ramal.columnCount() < 6):
            self.tb_ramal.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_ramal.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_ramal.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_ramal.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_ramal.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_ramal.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_ramal.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tb_ramal.setObjectName(u"tb_ramal")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.tb_ramal.setFont(font1)
        self.tb_ramal.setFrameShape(QFrame.Box)
        self.tb_ramal.setFrameShadow(QFrame.Sunken)
        self.tb_ramal.setAutoScrollMargin(20)
        self.tb_ramal.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked)
        self.tb_ramal.setTextElideMode(Qt.ElideMiddle)
        self.tb_ramal.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tb_ramal.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tb_ramal.setShowGrid(True)
        self.tb_ramal.setSortingEnabled(True)
        self.tb_ramal.setCornerButtonEnabled(True)
        self.tb_ramal.horizontalHeader().setMinimumSectionSize(50)
        self.tb_ramal.horizontalHeader().setDefaultSectionSize(250)
        self.tb_ramal.verticalHeader().setVisible(False)

        self.horizontalLayout_3.addWidget(self.tb_ramal)


        self.verticalLayout_7.addWidget(self.fram_table)

        self.pages.addWidget(self.page_ramal)
        self.page_chamados = QWidget()
        self.page_chamados.setObjectName(u"page_chamados")
        self.label_2 = QLabel(self.page_chamados)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 100, 561, 191))
        self.label_2.setStyleSheet(u"font: 700 28pt \"Segoe UI\";")
        self.pages.addWidget(self.page_chamados)

        self.verticalLayout_6.addWidget(self.pages)


        self.verticalLayout_5.addWidget(self.frame_page)


        self.verticalLayout_3.addWidget(self.frame_pages)

        self.frame_footer = QFrame(self.frame_content)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setMinimumSize(QSize(0, 35))
        self.frame_footer.setMaximumSize(QSize(16777215, 35))
        self.frame_footer.setStyleSheet(u"background-color: #0954B2;\n"
"border-radius: 2px;\n"
"")
        self.frame_footer.setFrameShape(QFrame.NoFrame)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_footer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_commom = QLabel(self.frame_footer)
        self.lb_commom.setObjectName(u"lb_commom")
        self.lb_commom.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: #fff;\n"
"")
        self.lb_commom.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lb_commom)


        self.verticalLayout_3.addWidget(self.frame_footer)


        self.horizontalLayout.addWidget(self.frame_content)


        self.verticalLayout_10.addWidget(self.fram_bot)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        self.btn_about.setDefault(False)
        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Modulo Principal", None))
        self.btn_menu.setText("")
#if QT_CONFIG(shortcut)
        self.btn_menu.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.btn_db.setText(QCoreApplication.translate("Main", u"Conex\u00e3o", None))
        self.btn_ramais.setText(QCoreApplication.translate("Main", u"Ramais", None))
        self.btn_chamados.setText(QCoreApplication.translate("Main", u"Chamados", None))
        self.btn_about.setText(QCoreApplication.translate("Main", u"Sobre", None))
        self.cbb_select_setor.setItemText(0, QCoreApplication.translate("Main", u"Flow Docs", None))
        self.cbb_select_setor.setItemText(1, QCoreApplication.translate("Main", u"Folha", None))
        self.cbb_select_setor.setItemText(2, QCoreApplication.translate("Main", u"Gerente", None))
        self.cbb_select_setor.setItemText(3, QCoreApplication.translate("Main", u"Recep\u00e7\u00e3o", None))
        self.cbb_select_setor.setItemText(4, QCoreApplication.translate("Main", u"Service Desk", None))
        self.cbb_select_setor.setItemText(5, QCoreApplication.translate("Main", u"SIS - SIE - SAS", None))
        self.cbb_select_setor.setItemText(6, QCoreApplication.translate("Main", u"SSE - SED - PORTAL - PATRIMONIO", None))
        self.cbb_select_setor.setItemText(7, QCoreApplication.translate("Main", u"Tribut\u00e1rio", None))

        self.le_search_name.setPlaceholderText(QCoreApplication.translate("Main", u"Nome do funcion\u00e1rio", None))
        self.groupBox.setTitle("")
        self.btn_search.setText(QCoreApplication.translate("Main", u"Pesquisar", None))
        self.btn_add.setText(QCoreApplication.translate("Main", u"Adicionar", None))
        self.btn_alter.setText(QCoreApplication.translate("Main", u"Alterar", None))
        self.btn_delete.setText(QCoreApplication.translate("Main", u"Excluir", None))
        ___qtablewidgetitem = self.tb_ramal.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Main", u"Nome", None));
        ___qtablewidgetitem1 = self.tb_ramal.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Main", u"Ramal Interno", None));
        ___qtablewidgetitem2 = self.tb_ramal.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Main", u"Ramal Externo", None));
        ___qtablewidgetitem3 = self.tb_ramal.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Main", u"Celular", None));
        ___qtablewidgetitem4 = self.tb_ramal.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Main", u"Status", None));
        ___qtablewidgetitem5 = self.tb_ramal.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Main", u"A\u00e7\u00e3o", None));
        self.label_2.setText(QCoreApplication.translate("Main", u"Pagina Ramal", None))
        self.lb_commom.setText(QCoreApplication.translate("Main", u"Utilitario de servi\u00e7os - vers\u00e3o 0.0.1", None))
    # retranslateUi

