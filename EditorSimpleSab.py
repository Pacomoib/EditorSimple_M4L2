from PyQt5.QtWidgets import QApplication, QWidget,QFileDialog, QLabel, QPushButton, QListWidget,QHBoxLayout,QVBoxLayout
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap 

from PIL import Image

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

class ImageProcessor():
    def __init__(self):
        self.image =None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modificado/'
    
    def LoadImage(self,dir,filename):
        #Al subir, recordar la ruta y el nombre del archivo
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir,filename)
        self.image = Image.open(image_path)
    
    def ShowImage(self,path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w,h = lb_image.width(),lb_image.height()
        pixmapimage = pixmapimage.scaled(w,h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

workimage = ImageProcessor()

def ShowChosenImage():
    if lw_files.currentRow() >= 0: 
        filename = lw_files.currentItem().text()
        workimage.LoadImage(workdir,filename)
        image_path = os.path.join(workimage.dir,workimage.filename)
        workimage.ShowImage(image_path)

lw_files.currentRowChanged.connect(ShowChosenImage)


app.exec()