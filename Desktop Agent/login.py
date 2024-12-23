from PyQt5 import QtCore, QtGui, QtWidgets
import constants
from server import Ui_MainWindow as s3

class Ui_MainWindow(object):
    def openNextWindow(self,mainWindow,previous_window):
        if self.username.text() == constants.USERNAME and self.password.text() == constants.PASSWORD:
            self.window = QtWidgets.QMainWindow()
            self.ui = s3()
            self.ui.setupUi(self.window,PreviousWindow=previous_window)
            mainWindow.hide()
            self.window.show()
    
    def setupUi(self, MainWindow,PreviousWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 247)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setStyleSheet("padding:2px 5px;")
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet("padding:2px 5px;")
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.openNextWindow(MainWindow,PreviousWindow))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        self.login_btn.setFont(font)
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn.setStyleSheet("padding:0px 30px;")
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout_2.addWidget(self.login_btn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Desktop Agent"))
        self.username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.login_btn.setText(_translate("MainWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
