import QtQuick 2.4
import QtQuick.Layouts 1.3
import "../styling"

Item {
    id: forecastDelegate

    Background {
        id: background1
        anchors.fill: parent

        RowLayout {
            id: rowLayout1
            spacing: 10

            Image {
                id: forecastIcon
                Layout.preferredHeight: 50
                Layout.preferredWidth: 50
                source: model.icon
            }

            ColumnLayout {
                id: columnLayout1

                MyLabel {
                    id: forecastTemp
                    text: model.temp
                }

                MyLabel {
                    id: forecastDescription
                    text: model.description
                }

                MyLabel {
                    id: forecastTime
                    text: model.time
                }
            }
        }
    }
}
