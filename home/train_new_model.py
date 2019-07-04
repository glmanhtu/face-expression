from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLineEdit, QLabel, QPushButton, QHBoxLayout, QSizePolicy

from common.type.custom_ui import BQSizePolicy


class TrainNewModel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.second_tab_layout = QVBoxLayout(self)
        self.second_tab_layout.setContentsMargins(11, 11, 11, 11)
        self.second_tab_layout.setSpacing(6)
        self.second_tab_main_widget = QWidget(self)
        self.second_tab_main_widget.setSizePolicy(BQSizePolicy(v_stretch=10))
        grid_layout = QGridLayout(self.second_tab_main_widget)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(6)
        self.n_epochs = QLineEdit(self.second_tab_main_widget)
        self.n_epochs.setValidator(QIntValidator(0, 10000, self))
        grid_layout.addWidget(self.n_epochs, 0, 1, 1, 1)
        self.label_3 = QLabel(self.second_tab_main_widget)
        grid_layout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QLabel(self.second_tab_main_widget)
        grid_layout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QLabel(self.second_tab_main_widget)
        grid_layout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_3 = QLineEdit(self.second_tab_main_widget)
        grid_layout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.lineEdit_4 = QLineEdit(self.second_tab_main_widget)
        grid_layout.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.find_dataset = QPushButton(self.second_tab_main_widget)
        self.find_dataset.setObjectName("findDataset")
        grid_layout.addWidget(self.find_dataset, 1, 2, 1, 1)
        self.select_checkpoint_dir = QPushButton(self.second_tab_main_widget)
        self.select_checkpoint_dir.setObjectName("pushButton_3")
        grid_layout.addWidget(self.select_checkpoint_dir, 2, 2, 1, 1)
        self.second_tab_layout.addWidget(self.second_tab_main_widget)
        self.widget_4 = QWidget(self)
        second_tab_bot_layout = QHBoxLayout(self.widget_4)
        second_tab_bot_layout.setContentsMargins(0, 0, 0, 0)
        second_tab_bot_layout.setSpacing(6)
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setSizePolicy(BQSizePolicy(h_stretch=2))
        second_tab_bot_layout.addWidget(self.widget_6)
        self.start_training = QPushButton(self.widget_4)
        self.start_training.setSizePolicy(BQSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed, h_stretch=1))
        self.start_training.setObjectName("pushButton_4")
        second_tab_bot_layout.addWidget(self.start_training)
        self.second_tab_layout.addWidget(self.widget_4)

        _translate = QCoreApplication.translate
        self.label_3.setText(_translate("MainWindow", "Fer2013's dataset: "))
        self.find_dataset.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Number epochs:"))
        self.label_4.setText(_translate("MainWindow", "Checkpoint dir:"))
        self.select_checkpoint_dir.setText(_translate("MainWindow", "..."))
        self.start_training.setText(_translate("MainWindow", "Start"))