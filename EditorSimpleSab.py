from PyQt5.QtWidgets import QApplication, QWidget,QFileDialog, QLabel, QPushButton, QListWidget,QHBoxLayout,QVBoxLayout
import os

app = QApplication([])
main_win = QWidget()
main_win.resize(700,500)
main_win.setWindowTitle('Editor Simple')

btn_dir = QPushButton('Carpeta')
lw_files = QListWidget()
lb_image = QLabel('Imagen')

btn_left = QPushButton('Izquierda')
btn_right = QPushButton('Derecha')
btn_flip = QPushButton('Reflejo')
btn_sharp = QPushButton('Nitidez')
btn_bw = QPushButton('B/N')

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
row_tools = QHBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image)
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)

col2.addLayout(row_tools)
row.addLayout(col1,20)
row.addLayout(col2,80)

main_win.setLayout(row)
main_win.show()

workdir = ''
def Filter(files,extensions):
    result = []
    for filename in files: 
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def ChooseWorkDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def ShowFileNameList():
    extensions = ['.jpg','.jpeg','.png','.gif','.bmp']
    ChooseWorkDir()
    filenames = Filter(os.listdir(workdir),extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)

btn_dir.clicked.connect(ShowFileNameList)

app.exec()