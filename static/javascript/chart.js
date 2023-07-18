google.charts.load("current", {
    packages: ['corechart']
});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {

    var DUNM = '{{DNUM}}';
    var data = google.visualization.arrayToDataTable([
        ["name", "number", {
            role: "style"
        }],
        ["Doctors", DUNM , "#444444"],
        ["Patients", 31, "#444444"],
        ["Devices", 20, "#444444"],
        ["Appoints", 10, "#444444"],
        ["FeedBack", 9, "#444444"]
    ]);

    var view = new google.visualization.DataView(data);
    view.setColumns([0, 1, {
            calc: "stringify",
            sourceColumn: 1,
            type: "string",
            role: "annotation"
        },
        2
    ]);

    var options = {
        title: "",
        width: 600,
        height: 400,
        bar: {
            groupWidth: "50%"
        },
        legend: {
            position: "none"
        },
    };
    var chart = new google.visualization.ColumnChart(document.getElementById("columnchart_values"));
    chart.draw(view, options);
}