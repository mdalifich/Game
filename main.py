import io
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
    <width>835</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QCalendarWidget" name="calendarWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>50</y>
      <width>501</width>
      <height>471</height>
     </rect>
    </property>
   </widget>
   <widget class="QTimeEdit" name="timeEdit">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>10</y>
      <width>501</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>530</y>
      <width>501</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="addEventBtn">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>560</y>
      <width>501</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Add Event</string>
    </property>
   </widget>
   <widget class="QListWidget" name="eventList">
    <property name="geometry">
     <rect>
      <x>510</x>
      <y>10</y>
      <width>321</width>
      <height>581</height>
     </rect>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.addEventBtn.clicked.connect(self.Plan)
        self.text = ''
        self.list1 = []

    def Plan(self):
        if len(str(self.timeEdit.time().hour())) == 1:
            self.text += '0' + str(self.timeEdit.time().hour())
        else:
            self.text += str(self.timeEdit.time().hour())
        if len(str(self.timeEdit.time().minute())) == 1:
            self.text += ':' + '0' + str(self.timeEdit.time().minute())
        else:
            self.text += ':' + str(self.timeEdit.time().minute())
        if len(str(self.timeEdit.time().second())) == 1:
            self.text += ':' + '0' + str(self.timeEdit.time().second())
        else:
            self.text += ':' + str(self.timeEdit.time().second())

        self.list1.append(self.text)
        self.list1.sort()
        self.eventList.clear()
        for i in self.list1:
            self.eventList.addItem(str(self.calendarWidget.selectedDate().year()) + '-' + str(
                self.calendarWidget.selectedDate().month()) + '-' + str(
                self.calendarWidget.selectedDate().day()) + ' ' +
                                   i + ' - ' + self.lineEdit.text())
        self.text = ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplePlanner()
    ex.show()
    sys.exit(app.exec_())