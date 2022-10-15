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

// setting scroll bars in the X and Y direction
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
/*
var series = chart.series.push(
    am5xy.LineSeries.new(root, {
      name: "Series",
      xAxis: xAxis,
      yAxis: yAxis,
      valueYField: "temp",
      valueXField: "js_timestamp",
      tooltip: am5.Tooltip.new(root, {})
    })
  );
  */

  // Adding labels to the graph axes, setting the y label to vertical 
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


//series.get("tooltip").label.set("text", "{valueX.formatDate()}: {valueY}")
//  series.data.setAll(temp_data_to_graph);
  
//series.data.setAll(temp_data_to_graph);
// Create series
function createSeries(name, field) {
  var series = chart.series.push( 
    am5xy.LineSeries.new(root, { 
      name: name,
      xAxis: xAxis, 
      yAxis: yAxis, 
      valueYField: field, 
      valueXField: "js_timestamp",
      tooltip: am5.Tooltip.new(root, {})
    }) 
  );
  
  series.bullets.push(function() {
    // create the circle first
    var circle = am5.Circle.new(root, {
      radius: 1,
      stroke: series.get("fill"),
      strokeWidth: 2,
      interactive: true, //required to trigger the state on hover
      fill: am5.color(0xffffff)
    });

    circle.states.create('hover', {
      scale: 2
    });

    return am5.Bullet.new(root, {
      sprite: circle
    });
  });
  
  series.get("tooltip").label.set("text", "{valueX.formatDate()}: {valueY}")
  series.data.setAll(temp_data_to_graph);
}

createSeries("Series #1", "temp");

// Add cursor
chart.set("cursor", am5xy.XYCursor.new(root, {
  behavior: "zoomXY",
  xAxis: xAxis
}));


}); // closing ready function