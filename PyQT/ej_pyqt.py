# pylint: disable=missing-docstring

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# creo una instancia de QApplication
app = QApplication(sys.argv)

# instancia principal GUI de la aplicacion:
# mini app
ventana = QWidget()
ventana.setWindowTitle('App PyQt5, by Dafne')
ventana.setGeometry(100, 100, 480, 80)
ventana.move(60, 15)

# contenido de la ventana.
mensaje = QLabel('<h1>Hola, esto es Python', parent=ventana)
mensaje.move(60, 15)

# App
ventana.show()

# Aplicacion corriendo:
sys.exit(app.exec_())
