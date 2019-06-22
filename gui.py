import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import scrap as scrap
import ftp as ftp
import smtp as smtp
import textwrap
import doc_to_txt

import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton)


class External(QThread):
    def __init__(self, filename, pswd_mail, pswd_ftp, pswd_forum, login):
        super().__init__()
        self.filename = filename
        self.pswd_mail = pswd_mail
        self.pswd_ftp = pswd_ftp
        self.pswd_forum = pswd_forum
        self.login = login

    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(int)

    def run(self):
        txt = doc_to_txt.convert(self.filename)
        print(txt.split('\n', 2)[1])
        print('------------------')
        print(txt[1:])
        # self.countChanged.emit(25)
        # smtp.mail_send(txt, self.pswd_mail, self.login)
        # self.countChanged.emit(50)
        # ftp.ftp_send(txt, self.pswd_ftp, self.login)
        # self.countChanged.emit(75)
        # scrap.send_to_forum(self.login, self.pswd_forum, txt)
        self.countChanged.emit(100)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.filePath = -1
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        app.setWindowIcon(QIcon('icon.jpg'))

        btn = QPushButton('Otwórz')
        btn.setToolTip('Załaduj plik .doc z postanowieniami')
        btn.resize(btn.sizeHint())
        btn.clicked.connect(self.openFileNameDialog)

        btn2 = QPushButton('Wyślij')
        btn2.setToolTip('<b>Wpierdol</b> postanowienia gdzie trzeba')
        btn2.resize(btn.sizeHint())
        btn2.clicked.connect(self.showDialog)

        e1 = QLineEdit()
        e1.setValidator(QIntValidator())
        e1.setMaxLength(4)
        e1.setFont(QFont("Arial", 20))

        hbox = QVBoxLayout()

        grid = QGridLayout()

        self.line_nick_forum = QLineEdit(self)
        self.line_pswd_forum = QLineEdit(self)
        self.line_nick_ftp = QLineEdit(self)
        self.line_pswd_ftp = QLineEdit(self)
        self.line_nick_poczta = QLineEdit(self)
        self.line_pswd_poczta = QLineEdit(self)

        grid.addWidget(self.createExampleGroup("Poczta", self.line_nick_poczta, self.line_pswd_poczta), 0, 0)
        grid.addWidget(self.createExampleGroup("FTP", self.line_nick_ftp, self.line_pswd_ftp), 0, 1)
        grid.addWidget(self.createExampleGroup("Forum", self.line_nick_forum, self.line_pswd_forum), 0, 2)
        grid.addWidget(self.label, 1, 0)
        grid.addWidget(btn, 1, 1)
        grid.addWidget(btn2, 1, 2)
        hbox.addLayout(grid)
        self.progress = QProgressBar()

        hbox.addWidget(self.progress)
        self.setLayout(hbox)

        # self.nameLabel = QLabel(self)
        # self.nameLabel.setText('Name:')
        # self.line = QLineEdit(self)
        # self.line.setEchoMode(QLineEdit.Password)
        # self.line.move(80, 20)
        # self.line.resize(200, 32)
        # self.nameLabel.move(20, 20)

        #

        # self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Poster')
        self.center()
        self.show()

    def onCountChanged(self, value):
        self.progress.setValue(value)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Wybierz Postanowienia", "",
                                                  "Postanowionka (*.doc)", options=options)
        if fileName:
            _, x = fileName.rsplit('/', 1)
            self.label.setText(x)
            self.filePath = fileName

    def createExampleGroup(self, name, line, line2):
        groupBox = QGroupBox(name)

        line.setPlaceholderText("Login")
        # line.setText("okragly")

        line2.setEchoMode(QLineEdit.Password)
        line2.setPlaceholderText("Hasło")

        vbox = QVBoxLayout()
        vbox.addWidget(line)
        vbox.addWidget(line2)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

    def showDialog(self):
        if self.filePath == -1:
            msgbox = QMessageBox.warning(self, 'Ups', 'Nie załączono pliku', QMessageBox.Ok)
        else:
            buttonReply = QMessageBox.information(self, 'Potwierdzonko', "Czy na pewno wysłać?",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.calc = External(self.filePath, self.line_pswd_poczta.text(), self.line_pswd_ftp.text(), self.line_pswd_forum.text(),
                                     self.line_nick_poczta.text())
                self.calc.countChanged.connect(self.onCountChanged)
                self.calc.start()
            else:
                print('No clicked.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
