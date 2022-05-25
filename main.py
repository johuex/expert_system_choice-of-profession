"""Start the application"""
import sys

from PyQt6 import QtWidgets

from service.ui import Interface


app = QtWidgets.QApplication([])
application = Interface()
application.show()
sys.exit(app.exec())
