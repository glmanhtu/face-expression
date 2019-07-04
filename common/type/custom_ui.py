from PyQt5.QtWidgets import QSizePolicy, QPushButton


class BQSizePolicy(QSizePolicy):
    def __init__(self, width=QSizePolicy.Preferred, height=QSizePolicy.Preferred, h_stretch=0, v_stretch=0):
        super().__init__(width, height)
        self.setHorizontalStretch(h_stretch)
        self.setVerticalStretch(v_stretch)


class TabButton(QPushButton):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setFlat(True)
        self.setStyleSheet("border: 1px solid #999999; padding: 4px 10px;")
