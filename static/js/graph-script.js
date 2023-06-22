// SIDEBAR TOGGLE
var sidebarOpen = false;
var subjects_list = []
var sidebar = document.getElementById("sidebar");

function openSidebar() {
  if (!sidebarOpen) {
    sidebar.classList.add("sidebar-responsive");
    sidebarOpen = true;
  }
}

function closeSidebar() {
  if (sidebarOpen) {
    sidebar.classList.remove("sidebar-responsive");
    sidebarOpen = false;
  }
}

// Function to fetch data using Axios
function api_data() {
  return axios.get('http://127.0.0.1:8000/api/graph-data/')  // Replace '/api/chart-data/' with your actual API endpoint URL
    .then(response => {
      let obj = response.data.subject;
      return obj;
    })
    .catch(error => {
      console.error('Error fetching chart data:', error);
      return [];
    });
}

// Function to update the bar chart data and render the chart
// function updateBarChartWithData(barChart, newData) {
//   barChart.updateOptions({
//     series: [{
//       data: newData
//     }]
//   });
// }

// Function to initialize the bar chart
function initializeBarChart() {
  console.warn(api_data());
  var barChartOptions = {
    series: [{
      data: [10, 8]
    }],
    chart: {
      type: 'bar',
      height: 350,
      toolbar: {
        show: false
      },
    },
    colors: [
      "#246dec",
      "#cc3c43",
      // "#367952",
    ],
    plotOptions: {
      bar: {
        distributed: true,
        borderRadius: 4,
        horizontal: false,
        columnWidth: '40%',
      }
    },
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false
    },
    xaxis: {
      categories: ["IOT",  "WT"],
      // categories: subjects,
    },
    yaxis: {
      title: {
        text: "No of Students"
      }
    }
  };

  var barChart = new ApexCharts(document.querySelector("#bar-chart"), barChartOptions);
  barChart.render();

  // Fetch data and update the bar chart when the page loads
  // fetchData().then(data => {
  //   updateBarChartWithData(barChart, data);
  // });

  // Fetch data and update the bar chart periodically (example: every 5 seconds)
  setInterval(() => {
    fetchData().then(data => {
      updateBarChartWithData(barChart, data);
    });
  }, 5000);
}

initializeBarChart();

// Function to update the area chart data and render the chart
function updateAreaChartWithData(areaChart, newData) {
  areaChart.updateSeries([
    { name: 'student opted for subjects', data: newData.opted },
    { name: 'student changed subject', data: newData.changed }
  ]);
}

// Function to initialize the area chart
function initializeAreaChart() {
  var areaChartOptions = {
    series: [{
      name: 'student opted for subjects',
      data: [10, 8, 6, 8]
    }, {
      name: 'student changed subject',
      data: [5, 12, 4, 8]
    }],
    chart: {
      height: 350,
      type: 'area',
      toolbar: {
        show: false,
      },
    },
    colors: ["#367952", "#cc3c43"],
    dataLabels: {
      enabled: false,
    },
    stroke: {
      curve: 'smooth'
    },
    labels: ["IOT", "CFCS", "SOFT COMP", "WT"],
    markers: {
      size: 0
    },
    yaxis: [
      {
        title: {
          text: 'student opted for subject',
        },
      },
      {
        opposite: true,
        title: {
          text: 'student changed subject',
        },
      },
    ],
    tooltip: {
      shared: true,
      intersect: false,
    }
  };

  var areaChart = new ApexCharts(document.querySelector("#area-chart"), areaChartOptions);
  areaChart.render();

  // Fetch data and update the area chart when the page loads
  fetchData().then(data => {
    updateAreaChartWithData(areaChart, data);
  });

  // Fetch data and update the area chart periodically (example: every 5 seconds)
  setInterval(() => {
    fetchData().then(data => {
      updateAreaChartWithData(areaChart, data);
    });
  }, 5000);
}

initializeAreaChart();
