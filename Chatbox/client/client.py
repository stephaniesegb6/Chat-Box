# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from network import Network
from _thread import *
from Name import Ui_Name


class Ui_ChatBox(object):
    def setupUi(self, ChatBox,name):
        ChatBox.setObjectName("ChatBox")
        ChatBox.resize(799, 710)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ChatBox.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ChatBox)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(11, 22, -1, -1)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.Messages = QtWidgets.QListWidget(self.widget_2)
        self.Messages.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.Messages.setObjectName("Messages")
        self.gridLayout.addWidget(self.Messages, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(12, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Message = QtWidgets.QLineEdit(self.widget)
        self.Message.setObjectName("Message")
        self.horizontalLayout.addWidget(self.Message)
        self.Send = QtWidgets.QPushButton(self.widget)
        self.Send.setObjectName("Send")
        self.Send.clicked.connect(self.send)
        self.horizontalLayout.addWidget(self.Send)
        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)
        ChatBox.setCentralWidget(self.centralwidget)
        # print(self.Message.text())

        self.retranslateUi(ChatBox)
        QtCore.QMetaObject.connectSlotsByName(ChatBox)

        self.n = Network() # Connect to the server
        self.name = name
        self.n.send(name)

    def retranslateUi(self, ChatBox):
        _translate = QtCore.QCoreApplication.translate
        ChatBox.setWindowTitle(_translate("ChatBox", "Chat Box"))
        self.Send.setText(_translate("ChatBox", "Send"))
        self.Send.setShortcut(_translate("ChatBox", "Return"))
    def receive(self) :
        while True :
            try :
                message = self.n.receive()
                self.Messages.addItem(message)
            except Exception as e : 
                print(e)
                # self.n.client.close()
                break
    def send(self) :
        message = self.Message.text()
        if message != '' :
            message = f'{self.name} : {message}'  
            self.n.send(message)
        self.Message.clear()    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChatBox = QtWidgets.QMainWindow()
    nameDialog = QtWidgets.QDialog()
    ui = Ui_Name()
    ui.setupUi(nameDialog)
    nameDialog.show()
    nameDialog.exec()
    name = ui.Name_user
    ui = Ui_ChatBox()
    ui.setupUi(ChatBox,name)
    ChatBox.show()
    start_new_thread(ui.receive,())
    sys.exit(app.exec())