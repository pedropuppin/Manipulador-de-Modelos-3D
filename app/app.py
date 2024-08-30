import sys
from PySide6 import QtWidgets
from core.main_window import MyWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.setWindowTitle("3D auto model")
    widget.show()

    sys.exit(app.exec())