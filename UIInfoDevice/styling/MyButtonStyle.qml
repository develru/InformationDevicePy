import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4

ButtonStyle {
    background: Rectangle {
        id: bRect
        implicitWidth: 50
        implicitHeight: 25
        border.width: control.activeFocus ? 3 : 2
        border.color: mainWin.buttonBorderColor
        //                width: control.text.contentWidth
        //                height: control.height
        radius: 2
        color: control.pressed ? mainWin.buttonColorDown : (control.hovered ? mainWin.buttonColorHover : mainWin.buttonColor)
    }
    label: Item {
        id: labelItem
        Label {
            anchors.leftMargin: 8
            //                verticalAlignment: Text.AlignVCenter
            anchors.centerIn: parent
            color: mainWin.buttonTextColor
            font.pixelSize: control.height * 0.4
            text: control.text
        }
    }
}
