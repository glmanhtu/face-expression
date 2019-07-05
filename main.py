import sys

from PyQt5.QtWidgets import QApplication

from home.home import Home

app = QApplication(sys.argv)

# Load home window
window = Home()

sys.exit(app.exec_())
