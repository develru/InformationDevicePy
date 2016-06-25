import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4

ApplicationWindow {
    id: mainWin
    property string bgColor: "#078c72"
        property string toolBarColor: "#045d4c"
        property string buttonColor: "#033e32"
        property string buttonColorDown: "#022e26"
        property string buttonColorHover: "#20a58b"
        property string buttonTextColor: "#6ac3b2"
        property string buttonBorderColor: "#056d58"

    visible: true
    width: 800
    height: 480
    title: qsTr("Pi control")

    style: ApplicationWindowStyle {
            background: Rectangle {
                color: mainWin.bgColor
            }
        }
}
