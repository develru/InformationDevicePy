"""
    Copyright (C) 2016  Richard Schwalk

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

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
