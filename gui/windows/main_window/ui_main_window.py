from qt_core import *

#MAIN WINDOW
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        

        #SET INITIAL PARAMETERS
        parent.resize(1200,720)
        parent.setMinimumSize(960,540)

        #CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #282a36")

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)