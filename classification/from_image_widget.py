from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton


class FromImageWidget(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setMaximumSize(QtCore.QSize(16777215, 50))
        self.setObjectName("widget")
        self.horizontalLayout_2 = QHBoxLayout(self)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hiddenWidget2 = QWidget(self)
        self.hiddenWidget2.setObjectName("hiddenWidget2")
        self.horizontalLayout_2.addWidget(self.hiddenWidget2)
        self.selectImage = QPushButton(self)
        self.selectImage.setObjectName("selectImage")
        self.horizontalLayout_2.addWidget(self.selectImage)
        self.hiddenWidget1 = QWidget(self)
        self.hiddenWidget1.setObjectName("hiddenWidget1")
        self.horizontalLayout_2.addWidget(self.hiddenWidget1)

        _translate = QtCore.QCoreApplication.translate
        self.selectImage.setText(_translate("MainWindow", "Select image"))