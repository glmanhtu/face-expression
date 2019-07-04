def cleanLayout(layout):
    while layout.count():
        item = layout.takeAt(0)
        item.widget().deleteLater()
