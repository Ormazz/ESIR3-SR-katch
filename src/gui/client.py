import sys
from PyQt4 import QtCore, QtGui
from gui import window
from connection import connectionManager

class MainWindow(window.Ui_Form):

    def __init__(self, Form):
        super(window.Ui_Form, self).__init__()
        self.setupUi(Form)
        QtCore.QObject.connect(self.connectButton, QtCore.SIGNAL(window._fromUtf8("clicked()")), self.press_connection_to_peer)

    def press_connection_to_peer(self):
        ip_addr = self.ipAddressEdit.text()
        connectionManager.ConnectionManager().connection_to_peer(ip_addr)

def launch():
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = MainWindow(Form)
    Form.show()
    sys.exit(app.exec_())