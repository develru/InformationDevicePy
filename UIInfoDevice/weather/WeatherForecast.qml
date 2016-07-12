import QtQuick 2.4
import QtQuick.Layouts 1.3
import "../styling"

Item {
    id: forecastView
    objectName: "forecastViewObject"
    transformOrigin: Item.Center

    anchors.fill: parent
    Component.onCompleted: weather.view_is_ready()
    Component.onDestruction: if (weather != null) weather.stop_timer()


    Background {
        id: background1
        anchors.fill: parent

        RowLayout {
            id: rowLayout1
            anchors.fill: parent

            ColumnLayout {
                id: columnLayout1
                Layout.preferredWidth: parent.width / 2
                Layout.columnSpan: 1
                Layout.rowSpan: 1
                anchors.topMargin: 0
                spacing: 10

                Image {
                    id: iconCurrent
                    width: 200
                    height: 200
                    Layout.preferredHeight: 200
                    Layout.preferredWidth: 200
                    fillMode: Image.PreserveAspectFit
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    sourceSize.height: 200
                    sourceSize.width: 200
                    source: weather.icon
                }

                MyLabel {
                    id: currentTemp
                    text: weather.temp + "°C"
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    font.pointSize: 22
                    font.bold: true
                }

                MyLabel {
                    id: currentDescription
                    text: weather.description
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    Layout.fillWidth: false
                    font.pointSize: 18
                }

                MyLabel {
                    id: currentLocation
                    text: weather.location
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    font.italic: true
                    font.pointSize: 18
                }
            }

            ColumnLayout {
                id: columnLayout2
                Layout.preferredWidth: parent.width / 2
                Layout.fillWidth: false
                Layout.fillHeight: false
                Layout.alignment: Qt.AlignRight | Qt.AlignVCenter

                ListView {
                    id: forecastListView
                    model: weather.data_model
                    delegate: ForecastDelegate {}
                    width: 400
                    height: 300
                    contentHeight: 300
                    contentWidth: 400
                    Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
                    spacing: 70

                }
            }
        }
    }
}
