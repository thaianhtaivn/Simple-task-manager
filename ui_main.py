# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainXqedkm.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(854, 610)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QHBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(6)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(9, 9, 9, 9)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(51, 65, 156, 255), stop:0.86828 rgba(33, 108, 194, 255));\n"
"border-radius:10px;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_bar.sizePolicy().hasHeightForWidth())
        self.title_bar.setSizePolicy(sizePolicy)
        self.title_bar.setMaximumSize(QSize(16777215, 150))
        self.title_bar.setLayoutDirection(Qt.LeftToRight)
        self.title_bar.setStyleSheet(u"background-color:none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setStyleSheet(u"border:none;")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Swis721 Blk BT")
        font.setPointSize(14)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"QLabel{\n"
"color: rgb(8, 255, 206);\n"
"}\n"
"QLabel:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}\n"
"\n"
"")
        self.label_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_7.addWidget(self.label_title)

        self.label_time = QLabel(self.frame_title)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setMinimumSize(QSize(0, 50))
        self.label_time.setMaximumSize(QSize(300, 16777215))
        self.label_time.setFont(font)
        self.label_time.setStyleSheet(u"QLabel{\n"
"color: rgb(8, 255, 206);\n"
"}\n"
"QLabel:hover{\n"
"color: rgba(8, 255, 206,150);\n"
"}\n"
"\n"
"")
        self.label_time.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_7.addWidget(self.label_time)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(80, 16777215))
        self.frame_btns.setStyleSheet(u"border:none;")
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 140)
        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(16, 16))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(0, 255, 127);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0, 255, 127,120);\n"
"}")
        self.btn_maximize.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.btn_maximize)

        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(16, 16))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 166, 11);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 166, 11,120);\n"
"}")
        self.btn_minimize.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(16, 16))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(213, 14, 14);\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(213, 14, 14,120);\n"
"}")
        self.btn_close.setCheckable(False)
        self.btn_close.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        sizePolicy.setHeightForWidth(self.content_bar.sizePolicy().hasHeightForWidth())
        self.content_bar.setSizePolicy(sizePolicy)
        self.content_bar.setMaximumSize(QSize(16777215, 16777215))
        self.content_bar.setStyleSheet(u"background-color:none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_bar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color:none;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_4 = QVBoxLayout(self.page_home)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content_home = QFrame(self.page_home)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_content_home)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_infor = QFrame(self.frame_content_home)
        self.frame_infor.setObjectName(u"frame_infor")
        self.frame_infor.setMinimumSize(QSize(0, 0))
        self.frame_infor.setMaximumSize(QSize(16777215, 16777215))
        self.frame_infor.setFrameShape(QFrame.StyledPanel)
        self.frame_infor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_infor)
        self.horizontalLayout_6.setSpacing(30)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 30, 10, 30)
        self.frame_circle_1 = QFrame(self.frame_infor)
        self.frame_circle_1.setObjectName(u"frame_circle_1")
        self.frame_circle_1.setMinimumSize(QSize(240, 240))
        self.frame_circle_1.setMaximumSize(QSize(240, 240))
        self.frame_circle_1.setStyleSheet(u"QFrame{\n""border: 5px solid rgb(60,231,195);\n""border-radius: 120px;\n""}\n""\n""QFrame:hover{\n""border: 5px solid rgba(0, 116, 118, 150);\n""}")
        self.frame_circle_1.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_circle_1)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 40, 10, 40)
        self.label_1 = QLabel(self.frame_circle_1)
        self.label_1.setObjectName(u"label_1")
        font1 = QFont()
        font1.setFamily(u"Swis721 Hv BT")
        font1.setPointSize(13)
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"border:none;\n"
"color: rgb(170, 255, 127);")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_1)

        self.label_2 = QLabel(self.frame_circle_1)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Swis721 Hv BT")
        font2.setPointSize(50)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"border:none;\n"
"color: rgb(255, 252, 233);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_circle_1)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamily(u"Swis721 Hv BT")
        font3.setPointSize(9)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"border:none;\n"
"color: rgb(0, 170, 127);")
        self.label_3.setLineWidth(0)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_circle_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border:none;\n"
"color: rgb(2, 120, 230);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)


        self.horizontalLayout_6.addWidget(self.frame_circle_1)

        self.frame_circle_2 = QFrame(self.frame_infor)
        self.frame_circle_2.setObjectName(u"frame_circle_2")
        self.frame_circle_2.setMinimumSize(QSize(240, 240))
        self.frame_circle_2.setMaximumSize(QSize(240, 240))
        self.frame_circle_2.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(60,231,195);\n"
"	border-radius: 120px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 5px solid rgba(0, 116, 118, 150);\n"
"}")
        self.frame_circle_2.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_circle_2)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 40, 10, 40)
        self.label_5 = QLabel(self.frame_circle_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"border:none;\n"
"color: rgb(170, 255, 127);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_circle_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"border:none;\n"
"color: rgb(255, 252, 233);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_circle_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"border:none;\n"
"color: rgb(0, 170, 127);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_circle_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"border:none;\n"
"color: rgb(2, 120, 230);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)


        self.horizontalLayout_6.addWidget(self.frame_circle_2)

        self.frame_circle_3 = QFrame(self.frame_infor)
        self.frame_circle_3.setObjectName(u"frame_circle_3")
        self.frame_circle_3.setMinimumSize(QSize(240, 240))
        self.frame_circle_3.setMaximumSize(QSize(240, 240))
        self.frame_circle_3.setStyleSheet(u"QFrame{\n"
"	border: 5px solid rgb(60,231,195);\n"
"	border-radius: 120px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 5px solid rgba(0, 116, 118, 150);\n"
"}")
        self.frame_circle_3.setFrameShape(QFrame.StyledPanel)
        self.frame_circle_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_circle_3)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 40, 10, 40)
        self.label_9 = QLabel(self.frame_circle_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"border:none;\n"
"color: rgb(170, 255, 127);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_circle_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"border:none;\n"
"color: rgb(255, 252, 233);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_circle_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"border:none;\n"
"color: rgb(0, 170, 127);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_circle_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"border:none;\n"
"color: rgb(2, 120, 230);")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_12)


        self.horizontalLayout_6.addWidget(self.frame_circle_3)


        self.verticalLayout_5.addWidget(self.frame_infor)

        self.frame_text = QFrame(self.frame_content_home)
        self.frame_text.setObjectName(u"frame_text")
        sizePolicy.setHeightForWidth(self.frame_text.sizePolicy().hasHeightForWidth())
        self.frame_text.setSizePolicy(sizePolicy)
        self.frame_text.setMinimumSize(QSize(0, 70))
        self.frame_text.setMaximumSize(QSize(16777215, 100))
        self.frame_text.setFrameShape(QFrame.StyledPanel)
        self.frame_text.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_text)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(30, 10, 30, 10)
        self.label_quote = QLabel(self.frame_text)
        self.label_quote.setObjectName(u"label_quote")
        sizePolicy.setHeightForWidth(self.label_quote.sizePolicy().hasHeightForWidth())
        self.label_quote.setSizePolicy(sizePolicy)
        self.label_quote.setSizeIncrement(QSize(1, 1))
        font4 = QFont()
        font4.setFamily(u"UVN Vung Tau")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(True)
        font4.setWeight(75)
        self.label_quote.setFont(font4)
        self.label_quote.setAutoFillBackground(False)
        self.label_quote.setStyleSheet(u"color: rgb(110, 33, 198);\n"
"background-color: rgba(238, 249, 241,150);")
        self.label_quote.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_quote)


        self.verticalLayout_5.addWidget(self.frame_text)


        self.verticalLayout_4.addWidget(self.frame_content_home)

        self.stackedWidget.addWidget(self.page_home)
        self.page_credits = QWidget()
        self.page_credits.setObjectName(u"page_credits")
        self.stackedWidget.addWidget(self.page_credits)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color:none;")
        self.credits_bar.setFrameShape(QFrame.StyledPanel)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_label_credits)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setMinimumSize(QSize(0, 30))
        font5 = QFont()
        font5.setFamily(u"MS Reference Sans Serif")
        font5.setPointSize(10)
        self.label_credits.setFont(font5)
        self.label_credits.setStyleSheet(u"QLabel{color: rgb(20, 15, 100);}\n"
"\n"
"\n"
"QLabel:hover{\n"
"	color: rgb(23, 15, 250);\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_credits)


        self.horizontalLayout_3.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMaximumSize(QSize(30, 16777215))
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"My App - Simple Task Manager", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"TIME", None))
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"CPU USEAGE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"25%", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Intel Xeon Dual | Xeon 1234U", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Temp: 51\u00b0C", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"GPU USEAGE", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"5%", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Strix Asus RX570", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Temp: 51\u00b0C", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"RAM USEAGE", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"8GB", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Total: 12GB", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Temp: 45\u00b0C", None))
        self.label_quote.setText(QCoreApplication.translate("MainWindow", u"DO WHAT YOU LOVE, LOVE WHAT YOU DO!", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Designer: Th\u00e1i Anh T\u00e0i; thaianhtaivn@gmail.com", None))
    # retranslateUi
