"""
Start the application
"""
import sys

from PyQt6 import QtWidgets

from service.ui_service import Interface

app = QtWidgets.QApplication([])
application = Interface()
application.show()

sys.exit(app.exec())
