import cv2
from PyQt5 import QtCore
from PyQt5.QtCore import QMetaObject, pyqtSlot, QDir, Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QFileDialog, QLabel, QVBoxLayout

from common.services import deep_learning_service
from common.type.custom_ui import BQSizePolicy
from common.utils import layout_utils


class FromImageWidget(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setMaximumSize(QtCore.QSize(16777215, 50))
        self.setObjectName("widget")
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.select_img_container = QWidget(self)

        self.hbox_layout = QHBoxLayout(self.select_img_container)
        self.hbox_layout.setContentsMargins(11, 11, 11, 11)
        self.hbox_layout.setSpacing(6)
        self.hidden_widget2 = QWidget(self.select_img_container)
        self.hbox_layout.addWidget(self.hidden_widget2)
        self.select_image = QPushButton(self.select_img_container)
        self.select_image.setObjectName("selectImage")
        self.hbox_layout.addWidget(self.select_image)
        self.hidden_widget1 = QWidget(self.select_img_container)
        self.hbox_layout.addWidget(self.hidden_widget1)

        self.main_layout.addWidget(self.select_img_container)

        self._translate = QtCore.QCoreApplication.translate
        self.select_image.setText(self._translate("MainWindow", "Select image"))
        QMetaObject.connectSlotsByName(self)

    def showImage(self, image_path):
        layout_utils.cleanLayout(self.main_layout)
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))
        widget = QWidget(self)
        hbox_layout = QHBoxLayout(widget)

        pic = QLabel(self)
        pic.setFixedSize(400, 300)
        pixmap = QPixmap(image_path)
        pic.setPixmap(pixmap.scaled(pic.size(), Qt.KeepAspectRatio))
        hbox_layout.addWidget(pic)

        self.main_layout.addWidget(widget)

        widget_2 = QWidget(self)
        hbox_layout_2 = QHBoxLayout(widget_2)

        self.detected_emotion = QLabel(self)
        self.detected_emotion.setSizePolicy(BQSizePolicy(h_stretch=3))
        hbox_layout_2.addWidget(self.detected_emotion)
        self.select_image = QPushButton(self)
        self.select_image.setObjectName("selectImage")
        self.select_image.setText(self._translate("MainWindow", "Select image"))
        self.select_image.clicked.connect(self.onSelectImage)
        hbox_layout_2.addWidget(self.select_image)

        self.main_layout.addWidget(widget_2)
        self.classifyImage(image_path)

    def classifyImage(self, imp_path):
        image = cv2.imread(imp_path)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('resources/opencv/haarcascade_frontalface_alt.xml')
        faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            crop_img = image[y: y + h, x: x + w]
            gray_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
            img_out = cv2.resize(gray_img, (48, 48), interpolation=cv2.INTER_CUBIC)
            predicted = deep_learning_service.predict_image(img_out)
            emotion = deep_learning_service.get_actual_labels(predicted[0])
            self.detected_emotion.setText(self._translate("MainWindow", "Detected emotion: " + emotion))
        else:
            self.detected_emotion.setText(self._translate("MainWindow", "No face detected."))

    @pyqtSlot(bool, name='on_selectImage_clicked')
    def onSelectImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', QDir.homePath(), "Image files (*.jpg)")
        if len(fname[0]) > 0:
            self.showImage(fname[0])
