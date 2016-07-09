import QtQuick 2.4
import QtQuick.Layouts 1.3
import QtQuick.Controls 1.4
import "../styling"

Item {
    Background {
        anchors.fill: parent

        GridLayout {
            columns: 2

            MyLabel {
                Layout.columnSpan: 2
                Layout.alignment: Qt.AlignHCenter
                font.pointSize: 18
                text: qsTr("Weather settings")
            }

            MyLabel {
                text: qsTr("Location")
            }
            TextField {
            }
        }
    }
}
