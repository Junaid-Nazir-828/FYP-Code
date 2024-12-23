from PyQt5 import QtCore, QtGui, QtWidgets
from send_server_request import send_request
import constants
import time
import configparser

class Ui_MainWindow(object):
    def openPreviousWindow(self,pWindow,cWindow):
        result = send_request(int(self.relay_id.text().strip()),1)
        constants.SERVER_STATUS = result
        if result:
            print('')
            config = configparser.ConfigParser()
            config.read(constants.CONFIG_FILE_PATH)
            config['CONFIGURATION']['RELAY_ID'] = self.relay_id.text()
            with open(constants.CONFIG_FILE_PATH, 'w') as configfile:
                config.write(configfile)
            constants.RELAY_ID = int(self.relay_id.text())
        
        time.sleep(2)
        cWindow.hide()
        pWindow.show()

    def setupUi(self, MainWindow,PreviousWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(475, 248)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.relay_id = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.relay_id.setFont(font)
        self.relay_id.setStyleSheet("padding:2px 5px;")
        self.relay_id.setObjectName("device_id")
        self.verticalLayout.addWidget(self.relay_id, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.send = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.openPreviousWindow(PreviousWindow,MainWindow))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(10)
        self.send.setFont(font)
        self.send.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send.setObjectName("send")
        self.verticalLayout_5.addWidget(self.send, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Desktop Agent"))
        self.relay_id.setPlaceholderText(_translate("MainWindow", "Relay ID"))
        self.send.setText(_translate("MainWindow", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
