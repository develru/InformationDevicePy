import QtQuick 2.4

WeatherForecastForm {
    anchors.fill: parent
    Component.onCompleted: weather.viewIsReaddy()
    Component.onDestruction: if (weather != null) weather.stopTimer()

    iconCurrent.source: weather.icon

    forecastListView {
        model: weather.dataModel
        delegate: ForecastDelegate {}
    }

//    forecastListView.model: weather.dataModel
//    forecastListView.delegate: forecastDelegate
}
