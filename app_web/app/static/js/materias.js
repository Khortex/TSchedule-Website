var optionsBar1 = {
    responsive: true
};

var dataBar1 = {
    labels: ['1 a 3', '3 a 5', '5 a 7', '7 a 9', '9 a 11', '11 a 13', 'Mais de 13 (Horas)' ],
    datasets: [
        {
        label: "Calculo 1",
        data: [10, 11, 9, 19, 21, 9, 5],
        backgroundColor: "rgba(255, 20, 147, 1)",
        bordercolor: "rgba(169, 169, 169, 1)",
        borderWidth: 5
        },
        
    ]
};

var optionsBar2 = {
    responsive: true
};

var dataBar2 = {
    labels: ['1 a 3', '3 a 5', '5 a 7', '7 a 9', '9 a 11', '11 a 13', 'Mais de 13 (Horas)'],
    datasets: [
        {
           label: "Fisica 1",
           data: [8, 15, 17, 22, 8, 11, 3],
           backgroundColor: "rgba(138, 43, 226, 1)",
           bordercolor: "rgba(169, 169, 169, 1)",
           borderWidth: 5
        },   
    ]
}; 

var optionsBar3 = {
    responsive: true
};

var dataBar3 = {
    labels: ['1 a 3', '3 a 5', '5 a 7', '7 a 9', '9 a 11', '11 a 13', 'Mais de 13 (Horas)'],
    datasets: [
        {
            label: "Quimica EE",
            data: [10, 17, 21, 16, 12, 6, 2],
            backgroundColor: "rgba(127, 255, 0, 1)",
            bordercolor: "rgba(169, 169, 169, 1)",
            borderWidth: 5
        },
        
    ]
};

var optionsBar4 = {
    responsive: true
};

var dataBar4 = {
    labels: ['1 a 3', '3 a 5', '5 a 7', '7 a 9', '9 a 11', '11 a 13', 'Mais de 13 (Horas)'],
    datasets: [
        {
            label: "Programacao",
            data: [9, 15, 17, 19, 9, 10, 5],
            backgroundColor: "rgba(255, 215, 0, 1)",
            bordercolor: "rgba(169, 169, 169, 1)",
            borderWidth: 5
        },
        
    ]
};

var optionsBar5 = {
    responsive: true
};

var dataBar5 = {
    labels: ['1 a 3', '3 a 5', '5 a 7', '7 a 9', '9 a 11', '11 a 13', 'Mais de 13 (Horas)'],
    datasets: [
        {
           label: "Fisica Experimental",
           data: [29, 25, 14, 7, 4, 1, 4],
           backgroundColor: "rgba(0, 255, 255, 1)",
           bordercolor: "rgba(169, 169, 169, 1)",
           borderWidth: 5
        },
        
    ]
};

function start(){
    var ctx = document.getElementById("calculo1").getContext("2d");
    var BarChart = new Chart(ctx, {
          type: 'bar',
          data: dataBar1,
          options: optionsBar1          
    });

    var ctx2 = document.getElementById("fisica1").getContext("2d");
    var BarChart2 = new Chart(ctx2, {
          type: 'bar',
          data: dataBar2,
          options: optionsBar2          
    });

    var ctx3 = document.getElementById("quimica").getContext("2d");
    var BarChart3 = new Chart(ctx3, {
          type: 'bar',
          data: dataBar3,
          options: optionsBar3          
    });

    var ctx4 = document.getElementById("programacao").getContext("2d");
    var BarChart4 = new Chart(ctx4, {
          type: 'bar',
          data: dataBar4,
          options: optionsBar4          
    });

    var ctx5 = document.getElementById("fisexp").getContext("2d");
    var BarChart5 = new Chart(ctx5, {
          type: 'bar',
          data: dataBar5,
          options: optionsBar5          
    });
}

window.onload = start;


Chart.plugins.register({
beforeDraw: function(chartInstance) {
var ctx = chartInstance.chart.ctx;
ctx.fillStyle = "white";
ctx.fillRect(0, 0, chartInstance.chart.width, chartInstance.chart.height);
}
});
