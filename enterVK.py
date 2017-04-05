from PyQt4 import QtGui, QtCore
from sys import argv, exit
from vk_requests import create_api, exceptions

class ENTER(QtGui.QWidget):
    def __init__(self, parrent = None):
        QtGui.QWidget.__init__(self, parrent)
        self.setWindowTitle("PosteVK")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        vbox = QtGui.QVBoxLayout()
        self.setMaximumSize(220,145)
        self.setMinimumSize(220,145)
        login = QtGui.QLabel("Телефон или Email:")
        vbox.addWidget(login, 0)
        self.logEnt = QtGui.QLineEdit()
        vbox.addWidget(self.logEnt,1)
        password = QtGui.QLabel("Пароль:")
        vbox.addWidget(password, 2)
        self.passEnt = QtGui.QLineEdit()
        vbox.addWidget(self.passEnt,3)
        self.setLayout(vbox)
        Confirum = QtGui.QPushButton('Войти')
        QtCore.QObject.connect(Confirum, QtCore.SIGNAL('clicked()'), self.CHEK)
        vbox.addWidget(Confirum, 4)
    def CHEK(self):
        try:
            api = create_api(app_id = 5618012,
                         login = self.logEnt.text(),
                         password = self.passEnt.text(),
                         scope = ['offline', 'status', 'wall', 'photo'],
                         api_version = '5.53')

            import poste
            poste.G.show()


        except exceptions.VkAuthError:
            print("Не верный логин или пароль")


app2 = QtGui.QApplication(argv)
win = ENTER()
win.show()
app2.exec_()

