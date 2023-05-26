import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsLineItem, QGraphicsTextItem
from PyQt5.QtGui import QPen, QColor, QFont

class TimeAxis(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        # self.setRenderHint(QGraphicsView.Antialiasing)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setHorizontalScrollBarPolicy(1)
        self.setVerticalScrollBarPolicy(1)
        self.setSceneRect(0, 0, 1000, 100)
        self.pen = QPen(QColor(0, 0, 0))
        self.pen.setWidth(2)
        self.font = QFont()
        self.font.setPointSize(10)
        self.font.setBold(True)
        self.markers = []

    def add_marker(self, time):
        marker = QGraphicsLineItem(time, 0, time, 100)
        marker.setPen(self.pen)
        self.scene.addItem(marker)
        text = QGraphicsTextItem(str(time))
        text.setFont(self.font)
        text.setPos(time, 100)
        self.scene.addItem(text)
        self.markers.append((marker, text))

    def mousePressEvent(self, event):
        if event.button() == 1:
            pos = self.mapToScene(event.pos())
            print(pos.x())
            self.add_marker(pos.x())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    axis = TimeAxis()
    axis.show()
    sys.exit(app.exec_())