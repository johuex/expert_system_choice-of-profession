"""
Start the application
"""
import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import QThread

from service.ui import Interface
thread = QThread()
app = QtWidgets.QApplication([])
application = Interface()
application.show()
sys.exit(app.exec())

# TODO refactor UI
# TODO check conditional_probabilities
# TODO finish end_loop