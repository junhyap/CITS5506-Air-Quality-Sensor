// using Amchart 5
// documentation: https://www.amcharts.com/docs/v5/charts/xy-chart/


// instantiating the chart
// ran into error where DOM was not fully loaded
// before am5 was searching for chartdiv
// used ready function to solve
// Documentation for solution: https://www.amcharts.com/docs/v5/getting-started/root-element/
am5.ready(function() {

    var root = am5.Root.new("temp_graph");
    var chart = root.container.children.push(
    am5xy.XYChart.new(root, {
        panX: true,
        panY: true,
        wheelX: "zoomX"
    })
);

chart.set("scrollbarX", am5.Scrollbar.new(root, { orientation: "horizontal" }));
chart.set("scrollbarY", am5.Scrollbar.new(root, { orientation: "vertical" }));

// adding axis
var yAxis = chart.yAxes.push(
    am5xy.ValueAxis.new(root, {
      renderer: am5xy.AxisRendererY.new(root, {})
    })
  );


// Axis renderer
// selected DateAxis
// Documentation: https://www.amcharts.com/docs/v5/charts/xy-chart/axes/date-axis/
// time unit is set to minute
var xAxis = chart.xAxes.push(
    am5xy.DateAxis.new(root, {
      baseInterval: { timeUnit: "minute", count: 1 },
      renderer: am5xy.AxisRendererX.new(root, {})
    })
  );

/*
var xRenderer = xAxis.get("renderer");
xRenderer.grid.template.setAll({
  stroke: am5.Color.fromCSS("rgba(255, 255, 255, 1)")
});
*/

/*
var xRenderer = xAxis.get("renderer");
xRenderer.ticks.template.setAll({
  color: am5.Color.fromCSS("rgba(255, 255, 255, 1)")
});
*/

// Adding series
// selected line series
// Documentation: https://www.amcharts.com/docs/v5/charts/xy-chart/series/line-series/
var series = chart.series.push(
    am5xy.LineSeries.new(root, {
      name: "Series",
      xAxis: xAxis,
      yAxis: yAxis,
      valueYField: "temp",
      valueXField: "js_timestamp"
    })
  );

  /*
  var series2 = chart.series.push(
    am5xy.StepLineSeries.new(root, {
      name: "Series2",
      xAxis: xAxis,
      yAxis: yAxis,
      valueYField: "temperature",
      valueXField: "time",
      //noRisers: true,
      //fill: am5.color(0x095256),
      //stepWidth: am5.percent(50),
      //locationX: 0.25
    })
  );
  */

  //xAxis.axisHeader.children.push(am5.Label.new(root, {
  //  text: "Temperature (C˚)",
  //  fontWeight: "500",
  //}));

  yAxis.children.moveValue(am5.Label.new(root, { 
    text: "Temperature (C˚)", 
    rotation: -90, 
    y: am5.p50, 
    centerX: am5.p50,
    fill: am5.Color.fromCSS("rgba(255, 255, 255, 1)")
}), 0);

xAxis.children.push(am5.Label.new(root, { 
    text: "Time", 
    x: am5.p50, 
    centerX: am5.p50,
    fill: am5.Color.fromCSS("rgba(255, 255, 255, 1)")
}));

//var graph_data = document.getElementById("graph_data").textContent;

//console.log(graph_data);

series.data.setAll(temp_data_to_graph);


}); // closing ready function