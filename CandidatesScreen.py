# Form implementation generated from reading ui file 'CandidatesScreen.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CandidatesScreen(object):
    def setupUi(self, CandidatesScreen):
        CandidatesScreen.setObjectName("CandidatesScreen")
        CandidatesScreen.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=CandidatesScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.victor_profile_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.victor_profile_button.setGeometry(QtCore.QRect(160, 30, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.victor_profile_button.setFont(font)
        self.victor_profile_button.setObjectName("victor_profile_button")
        self.don_profile_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.don_profile_button.setGeometry(QtCore.QRect(160, 220, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.don_profile_button.setFont(font)
        self.don_profile_button.setObjectName("don_profile_button")
        self.nigil_profile_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.nigil_profile_button.setGeometry(QtCore.QRect(160, 410, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.nigil_profile_button.setFont(font)
        self.nigil_profile_button.setObjectName("nigil_profile_button")
        CandidatesScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=CandidatesScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        CandidatesScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=CandidatesScreen)
        self.statusbar.setObjectName("statusbar")
        CandidatesScreen.setStatusBar(self.statusbar)

        self.retranslateUi(CandidatesScreen)
        QtCore.QMetaObject.connectSlotsByName(CandidatesScreen)

    def retranslateUi(self, CandidatesScreen):
        _translate = QtCore.QCoreApplication.translate
        CandidatesScreen.setWindowTitle(_translate("CandidatesScreen", "MainWindow"))
        self.victor_profile_button.setText(_translate("CandidatesScreen", "Victor Emmanuel II"))
        self.don_profile_button.setText(_translate("CandidatesScreen", "Don Beyer"))
        self.nigil_profile_button.setText(_translate("CandidatesScreen", "Nigil Johnson"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CandidatesScreen = QtWidgets.QMainWindow()
    ui = Ui_CandidatesScreen()
    ui.setupUi(CandidatesScreen)
    CandidatesScreen.show()
    sys.exit(app.exec())