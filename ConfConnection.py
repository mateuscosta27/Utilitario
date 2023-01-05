import sys
from configs.config import *
from View.StringConnection import *

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog




class ConfConnection(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_StringConnection()
        self.ui.setupUi(self)

        self.config = Conf()

        self.ui.btn_localDB.clicked.connect(self.localdb)

        self.ui.lb_commom.setText(f'Todos os direitos reservados | {self.config.} | {self.config.data}')


    def localdb(self):
        self.config.select_local_db()
        self.ui.le_localDb.setText(self.config.directory)
        check_btn = self.ui.le_localDb.text()
        if check_btn!='':
            self.ui.btn_localDB.setVisible(False)
            self.ui.btn_testConnection.setGeometry(520,80,150,45)
        self.ui.btn_testConnection.clicked.connect(self.config.create_directory_db)
        self.ui.btn_testConnection.clicked.connect(self.test_connection_status)
        self.ui.le_localDb.setDisabled(True)
        

    def test_connection_status(self):

        try:
            icon_Connect = QIcon()
            icon_Connect.addFile(u"./src/icon_connectDB.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.btn_statusConection.setIcon(icon_Connect)
            icon_check = QIcon()
            icon_check.addFile(u"./src/icon_check.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.btn_testConnection.setIcon(icon_check)
            self.ui.btn_testConnection.setText("Conectado")
        except sqlite3.Error as e:
            icon_diconnect = QIcon()
            icon_diconnect.addFile(u"./src/icon_disconnectDB.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.btn_statusConection.setIcon(icon_diconnect)
            icon_uncheck = QIcon()
            icon_uncheck.addFile(u"./src/icon_uncheck.svg", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.btn_testConnection.setIcon(icon_check)


       







  














if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = ConfConnection()
    window.show()
    sys.exit(app.exec())