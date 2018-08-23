import sys
import logging

from PySide2 import QtCore, QtWidgets

from view.main_view import MainView
from controller.mainwindow_ctrl import MainController


# Global settings for logging module
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s %(message)s',
    datefmt='%H:%M:%S')
logging.addLevelName(logging.DEBUG, '[D]')
logging.addLevelName(logging.INFO, '[I]')
logging.addLevelName(logging.WARNING, '[W]')
logging.addLevelName(logging.ERROR, '[E]')


class App(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        # Set Application Default Settings
        QtCore.QCoreApplication.setOrganizationName("DreamingKeldi")
        QtCore.QCoreApplication.setApplicationName("MailAutomate")

        self.main_view = MainView()
        self.main_view.show()
        self.main_ctrl = MainController(None, self.main_view)

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
