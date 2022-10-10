/**
 * ---------------------------------------
 * This demo was created using amCharts 5.
 *
 * For more information visit:
 * https://www.amcharts.com/
 *
 * Documentation is available at:
 * https://www.amcharts.com/docs/v5/
 * ---------------------------------------
 */

// Create root and chart
// ran into error where DOM was not fully loaded
// before am5 was searching for chartdiv
// used ready function to solve
// Documentation for solution: https://www.amcharts.com/docs/v5/getting-started/root-element/
am5.ready(function() {
    var root = am5.Root.new("chartdiv_basic");

root.setThemes([
  am5themes_Animated.new(root)
]);

var chart = root.container.children.push( 
  am5xy.XYChart.new(root, {
    panY: false,
    wheelY: "zoomX",
    layout: root.verticalLayout
  }) 
);

// Define data
var data = [{ 
  category: "Research", 
  value1: 1000, 
  value2: 588 
}, { 
  category: "Marketing", 
  value1: 1200, 
  value2: 1800 
}, { 
  category: "Sales", 
  value1: 850, 
  value2: 1230 
}];

// Craete Y-axis
let yAxis = chart.yAxes.push(
  am5xy.ValueAxis.new(root, {
    renderer: am5xy.AxisRendererY.new(root, {
    })
  })
);

// Create X-Axis
var xAxis = chart.xAxes.push(
  am5xy.CategoryAxis.new(root, {
      maxDeviation: 0.2,
      renderer: am5xy.AxisRendererX.new(root, {
    }),
    categoryField: "category"
  })
);
xAxis.data.setAll(data);

// Create series
var series1 = chart.series.push( 
  am5xy.ColumnSeries.new(root, { 
    name: "Series", 
    xAxis: xAxis, 
    yAxis: yAxis, 
    valueYField: "value1", 
    categoryXField: "category",
    tooltip: am5.Tooltip.new(root, {})
  }) 
);
series1.data.setAll(data);

var series2 = chart.series.push( 
  am5xy.ColumnSeries.new(root, { 
    name: "Series", 
    xAxis: xAxis, 
    yAxis: yAxis, 
    valueYField: "value2", 
    categoryXField: "category" 
  }) 
);
series2.data.setAll(data);

// Add legend
var legend = chart.children.push(am5.Legend.new(root, {})); 
legend.data.setAll(chart.series.values);

});