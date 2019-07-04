import sys

from PyQt5.QtWidgets import QApplication

# from common.services import deep_learning_service

# Number of images to be processed per time
from home.home import Home

# batch_size = 128
# epochs = 100

# checkpoint
# filepath = "checkpoint.saved.hdf5"

# deep_learning_service.train_model("fer2013/fer2013.csv", batch_size, epochs, filepath)

app = QApplication(sys.argv)

# Load home window
window = Home()

sys.exit(app.exec_())
