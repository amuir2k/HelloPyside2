# https://doc.qt.io/qtforpython/tutorials/index.html
# https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html
# https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html

import sys
from PySide2.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("Hello World")
    label.setMargin(20)
    label.show()
    sys.exit(app.exec_())