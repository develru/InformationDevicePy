import QtQuick 2.4
import QtQuick.Layouts 1.3
import QtQuick.Controls 1.4
import "../styling"

Item {
    id: weatherSettings
    Background {
        anchors.fill: parent

        GridLayout {
            anchors.horizontalCenter:  parent.horizontalCenter
            columns: 2

            MyLabel {
                Layout.columnSpan: 2
                Layout.alignment: Qt.AlignHCenter
                font.pointSize: 22
                text: qsTr("Weather settings")
            }

            MyLabel {
                text: qsTr("Location")
            }
            TextField {
                id: locationTextField
                font.pointSize: 18
            }

            MyButton {
                Layout.alignment: Qt.AlignRight
                height: 40
                text: qsTr("Cancel")
                onClicked: weatherSettings.Stack.view.pop()
            }
            MyButton {
                Layout.alignment: Qt.AlignRight
                height: 40
                text: qsTr("Ok")
                onClicked: {
                    weather.requested_location = locationTextField.text
                    weatherSettings.Stack.view.pop()
                }
            }
        }
    }
}
