import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt, QPoint, QRect

class Maze(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Maze Game')
        self.setGeometry(100, 100, 600, 600)

        self.maze = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        self.player_pos = QPoint(1, 1)

        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawMaze(qp)
        self.drawPlayer(qp)
        qp.end()

    def drawMaze(self, qp):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == 1:
                    qp.fillRect(j*60, i*60, 60, 60, QBrush(Qt.black))

    def drawPlayer(self, qp):
        qp.setBrush(QBrush(Qt.red))
        qp.drawEllipse(QRect(self.player_pos.x()*60+10, self.player_pos.y()*60+10, 40, 40))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            if self.maze[self.player_pos.y()-1][self.player_pos.x()] == 0:
                self.player_pos.setY(self.player_pos.y()-1)
                self.update()
        elif event.key() == Qt.Key_Down:
            if self.maze[self.player_pos.y()+1][self.player_pos.x()] == 0:
                self.player_pos.setY(self.player_pos.y()+1)
                self.update()
        elif event.key() == Qt.Key_Left:
            if self.maze[self.player_pos.y()][self.player_pos.x()-1] == 0:
                self.player_pos.setX(self.player_pos.x()-1)
                self.update()
        elif event.key() == Qt.Key_Right:
            if self.maze[self.player_pos.y()][self.player_pos.x()+1] == 0:
                self.player_pos.setX(self.player_pos.x()+1)
                self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    maze = Maze()
    sys.exit(app.exec_())