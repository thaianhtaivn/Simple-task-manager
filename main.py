################################################################################
##
## BY: thaianhtaivn
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################
import datetime
import psutil
from psutil._common import bytes2human
import cpuinfo
import sys
import platform
from PyQt5.QtCore import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    defaultSize = 14

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Move WINDOW
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.title_bar.mouseMoveEvent = moveWindow
        # self.ui.label_3.setText('%s'%cpuinfo.get_cpu_info()['brand_raw'][:27])
        #Set ui uiDefinitions
        UIFunctions.uiDefinitions(self)
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

        # Loop for update
        self.timer = QTimer()
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.display_frame_circle1)
        self.timer.timeout.connect(self.display_frame_circle3)
        self.timer.timeout.connect(self.resize_text)

        self.timer.start()

    ## APP EVENTS

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


    def display_frame_circle1(self):

        self.ui.label_2.setText('%s%%'%psutil.cpu_percent())


    def display_frame_circle3(self):
        self.ui.label_10.setText('%s'%bytes2human(psutil.virtual_memory().used))
        self.ui.label_11.setText('Total: %s'%bytes2human(psutil.virtual_memory().total))

    def resize_text(self):

        if self.rect().width() // 60 != self.defaultSize:
            f = QFont('Swis721 Blk BT', self.rect().width() // 60)
            f1 = QFont('UVN Vung Tau', self.rect().width() // 60)
            self.ui.label_title.setFont(QtGui.QFont(f))
            self.ui.label_quote.setFont(QtGui.QFont(f1))
            self.ui.label_time.setFont(QtGui.QFont(f))
            self.defaultSize = self.rect().width()//60

            border_radius = self.rect().width()//7
            self.ui.frame_circle_1.setMaximumSize(QSize(self.rect().width()//3.5, self.rect().width()//3.5))
            # self.ui.frame_circle_1.setMinimumSize(QSize(self.rect().width()//3.5, self.rect().width()//3.5))
            self.ui.frame_circle_1.setStyleSheet(u"QFrame{\n""border: 5px solid rgb(60,231,195);\n""border-radius: %dpx;\n""}\n""\n""QFrame:hover{\n""border: 5px solid rgba(0, 116, 118, 150);\n""}"%(border_radius))

            self.ui.frame_circle_2.setMaximumSize(QSize(self.rect().width()//3.5, self.rect().width()//3.5))
            # self.ui.frame_circle_2.setMinimumSize(QSize(self.rect().width()//3.5, self.rect().width()//3.5))
            self.ui.frame_circle_2.setStyleSheet(u"QFrame{\n""border: 5px solid rgb(60,231,195);\n""border-radius: %dpx;\n""}\n""\n""QFrame:hover{\n""border: 5px solid rgba(0, 116, 118, 150);\n""}"%(border_radius))

            self.ui.frame_circle_3.setMaximumSize(QSize(self.rect().width()//3.5, self.rect().width()//3.5))
            # self.ui.frame_circle_3.setMinimumSize(QSize(self.rect().width()//3.5, self.rect().width()//3.5))
            self.ui.frame_circle_3.setStyleSheet(u"QFrame{\n""border: 5px solid rgb(60,231,195);\n""border-radius: %dpx;\n""}\n""\n""QFrame:hover{\n""border: 5px solid rgba(0, 116, 118, 150);\n""}"%(border_radius))

            print (self.defaultSize)
        else:
            pass
        #Update datetime
        self.ui.label_time.setText(datetime.datetime.now().strftime("%I:%M:%S %p"))
        pass





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
