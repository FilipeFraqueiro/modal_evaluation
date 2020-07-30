import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import modal_analysis_bands
# 1
# 2
# 3
# 4
# 5
class main_layout(QWidget):
    def __init__(self):
        super(main_layout, self).__init__()

        self.layout_build()
    # 1
    # 2
    # 3
    def layout_build(self):
        lb_1 = QLabel("sum_threshold:")
        lb_2 = QLabel("fraction_threshold:")
        lb_3 = QLabel("cut_off:")
        lb_4 = QLabel("Select File:")

        vbl_1 = QVBoxLayout()
        vbl_1.addWidget(lb_1)
        vbl_1.addWidget(lb_2)
        vbl_1.addWidget(lb_3)
        vbl_1.addWidget(lb_4)

        te_1 = QTextEdit()
        te_2 = QTextEdit()
        te_3 = QTextEdit()
        btn_1 = QPushButton("File")
        btn_1.clicked.connect(self.getfile)

        vbl_2 = QVBoxLayout()
        vbl_2.addWidget(te_1)
        vbl_2.addWidget(te_2)
        vbl_2.addWidget(te_3)
        vbl_2.addWidget(btn_1)

        hbl_1 = QHBoxLayout()
        hbl_1.addLayout(vbl_1)
        hbl_1.addLayout(vbl_2)

        btn_2 = QPushButton("Run")
        btn_2.clicked.connect(self.run)

        self.pte_1 = QPlainTextEdit(self)
        self.pte_1.setReadOnly(True)

        vbl_main = QVBoxLayout()
        vbl_main.addLayout(hbl_1)
        vbl_main.addWidget(btn_2)
        vbl_main.addWidget(self.pte_1)

        self.setLayout(vbl_main)
    # 1
    # 2
    # 3
    def getfile(self):
        print("Select File")
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
        print(self.fname)
    # 1
    # 2
    # 3
    def run(self):
        print("Run")
        
        file_name = "modal_inputs.xlsx"
        
        text_out = modal_analysis_bands.main(file_name, 0.85, 0.03, -1)

        self.pte_1.insertPlainText(text_out)
# 1
# 2
# 3
# 4
# 5
class main_window(QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()

        self.setWindowTitle("sjo")
        self.define_main_window()

        self.menuBar_build()
    # 1
    # 2
    # 3
    def define_main_window(self):
        # Define Main window properties
        self.setMinimumSize(QSize(300, 100))    
        self.setWindowTitle("Python SkyLibris") 
        # self.setWindowIcon(QtGui.QIcon("images/skylibris_icon.png"))
        self.setStyleSheet("QMainWindow {background: 'white';}")
        
        self.top = 100
        self.left = 500
        self.width = 400
        self.height = 400
        self.setGeometry(self.left, self.top, self.width, self.height)

        main_ly = main_layout()
        self.setCentralWidget(main_ly)
    # 1
    # 2
    # 3
    def menuBar_build(self):        
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
# 1
# 2
# 3
# 4
# 5
if __name__ == "__main__":
    print("k")
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    mainWin = main_window()
    mainWin.show()
    sys.exit(app.exec_())
