from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTabWidget, QMenuBar

from home.load_trained_model import LoadTrainedModelWidget
from home.train_new_model import TrainNewModel


class Home(QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        self.setupUi(self)
        self.show()
        self.tabs.setCurrentIndex(0)

    def setupUi(self, window):
        window.resize(600, 236)
        central_widget = QWidget(window)
        vertical_layout = QVBoxLayout(central_widget)
        vertical_layout.setContentsMargins(11, 11, 11, 11)
        vertical_layout.setSpacing(6)
        self.tabs = QTabWidget(central_widget)
        self.tabs.setTabShape(QTabWidget.Rounded)
        self.first_tab = LoadTrainedModelWidget()
        self.tabs.addTab(self.first_tab, "")

        self.second_tab = TrainNewModel()
        self.tabs.addTab(self.second_tab, "")
        vertical_layout.addWidget(self.tabs)
        window.setCentralWidget(central_widget)
        self.menuBar = QMenuBar(window)
        self.menuBar.setGeometry(QRect(0, 0, 600, 22))
        self.menuBar.setObjectName("menuBar")
        window.setMenuBar(self.menuBar)

        self.retranslateUi(window)
        self.tabs.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QCoreApplication.translate
        window.setWindowTitle(_translate("MainWindow", "Face Expression"))
        self.tabs.setTabText(self.tabs.indexOf(self.first_tab), _translate("MainWindow", "Load a trained model"))
        self.tabs.setTabText(self.tabs.indexOf(self.second_tab), _translate("MainWindow", "Train a new model"))