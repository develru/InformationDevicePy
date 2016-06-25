import sys

import PyQt5
from os import path, environ
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, QQmlComponent
from PyQt5.QtQuick import QQuickView


if __name__ == '__main__':
    environ['QT_LOGGING_TO_CONSOLE'] = '1'

    app = QGuiApplication(sys.argv)
    app.addLibraryPath(path.abspath(path.join(path.dirname(PyQt5.__file__), 'plugins')))
    filename = path.abspath(path.join(path.dirname(__file__), 'UIInfoDevice', 'UIInfoDevice.qml'))
    # engine = QQmlApplicationEngine()
    #
    # engine.load(QUrl(filename))

    view = QQuickView()
    view.setSource(QUrl(filename))
    view.show()

    sys.exit(app.exec_())
