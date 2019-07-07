import cv2
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, pyqtSignal, Qt, pyqtSlot, QCoreApplication
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

from common.services import deep_learning_service


class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    changeEmotion = pyqtSignal(str)

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face_cascade = cv2.CascadeClassifier('resources/opencv/haarcascade_frontalface_alt.xml')
                faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)

                if (len(faces)) != 0:
                    crop_img = frame[y: y + h, x: x + w]
                    gray_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
                    img_out = cv2.resize(gray_img, (48, 48), interpolation=cv2.INTER_CUBIC)
                    predicted = deep_learning_service.predict_image(img_out)
                    emotion = deep_learning_service.get_actual_labels(predicted[0])
                    self.changeEmotion.emit(emotion)
                else:
                    self.changeEmotion.emit("None")

                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
                p = convert_to_qt_format.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)


class FromCameraWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self._translate = QCoreApplication.translate

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(str)
    def setEmotion(self, emotion):
        if emotion == "None":
            self.emotion.setText(self._translate("MainWindow", "No face detected"))
        else:
            self.emotion.setText(self._translate("MainWindow", "Detected face emotion: " + emotion))

    def initUI(self):
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(6)
        self.label = QLabel(self)
        self.mainLayout.addWidget(self.label)
        self.emotion = QLabel(self)
        self.mainLayout.addWidget(self.emotion)

        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.changeEmotion.connect(self.setEmotion)
        th.start()

