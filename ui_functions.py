
from main import *

GLOBAL_STATE = 0

class UIFunctions(MainWindow):
    """docstring for UIFunctions."""

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        #IF NOT MAXIMIZE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.drop_shadow_layout.setContentsMargins(0,0,0,0)
            self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(51, 65, 156, 255), stop:0.86828 rgba(33, 108, 194, 255));border-radius:10px;")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.drop_shadow_layout.setContentsMargins(10,10,10,10)
            self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(51, 65, 156, 255), stop:0.86828 rgba(33, 108, 194, 255));border-radius:10px;")
            self.ui.btn_maximize.setToolTip("Maximize")

    def uiDefinitions(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #SET SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,100))

        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)
        self.ui.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda: self.close())

        # Create a grip to resize
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("QSizeGrip {width: 10px; height: 10px; margin: 5px;} QSizeGrip:hover {background-color: rgb(50,42,92)}")
        self.sizegrip.setToolTip("Resize")

        # Block CPU
        # self.lable1 = QLabel(self.ui.label_1)