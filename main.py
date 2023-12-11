import io
import math
import sys

from PyQt5 import uic
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>900</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="draw">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>20</y>
     <width>221</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Показать</string>
   </property>
  </widget>
   <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>270</x>
     <y>20</y>
     <width>57</width>
     <height>21</height>
    </rect>
   </property>
   <property name="text">
    <string>coeff:</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_3">
   <property name="geometry">
    <rect>
     <x>270</x>
     <y>50</y>
     <width>57</width>
     <height>21</height>
    </rect>
   </property>
   <property name="text">
    <string>n:</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="k">
   <property name="geometry">
    <rect>
     <x>310</x>
     <y>20</y>
     <width>471</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>0.9</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="n">
   <property name="geometry">
    <rect>
     <x>310</x>
     <y>50</y>
     <width>471</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>5</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>'''


class Square2(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.xUp, self.yUp = 50, 130
        self.box = 200
        self.color = QColor(250, 0, 0)
        self.rot = 0
        self.initUi()

    def initUi(self):
        self.draw.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw5(qp)
            qp.end()

    def paint(self, event):
        self.do_paint = True
        self.repaint()

    def draw5(self, qp):
        self.rot = 0
        self.box = 200
        self.xUp, self.yUp = -self.box / 2, -self.box / 2
        self.XX = self.xUp + self.box / 2
        self.YY = self.yUp + self.box / 2
        qp.setPen(self.color)
        qp.translate(self.XX + self.box, self.YY + self.box)
        for _ in range(int(self.n.text())):
            self.Rect = QRectF(int(self.xUp), int(self.yUp), int(self.box), int(self.box))
            self.maxu = self.box * float(self.k.text())
            self.minu = self.box - (self.box * float(self.k.text()))
            self.box = math.sqrt(self.minu * self.minu + self.maxu * self.maxu)
            self.xUp = self.XX - self.box / 2
            self.yUp = self.YY - self.box / 2
            self.rot = (math.atan(self.minu / self.maxu) * 180) / math.pi
            qp.drawRect(self.Rect)
            qp.rotate(self.rot)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square2()
    ex.show()
    sys.exit(app.exec_())
