from PyQt4 import QtGui, QtCore
from sys import argv
import upld
from vk_requests import exceptions, create_api


class GUI(QtGui.QWidget):
    def __init__(self, parrent = None):
        QtGui.QWidget.__init__(self, parrent)
        self.setWindowTitle("PosteVK")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        grid = QtGui.QGridLayout()
        labText = QtGui.QLabel("Текст:")
        grid.addWidget(labText, 0,0)
        labText.setAlignment(QtCore.Qt.AlignTop)
        labPhoto =  QtGui.QLabel("Изображение:")
        labPhoto.setAlignment(QtCore.Qt.AlignTop)
        grid.addWidget(labPhoto, 1,0)
        self.text = QtGui.QTextEdit()
        grid.addWidget(self.text, 0,1)
        self.photo = QtGui.QPushButton(text = "Выбрать файл...")
        self.count = 0
        grid.addWidget(self.photo, 1,1)
        self.paths = []
        QtCore.QObject.connect(self.photo, QtCore.SIGNAL("clicked()"), self.BTNCLICKED)
        self.POSTE_BTN = QtGui.QPushButton(text = "Разместить")
        self.POSTE_BTN.setFont(QtGui.QFont('Bold',14))

        vbox = QtGui.QVBoxLayout()

        self.POSTE_BTN.setMinimumSize(120,50)
        self.POSTE_BTN.setStyleSheet("QPushButton { background-color: rgb(69,115,165); border : none;color: rgb(255,255,255)}"
                                "QPushButton:pressed { background-color: rgb(59, 94, 144); border: none;color: rgb(202,203,204)}")
        self.POSTE_BTN.setMaximumSize(120,50)
        QtCore.QObject.connect(self.POSTE_BTN, QtCore.SIGNAL("clicked()"), self.POSTE)
        vbox.addWidget(self.POSTE_BTN, 0)

        self.CLEAR = QtGui.QPushButton(text = "Обновить")
        self.CLEAR.setMaximumSize(120,30)
        vbox.addWidget(self.CLEAR, 1)
        QtCore.QObject.connect(self.CLEAR, QtCore.SIGNAL("clicked()"), self.CLEARING)

        grid.addLayout(vbox, 0,2)
        self.setLayout(grid)



    def BTNCLICKED(self):
        path, ok = QtGui.QFileDialog.getOpenFileNamesAndFilter(filter ="*.jpg *.jpeg *.png *.bmp *.gif")
        if ok:
            x = path
            self.count +=1
            self.paths = self.paths + path
        print(self.paths, '\n',len(self.paths))
        if len(self.paths) == 10:
            self.photo.setDisabled(True)
    def POSTE(self):
        print('POSTED')
        self.POSTE_BTN.setStyleSheet("QPushButton { background-color: rgb(129,148,170); border : none;color: rgb(200,200,200)}")
        self.POSTE_BTN.setDisabled(True)
        PATHS = self.paths
        TEXT = self.text.toPlainText()
        upld.CREATE(PATHS, TEXT)
    def CLEARING(self):
        self.text.setText('')
        self.paths = []
        self.photo.setEnabled(True)
        self.POSTE_BTN.setDisabled(False)
        self.POSTE_BTN.setStyleSheet("QPushButton { background-color: rgb(69,115,165); border : none;color: rgb(255,255,255)}"
                               "QPushButton:pressed { background-color: rgb(59, 94, 144); border: none;color: rgb(202,203,204)}")

    # def CREATE(PATHS, TEXT='Test'):
    #     api = create_api(app_id=5540525, login='+79780728194',
    #                      password='Ctnnfhjdfhba1998',
    #                      scope=['offline', 'photos', 'wall'],
    #                      api_version='5.53')
    #
    #     if len(PATHS) > 0:
    #         upld_url = api.photos.getWallUploadServer()
    #         file = PATHS
    #         for i in range(len(file)):
    #             poste = post(upld_url['upload_url'], files={'photo': open(file[i], 'rb')})
    #             print(upld_url['upload_url'], '\n', poste.text)
    #             poste.status_code == codes.ok
    #             params = {'server': poste.json()['server'], 'photo': poste.json()['photo'],
    #                       'hash': poste.json()['hash']}
    #             wallphoto = api.photos.saveWallPhoto(**params)
    #             photoID.append(wallphoto[0]['id'])
    #
    #         params = {'attachments': [], 'message': TEXT}
    #         for i in range(len(photoID)):
    #             params['attachments'].append('photo' + '146897234_' + str(photoID[i]))
    #
    #         api.wall.post(**params)
    #     else:
    #         api.wall.post(message=(TEXT))


app = QtGui.QApplication(argv)
G = GUI()
app.exec_()
