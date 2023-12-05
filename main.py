import io
import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>343</width>
    <height>345</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="KolVoStones">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>81</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Kol-vo stones</string>
    </property>
   </widget>
   <widget class="QSpinBox" name="stones">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>0</y>
      <width>211</width>
      <height>24</height>
     </rect>
    </property>
   </widget>
   <widget class="QLCDNumber" name="remainLcd">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>30</y>
      <width>341</width>
      <height>23</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="SkolkoVsatStone">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>70</y>
      <width>81</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>SkolkoStone?</string>
    </property>
   </widget>
   <widget class="QSpinBox" name="takeInput">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>70</y>
      <width>251</width>
      <height>24</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="takeButton">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>100</y>
      <width>341</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>PushButton</string>
    </property>
   </widget>
   <widget class="QPushButton" name="startButton">
    <property name="geometry">
     <rect>
      <x>310</x>
      <y>0</y>
      <width>31</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>edit</string>
    </property>
   </widget>
   <widget class="QListWidget" name="listWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>130</y>
      <width>341</width>
      <height>191</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="resultLabel">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>320</y>
      <width>341</width>
      <height>21</height>
     </rect>
    </property>
    <property name="layoutDirection">
     <enum>Qt::LeftToRight</enum>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Pseudonym(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.startButton.clicked.connect(self.newGame)
        self.takeButton.clicked.connect(self.Move)
        self.count = 0
        self.count2 = 0

    def newGame(self):
        self.listWidget.clear()
        self.remainLcd.display(self.stones.text())
        self.count = int(self.stones.text())
        self.resultLabel.setText('')

    def Move(self):
        if self.count > 0:
            self.listWidget.addItem(self.takeInput.text())
            self.remainLcd.display(str(self.count - int(self.takeInput.text())))
            self.count -= int(self.takeInput.text())
            if self.count <= 0:
                self.resultLabel.setText('Победа игрока')
        else:
            self.resultLabel.setText('Победа компьютера')

        if self.count > 0:
            if self.count <= 3:
                self.count2 = self.count
                self.listWidget.addItem(str(self.count2))
                self.remainLcd.display(str(self.count - self.count2))
                self.count -= self.count2
            else:
                self.count2 = random.randint(1, 3)
                self.listWidget.addItem(str(self.count2))
                self.remainLcd.display(str(self.count - self.count2))
                self.count -= self.count2
            if self.count <= 0:
                self.resultLabel.setText('Победа компьютера')
        else:
            self.resultLabel.setText('Победа игрока')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pseudonym()
    ex.show()
    sys.exit(app.exec_())
