    $(document).ready(function () {
        const config = {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: "X",
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data: [],
                    fill: false,
                },
                {   label: "Y",
                    backgroundColor: 'rgb(0, 0, 255)',
                    borderColor: 'rgb(0, 0, 255)',
                    data: [],
                    fill: false,
                },

                {    label: "Z",
                    backgroundColor: 'rgb(0,255, 0)',
                    borderColor: 'rgb(0, 255, 0)',
                    data: [],
                    fill: false,
                }],
            },
            options: {
                responsive: true,
                title: {
                    display: true,
                    text: 'Graph of MPUs data'
                },
                tooltips: {
                    mode: 'index',
                    intersect: false,
                },
                hover: {
                    mode: 'nearest',
                    intersect: true
                },
                scales: {
                    xAxes: [{
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: 'Time'
                        }
                    }],
                    yAxes: [{
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: 'Axis angles'
                        }
                    }]
                }
            }
        };

        const context = document.getElementById('canvas').getContext('2d');

        const lineChart = new Chart(context, config);

        const source = new EventSource("/canvas-data");
        source.onmessage = function (event) {
            const data = JSON.parse(event.data);
        
            config.data.labels.push(data.time);
            config.data.datasets[0].data.push(data.value0);
            config.data.datasets[1].data.push(data.value1);
            config.data.datasets[2].data.push(data.value2);
            lineChart.update();
            console.log("ax= ",data.value0, " ay= ", data.value1, " az= ", data.value2);
        }
    });
