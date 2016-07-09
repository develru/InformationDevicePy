import QtQuick 2.4
import QtQuick.Layouts 1.3

Item {
    Background {
        anchors.fill: parent

        GridLayout {
            columns: 2
            rows: 2

            MyLabel {
                text: qsTr("Location")
            }
        }
    }
}
