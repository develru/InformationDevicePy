from PyQt5.QtCore import QObject, QTimer, pyqtProperty, QTime, pyqtSignal


class CurrentTime(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._my_timer = QTimer(self)
        self._my_timer.timeout.connect(self.refreshTime)
        self._my_timer.start(10000)

    timeChanged = pyqtSignal()

    @pyqtProperty('QString', notify=timeChanged)
    def time(self):
        return QTime.currentTime().toString('hh:mm')

    def refreshTime(self):
        self.timeChanged.emit()
