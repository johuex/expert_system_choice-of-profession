"""
Start the application
"""
import sys

from PyQt6 import QtWidgets

from service.ui_service import Interface

app = QtWidgets.QApplication([])
application = Interface()
application.show()
app.processEvents()
application.update()
sys.exit(app.exec())
