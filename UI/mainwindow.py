# Form implementation generated from reading ui file '.\UI\mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.questionTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.questionTextLabel.setGeometry(QtCore.QRect(10, 490, 721, 31))
        self.questionTextLabel.setObjectName("questionTextLabel")
        self.answerText = QtWidgets.QLabel(self.centralwidget)
        self.answerText.setGeometry(QtCore.QRect(250, 640, 111, 20))
        self.answerText.setObjectName("answerText")
        self.yesPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.yesPushButton.setGeometry(QtCore.QRect(10, 570, 75, 23))
        self.yesPushButton.setObjectName("yesPushButton")
        self.noPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.noPushButton.setGeometry(QtCore.QRect(120, 570, 75, 23))
        self.noPushButton.setObjectName("noPushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 420, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 390, 1041, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.questionsDoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.questionsDoneLabel.setGeometry(QtCore.QRect(140, 420, 47, 13))
        self.questionsDoneLabel.setText("")
        self.questionsDoneLabel.setObjectName("questionsDoneLabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 440, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.questionsLeft = QtWidgets.QLabel(self.centralwidget)
        self.questionsLeft.setGeometry(QtCore.QRect(140, 440, 47, 13))
        self.questionsLeft.setText("")
        self.questionsLeft.setObjectName("questionsLeft")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(370, 10, 16, 381))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 640, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.excludedDiagnosisTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.excludedDiagnosisTableWidget.setGeometry(QtCore.QRect(410, 30, 321, 351))
        self.excludedDiagnosisTableWidget.setObjectName("excludedDiagnosisTableWidget")
        self.excludedDiagnosisTableWidget.setColumnCount(0)
        self.excludedDiagnosisTableWidget.setRowCount(0)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 0, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.countExcludedDiagnosesLabel = QtWidgets.QLabel(self.centralwidget)
        self.countExcludedDiagnosesLabel.setGeometry(QtCore.QRect(680, 50, 47, 13))
        self.countExcludedDiagnosesLabel.setText("")
        self.countExcludedDiagnosesLabel.setObjectName("countExcludedDiagnosesLabel")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 0, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.startpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.startpushButton.setGeometry(QtCore.QRect(10, 640, 141, 31))
        self.startpushButton.setObjectName("startpushButton")
        self.countAllQuestionLabel = QtWidgets.QLabel(self.centralwidget)
        self.countAllQuestionLabel.setGeometry(QtCore.QRect(140, 420, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.countAllQuestionLabel.setFont(font)
        self.countAllQuestionLabel.setText("")
        self.countAllQuestionLabel.setObjectName("countAllQuestionLabel")
        self.allDiagnosisTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.allDiagnosisTableWidget.setGeometry(QtCore.QRect(10, 30, 351, 351))
        self.allDiagnosisTableWidget.setObjectName("leftDiagnosisTableWidget")
        self.allDiagnosisTableWidget.setColumnCount(0)
        self.allDiagnosisTableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Экспертная система"))
        self.questionTextLabel.setText(_translate("MainWindow", "Тут будет вопрос..."))
        self.answerText.setText(_translate("MainWindow", "Тут ответ (диагноз)"))
        self.yesPushButton.setText(_translate("MainWindow", "Yes"))
        self.noPushButton.setText(_translate("MainWindow", "No"))
        self.label.setText(_translate("MainWindow", "Задано вопросов:"))
        self.label_2.setText(_translate("MainWindow", "Осталось вопросов:"))
        self.label_4.setText(_translate("MainWindow", "Ответ: "))
        self.label_5.setText(_translate("MainWindow", "Исключенные диагнозы"))
        self.label_6.setText(_translate("MainWindow", "Диагнозы и их вероятности "))
        self.startpushButton.setText(_translate("MainWindow", "Start"))
