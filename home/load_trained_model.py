import os

from PyQt5.QtCore import QCoreApplication, pyqtSlot, QDir, QMetaObject
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton, QSizePolicy, QFileDialog

from classification.classification import Classification
from common.services import deep_learning_service, data_transporter_service
from common.type.custom_ui import BQSizePolicy
from common.utils.constants import WINDOW_CHANEL


class LoadTrainedModelWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(11, 11, 11, 11)
        self.layout.setSpacing(6)
        self.select_trained_label = QLabel(self)
        self.select_trained_label.setSizePolicy(BQSizePolicy(v_stretch=1))
        self.layout.addWidget(self.select_trained_label)
        self.mainWidget = QWidget(self)
        self.mainWidget.setSizePolicy(BQSizePolicy(v_stretch=2))
        self.select_file_layout = QHBoxLayout(self.mainWidget)
        self.select_file_layout.setContentsMargins(0, 0, 0, 0)
        self.select_file_layout.setSpacing(6)
        self.trained_file_path = QLineEdit(self.mainWidget)
        self.select_file_layout.addWidget(self.trained_file_path)
        self.select_trained_file = QPushButton(self.mainWidget)
        self.select_trained_file.setObjectName("selectTrainedFile")
        self.select_file_layout.addWidget(self.select_trained_file)
        self.layout.addWidget(self.mainWidget)
        widget = QWidget(self)
        widget.setSizePolicy(BQSizePolicy(v_stretch=1))
        bot_layout = QHBoxLayout(widget)
        bot_layout.setContentsMargins(0, 0, 0, 0)
        bot_layout.setSpacing(6)
        hidden_widget = QWidget(widget)
        hidden_widget.setSizePolicy(BQSizePolicy(h_stretch=2))
        bot_layout.addWidget(hidden_widget)
        self.process_selected_file = QPushButton(widget)
        self.process_selected_file.setSizePolicy(BQSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed, h_stretch=1))
        self.process_selected_file.setObjectName("processSelectedFile")
        bot_layout.addWidget(self.process_selected_file)
        self.layout.addWidget(widget)

        _translate = QCoreApplication.translate
        self.select_trained_label.setText(
            _translate("MainWindow", "Please select the location of the trained model (*.hdf5)"))
        self.select_trained_file.setText(_translate("MainWindow", "..."))
        self.process_selected_file.setText(_translate("MainWindow", "Load selected model"))

        QMetaObject.connectSlotsByName(self)

    @pyqtSlot(bool, name='on_selectTrainedFile_clicked')
    def selectTrainedFile(self, checked):
        fname = QFileDialog.getOpenFileName(self, 'Open file', QDir.homePath(), "HDF5 files (*.hdf5)")
        if len(fname[0]) > 0:
            self.trained_file_path.setText(fname[0])

    @pyqtSlot(bool, name='on_processSelectedFile_clicked')
    def loadTrainedFile(self, checked):
        if os.path.isfile(self.trained_file_path.text()):
            deep_learning_service.load_model(self.trained_file_path.text())
            data_transporter_service.fire(WINDOW_CHANEL, Classification())

