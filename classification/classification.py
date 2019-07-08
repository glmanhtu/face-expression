from PyQt5.QtCore import QCoreApplication, QRect, QMetaObject, Qt, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMenuBar, QSizePolicy, QWidget, QFrame, QVBoxLayout, QHBoxLayout

from classification.from_camera_widget import FromCameraWidget
from classification.from_image_widget import FromImageWidget
from common.type.custom_ui import TabButton
from common.utils import layout_utils


class Classification(QMainWindow):
    def __init__(self):
        super(Classification, self).__init__()
        self.setupUi(self)
        self.show()
    
    def setupUi(self, window):
        window.setObjectName("MainWindow")
        window.resize(758, 418)
        window.setMinimumSize(758, 418)
        self.centralWidget = QWidget(window)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sideBar = QWidget(self.centralWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sideBar.sizePolicy().hasHeightForWidth())
        self.sideBar.setSizePolicy(sizePolicy)
        self.sideBar.setObjectName("sideBar")
        self.verticalLayout = QVBoxLayout(self.sideBar)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setAlignment(Qt.AlignTop)
        self.fromImage = TabButton(self.sideBar)
        self.fromImage.setObjectName("fromImage")
        self.verticalLayout.addWidget(self.fromImage)
        self.fromCamera = TabButton(self.sideBar)
        self.fromCamera.setObjectName("fromCamera")
        self.verticalLayout.addWidget(self.fromCamera)
        self.horizontalLayout.addWidget(self.sideBar)
        self.line = QFrame(self.centralWidget)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.mainWindow = QWidget(self.centralWidget)

        self.mainLayout = QVBoxLayout(self.mainWindow)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(6)

        self.onImageSelect()

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWindow.sizePolicy().hasHeightForWidth())
        self.mainWindow.setSizePolicy(sizePolicy)
        self.mainWindow.setObjectName("mainWindow")
        self.horizontalLayout.addWidget(self.mainWindow)
        window.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(window)
        self.menuBar.setGeometry(QRect(0, 0, 758, 22))
        self.menuBar.setObjectName("menuBar")
        window.setMenuBar(self.menuBar)

        self.retranslateUi(window)
        QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fromImage.setText(_translate("MainWindow", "From Image"))
        self.fromCamera.setText(_translate("MainWindow", "Camera"))

    @pyqtSlot(bool, name='on_fromCamera_clicked')
    def onCameraSelect(self, checked=False):
        layout_utils.cleanLayout(self.mainLayout)
        self.mainLayout.addWidget(FromCameraWidget())

    @pyqtSlot(bool, name='on_fromImage_clicked')
    def onImageSelect(self, checked=False):
        layout_utils.cleanLayout(self.mainLayout)
        self.mainLayout.addWidget(FromImageWidget())
