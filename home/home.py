from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel, QSizePolicy, QHBoxLayout, QLineEdit, \
    QPushButton, QGridLayout, QMenuBar

from common.type.custom_ui import BQSizePolicy


class Home(QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        self.setupUi(self)
        self.show()

    def setupUi(self, window):
        window.resize(600, 236)
        self.centralWidget = QWidget(window)
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.tabWidget = QTabWidget(self.centralWidget)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.label = QLabel(self.tab)
        self.label.setSizePolicy(BQSizePolicy(v_stretch=1))
        self.verticalLayout_2.addWidget(self.label)
        self.widget = QWidget(self.tab)
        self.widget.setSizePolicy(BQSizePolicy(v_stretch=2))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.lineEdit = QLineEdit(self.widget)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_2 = QWidget(self.tab)
        self.widget_2.setSizePolicy(BQSizePolicy(v_stretch=1))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setSizePolicy(BQSizePolicy(h_stretch=2))
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setSizePolicy(BQSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed, h_stretch=1))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.widget_5 = QWidget(self.tab_2)
        self.widget_5.setSizePolicy(BQSizePolicy(v_stretch=10))
        self.gridLayout = QGridLayout(self.widget_5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(6)
        self.lineEdit_2 = QLineEdit(self.widget_5)
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.label_3 = QLabel(self.widget_5)
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QLabel(self.widget_5)
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QLabel(self.widget_5)
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_3 = QLineEdit(self.widget_5)
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.lineEdit_4 = QLineEdit(self.widget_5)
        self.gridLayout.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.find_dataset = QPushButton(self.widget_5)
        self.find_dataset.setObjectName("findDataset")
        self.gridLayout.addWidget(self.find_dataset, 1, 2, 1, 1)
        self.pushButton_3 = QPushButton(self.widget_5)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.widget_4 = QWidget(self.tab_2)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setSizePolicy(BQSizePolicy(h_stretch=2))
        self.horizontalLayout_3.addWidget(self.widget_6)
        self.pushButton_4 = QPushButton(self.widget_4)
        self.pushButton_4.setSizePolicy(BQSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed, h_stretch=1))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        window.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(window)
        self.menuBar.setGeometry(QRect(0, 0, 600, 22))
        self.menuBar.setObjectName("menuBar")
        window.setMenuBar(self.menuBar)

        self.retranslateUi(window)
        self.tabWidget.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QCoreApplication.translate
        window.setWindowTitle(_translate("MainWindow", "Face Expression"))
        self.label.setText(_translate("MainWindow", "Please select the location of the trained model (*.hdf5)"))
        self.pushButton.setText(_translate("MainWindow", "..."))
        self.pushButton_2.setText(_translate("MainWindow", "Load selected model"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Load a trained model"))
        self.label_3.setText(_translate("MainWindow", "Fer2013's dataset: "))
        self.find_dataset.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Number epochs:"))
        self.label_4.setText(_translate("MainWindow", "Checkpoint dir:"))
        self.pushButton_3.setText(_translate("MainWindow", "..."))
        self.pushButton_4.setText(_translate("MainWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Train a new model"))