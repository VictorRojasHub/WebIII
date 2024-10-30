import mysql.connector
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
import sys


#Front-End Qtdesigner

app=QtWidgets.QApplication([])
formulario=uic.loadUi("frm_contas.ui")
formulario1=uic.loadUi("frm_login.ui")
formulario.show()
app.exec()


def connect():

    #string de conexão no Xampp

    conn = mysql.connector.connect (
        user = 'root',
        password = '',
        host = 'localhost',
        port = '3307',
        database ='cadastro_contas'
    )

    return conn





class AnimatedWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Define as cores para os tons de "midnight"
        self.colors = ['#2c3e50', '#34495e', '#1c2833']
        self.color_index = 0


        # Configurações da janela
        self.setWindowTitle('frm_contas.ui')
        self.setGeometry(100, 100, 400, 300)

        # Configura o temporizador
        self.timer = QTimer()
        self.timer.timeout.connect(self.change_color)
        self.timer.start(3000)  # Muda a cada 3 segundos

    def change_color(self):
        # Define a cor de fundo atual
        self.setStyleSheet(f'background-color: {self.colors[self.color_index]};')
        self.color_index = (self.color_index + 1) % len(self.colors)

app = QApplication(sys.argv)
window = AnimatedWindow()
window.show()
sys.exit(app.exec_())
