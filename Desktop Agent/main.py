from PyQt5 import QtCore, QtGui, QtWidgets
import resource_file_rc
from login import Ui_MainWindow as s2
import os
import constants
from send_server_request import send_request
from check_occupancy import get_occupancy_status
import time
import configparser
from send_server_request import send_request

class Ui_MainWindow(object):

    def openNextWindow(self,mainWindow):
        self.window = QtWidgets.QMainWindow()
        self.ui = s2()
        self.ui.setupUi(self.window,PreviousWindow=mainWindow)
        mainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 247)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.settings_btn = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.openNextWindow(MainWindow))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(14)
        self.settings_btn.setFont(font)
        self.settings_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_btn.setStyleSheet("background:transparent;")
        self.settings_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/resource/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_btn.setIcon(icon)
        self.settings_btn.setIconSize(QtCore.QSize(30, 30))
        self.settings_btn.setObjectName("settings_btn")
        self.horizontalLayout_2.addWidget(self.settings_btn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.status_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.status_btn.setFont(font)
        self.status_btn.setStyleSheet("background-color:#FF474C;\n"
"border-radius:12px;\n"
"\n"
"")
        self.status_btn.setText("")
        self.status_btn.setObjectName("status_btn")
        self.horizontalLayout_2.addWidget(self.status_btn, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.auto_radio_btn = QtWidgets.QRadioButton(self.centralwidget, clicked = lambda : self.auto_clicked())
        font = QtGui.QFont()
        font.setPointSize(14)
        self.auto_radio_btn.setFont(font)
        self.auto_radio_btn.setObjectName("auto_radio_btn")
        self.horizontalLayout.addWidget(self.auto_radio_btn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.manual_radio_btn = QtWidgets.QRadioButton(self.centralwidget, clicked = lambda : self.manual_clicked())
        font = QtGui.QFont()
        font.setPointSize(14)
        self.manual_radio_btn.setFont(font)
        self.manual_radio_btn.setObjectName("manual_radio_btn")
        self.horizontalLayout.addWidget(self.manual_radio_btn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.auto_radio_btn.setChecked(True)
        # self.server_connection = False

        # Timer to check the status.txt file periodically
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.check_status)
        self.timer.start(1000)  # Check every second

        # Timer to check the status.txt file periodically
        self.shutdown_timer = QtCore.QTimer()
        self.shutdown_timer.timeout.connect(self.shutdown)
        # self.shutdown_timer.start(120000)  # Check every second
        self.shutdown_timer.start(30000)

        # check whether relay id is already given
        config = configparser.ConfigParser()
        config.read(constants.CONFIG_FILE_PATH)
        
        try:
            url = config['CONFIGURATION']['URL']
            relay_id = int(config['CONFIGURATION']['RELAY_ID'])

            if url == '' or relay_id == 'no':
                print('APP NOT CONFIGURED, CONTACT LAB ADMINISTRATOR')
            else:
                print('CONNECTING TO SERVER')
                response = send_request(relay_id,1)
                if response:
                    constants.SERVER_STATUS = True
                else:
                    print('CONNECTION FAILED')
        except Exception as e:
            print('APP NOT CONFIGURED, CONTACT LAB ADMINISTRATOR')
            print('CONNECTION FAILED')


        # self.config_timer = QtCore.QTimer()
        # self.config_timer.timeout.connect(self.configurations)
        # self.config_timer.start(self.configurations)

    def check_status(self):
        if constants.SERVER_STATUS:
            self.status_btn.setStyleSheet("background-color:#90EE90;\n"
                                        "border-radius:12px;\n"
                                        "\n"
                                        "")
            # self.server_connection = True

    # def configurations(self):
    #     if not os.path.exists(constants.DESKTOP_AGENT_PATH):
    #         create_config_file()
    #     else:
    #         config_file_data = load_config_file()

    def shutdown(self):
        print('CHECKING FOR SHUTDOWN')
        print(f'AUTO STATUS : {constants.AUTO_STATUS}')
        print(f'SERVER STATUS : {constants.SERVER_STATUS}')
        print(f'OCCUPANCY STATUS : {get_occupancy_status()}')
        if constants.AUTO_STATUS == 1 and constants.SERVER_STATUS == True and get_occupancy_status() == False:
            print('SHUTTING DOWN IN 5 SECONDS')
            time.sleep(5)
            os.system("shutdown /s /t 1")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Desktop Agent"))
        self.auto_radio_btn.setText(_translate("MainWindow", "Auto"))
        self.manual_radio_btn.setText(_translate("MainWindow", "Manual"))

    def manual_clicked(self):
        if constants.SERVER_STATUS:
            constants.AUTO_STATUS = 0
            send_request(constants.RELAY_ID,0) #constants.AUTO_STATUS
            # constants.AUTO_STATUS = 0

    def auto_clicked(self):
        if constants.SERVER_STATUS:
            constants.AUTO_STATUS = 1
            send_request(constants.RELAY_ID,1) #constants.AUTO_STATUS
            # constants.AUTO_STATUS = 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
