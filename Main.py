import sys
from View.Principal import *
from PySide6.QtWidgets import QApplication, QMainWindow



class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)


        ####Pagina Inicial###

        self.ui.pages.setCurrentWidget(self.ui.page_ramal)


        ####Botões###
        self.ui.btn_chamados.clicked.connect(self.chamados)
        self.ui.btn_ramais.clicked.connect(self.ramal)


        ###paginas###
    def chamados(self):
        self.ui.pages.setCurrentWidget(self.ui.Page_chamados)

    def ramal(self):
        self.ui.pages.setCurrentWidget(self.ui.page_ramal)    


if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = TelaPrincipal()
    window.show()
    sys.exit(app.exec())