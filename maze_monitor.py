import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt, QPoint, QRect, QThread, pyqtSignal


from enum import Enum
import time
import numpy as np

class Next_Action_Type(Enum):
    ACTION_UP = 0,
    ACTION_DOWN = 1,
    ACTION_LEFT = 2,
    ACTION_RIGHT = 3,
    ACTION_STAY = 4,
    NUM_NEXT_ACTION_TYPE = 5

class Maze_Auto_Update_Thread(QThread):
    signal_int = pyqtSignal(int)
    def __init__(self, handle, parent=None):
        super(Maze_Auto_Update_Thread, self).__init__(parent)
        self.run_handle = handle
    
    def run(self):
        # 在线程中执行长时间操作
        if self.run_handle != None:
            self.run_handle()
    
    def signal_emit(self, val):
        self.signal_int.emit(val)

class Maze(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.maze_auto_update_thread = Maze_Auto_Update_Thread(self.auto_update_maze_action_thread_exec)
        self.maze_auto_update_thread.signal_int.connect(self.update_pose_with_next_action)
        self.maze_auto_update_thread.start()

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

    def update_pose_with_next_action(self, action):
        if action == 0:
            if self.maze[self.player_pos.y()-1][self.player_pos.x()] == 0:
                self.player_pos.setY(self.player_pos.y()-1)
        elif action == 1:
            if self.maze[self.player_pos.y()+1][self.player_pos.x()] == 0:
                self.player_pos.setY(self.player_pos.y()+1)
        elif action == 2:
            if self.maze[self.player_pos.y()][self.player_pos.x()-1] == 0:
                self.player_pos.setX(self.player_pos.x()-1)
        elif action == 3:
            if self.maze[self.player_pos.y()][self.player_pos.x()+1] == 0:
                self.player_pos.setX(self.player_pos.x()+1)
        self.update()

    def auto_update_maze_action_thread_exec(self):
        while True:
            time.sleep(0.5)
            next_action = np.random.randint(0, 4)
            # print("------", next_action, Next_Action_Type(next_action))
            self.print_next_action_name_by_enum_id(next_action)
            self.maze_auto_update_thread.signal_int.emit(next_action) 

    def print_next_action_name_by_enum_id(self, action):
        if action == 0:
            print("ACTION_UP")
        elif action == 1:
            print("ACTION_DOWN")
        elif action == 2:
            print("ACTION_LEFT")
        elif action == 3:
            print("ACTION_RIGHT")
        elif action == 4:
            print("ACTION_STAY")
        else:
            print("ACTION_ERROR", action, Next_Action_Type.ACTION_RIGHT)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    maze = Maze()
    sys.exit(app.exec_())