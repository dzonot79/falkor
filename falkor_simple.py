import sys
import pyttsx3
from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6.QtGui import QMovie, QPixmap
from PyQt6.QtCore import Qt, QTimer

class Falkor(QLabel):
    def __init__(self):
        super().__init__()

        # -------- VOZ --------
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 110)

        # -------- VIDEO/GIF DE DESPERTAR --------
        self.movie = QMovie("despertar.gif")
        self.setMovie(self.movie)

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )

        self.old_pos = None

        # Iniciar animación
        self.movie.start()

        # Después de 5 segundos cambiar a imagen normal
        QTimer.singleShot(5000, self.activar_modo_normal)

    def activar_modo_normal(self):
        self.setPixmap(QPixmap("falkor.png"))
        self.hablar("Om mani peme hung")

    def hablar(self, texto):
        self.engine.say(texto)
        self.engine.runAndWait()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.hablar("Om mani peme hung")

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.pos())

app = QApplication(sys.argv)
falkor = Falkor()
falkor.show()
app.exec()
