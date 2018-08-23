from PySide2 import QtWidgets

from .ui.MailAutomateView import Ui_MainWindow


class MainView(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        self.build_ui()

    def build_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

