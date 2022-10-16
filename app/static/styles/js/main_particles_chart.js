// using Amchart 5
// documentation: https://www.amcharts.com/docs/v5/charts/xy-chart/


// instantiating the chart
// ran into error where DOM was not fully loaded
// before am5 was searching for chartdiv
// used ready function to solve
// Documentation for solution: https://www.amcharts.com/docs/v5/getting-started/root-element/
am5.ready(function() {

    var root = am5.Root.new("particles_graph");
    var chart = root.container.children.push(
    am5xy.XYChart.new(root, {
        panX: true,
        panY: true,
        wheelX: "zoomX"
    })
);

// setting scroll bars in the X and Y direction
chart.set("scrollbarX", am5.Scrollbar.new(root, { orientation: "horizontal", start: 0.98, end: 1 }));
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
      start: 0.98,
      end: 1,
      baseInterval: { timeUnit: "second", count: 1 },
      renderer: am5xy.AxisRendererX.new(root, {})
    })
  );

// Setting the graph labels to white
var xRenderer = xAxis.get("renderer");
xRenderer.labels.template.setAll({
  fill: am5.Color.fromCSS("rgba(255, 255, 255, 1)")
});

var yRenderer = yAxis.get("renderer");
yRenderer.labels.template.setAll({
  fill: am5.Color.fromCSS("rgba(255, 255, 255, 1)")
});

// Adding series
// selected line series
// Documentation: https://www.amcharts.com/docs/v5/charts/xy-chart/series/line-series/
var series = chart.series.push(
    am5xy.LineSeries.new(root, {
      name: "Series",
      xAxis: xAxis,
      yAxis: yAxis,
      valueYField: "particles",
      valueXField: "js_timestamp"
    })
  );

  // Adding labels to the graph axes, setting the y label to vertical 
  yAxis.children.moveValue(am5.Label.new(root, { 
    text: "Particles (mM)", 
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


series.data.setAll(particles_data_to_graph);


}); // closing ready function