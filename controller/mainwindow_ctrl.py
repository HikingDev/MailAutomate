from PySide2 import QtWidgets, QtCore


class MainController(QtCore.QObject):
    VERSION = "v1.6.0"

    def __init__(self, model, view, parent=None):
        self._model = model
        self._view = view

