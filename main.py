#создай тут фоторедактор Easy Editor!
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QListWidget, QFileDialog
import os
from PyQt5.QtGui import QPixmap 
from PIL import Image
from PyQt5.QtCore import Qt
#from PIL.ImageQT import ImageQT
from PIL.ImageFilter import (
    BLUR, SHARPEN
)
from PIL import ImageFilter



app = QApplication([])
window = QWidget()
window.setWindowTitle('Easy Editor')
folder = QPushButton('папка')



main_layout = QHBoxLayout()

left_layout = QVBoxLayout()

midle_layout = QVBoxLayout()

button_layout = QHBoxLayout()



image = QLabel('Картинка')
midle_layout.addWidget(image)

left_layout.addWidget(folder)

file_list = QListWidget()
left_layout.addWidget(file_list)




left = QPushButton("Лево")
right = QPushButton("Право")
mirror = QPushButton("Зеркало")
rez = QPushButton("Резкость")
bw = QPushButton("Ч/Б")

button_layout.addWidget(left)
button_layout.addWidget(right)
button_layout.addWidget(mirror)
button_layout.addWidget(rez)
button_layout.addWidget(bw)

midle_layout.addLayout(button_layout)
main_layout.addLayout(left_layout)
main_layout.addLayout(midle_layout)

class ImageProcessor():
    def __init__(self, path = None, image = None, filename = None):
        self.image = image
        self.filename = filename
        self.folder = 'new_folder'
    def load_image(self, filename):
        self.filename = filename
        image_path = os.path.join(workdir, filename)
        self.image = Image.open(image_path)
    def showImage(self, path):
        image.hide()
        pixmapimage = QPixmap(path)
        w, h = image.width(), image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        image.setPixmap(pixmapimage)
        image.show()
    def saveImage(self):
        path = os.path.join(workdir, self.folder)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def do_wb(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir, self.folder, self.filename)
        self.showImage(image_path)

    def left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.folder, self.filename)
        self.showImage(image_path)

    def right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.folder, self.filename)
        self.showImage(image_path)

    def rez(self):
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.folder, self.filename)
        self.showImage(image_path)

    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.folder, self.filename)
        self.showImage(image_path)        

imagep = ImageProcessor()

def showChosenimage(): 
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        imagep.load_image(filename)
        image_path = os.path.join(workdir, imagep.filename)
        imagep.showImage(image_path)
file_list.currentRowChanged.connect(showChosenimage)
            




def filter(files, extensions):
    result = []
    for file in files:
        for extension in extensions:
            if file.endswith(extension):
                result.append(file)
    return result
def showFilenameList():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    file = os.listdir(workdir)
    exception = ['.jpg','.png','.jpeg','.gif']
    f = filter(file, exception)
    file_list.clear()
    for file in f:
        file_list.addItem(file)


folder.clicked.connect(showFilenameList)

bw.clicked.connect(imagep.do_wb)
left.clicked.connect(imagep.left)
right.clicked.connect(imagep.right)
rez.clicked.connect(imagep.rez)
mirror.clicked.connect(imagep.mirror)



window.setLayout(main_layout)


window.show()
app.exec_()