function fetch_url(url) {
    console.log(url)
    // console.log("!!!Teste JS!!!")
    // console.log(data)
    return fetch(url, { method: "get" }).then(data => data.json())
}

async function ocs_pie_cpu(url) {
    const data = await fetch_url(url)

    const ctx = document.getElementById('ocs_pie_cpu').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.cpu_labels,
            datasets: [
                {
                    label: "Estações de Trabalho por CPU",
                    data: data.cpu_counts,
                    backgroundColor: [
                        '#86cbf9',
                        '#7fe686',
                        '#ffe97f',
                        '#fe7167',
                    ],
                    borderColor: [
                        '#0b97f4',
                        '#2ad535',
                        '#ffd500',
                        '#fe1201',
                    ],
                    borderWidth: 1
                },
            ]

        },
    });
}

async function ocs_pie_memory(url) {
    const data = await fetch_url(url)

    const ctx = document.getElementById('ocs_pie_memory').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.memory_labels,
            datasets: [
                {
                    label: "Estações de Trabalho por Memória",
                    data: data.memory_counts,
                    backgroundColor: [
                        '#86cbf9',
                        '#7fe686',
                        '#ffe97f',
                        '#fe7167',
                    ],
                    borderColor: [
                        '#0b97f4',
                        '#2ad535',
                        '#ffd500',
                        '#fe1201',
                    ],
                    borderWidth: 1
                },
            ]

        },
    });
}

async function ocs_bar_manufacturer(url) {
    const data = await fetch_url(url)

    const ctx = document.getElementById('ocs_bar_manufacturer').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.manufacturer_labels,
            datasets: [
                {
                    axis: "y",
                    label: "Quantidade",
                    data: data.manufacturer_counts,
                    backgroundColor: [
                        '#86cbf9',
                    ],
                    borderColor: [
                        '#0b97f4',
                    ],
                    borderWidth: 1
                },
            ]

        },
        options: {
            indexAxis: 'y',
            scales: {
                yAxes: [{
                    ticks: {
                        min: 0,
                        max: 120,
                        callback: function (value) { return value + "%" }
                    },
                    scaleLabel: {
                        display: true,
                        labelString: "Percentage"
                    }
                }]
            }
        }

    });
}


async function bar_ocs_department_cpu(url) {
    const data = await fetch_url(url)
    // console.log(data)

    const ctx = document.getElementById('bar_ocs_department_cpu').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.departments,
            datasets: [
                {
                    label: data.cpu_labels[0],
                    data: data.cpu_core_i7_counts_all_departments,
                    backgroundColor: [
                        '#86cbf9',
                    ],
                    borderColor: [
                        '#0b97f4',
                    ],
                    borderWidth: 1
                },
                {
                    label: data.cpu_labels[1],
                    data: data.cpu_core_i5_counts_all_departments,
                    backgroundColor: [
                        '#7fe686',
                    ],
                    borderColor: [
                        '#2ad535',
                    ],
                    borderWidth: 1
                },
                {
                    label: data.cpu_labels[2],
                    data: data.cpu_core_i3_counts_all_departments,
                    backgroundColor: [
                        '#ffe97f',
                    ],
                    borderColor: [
                        '#ffd500',
                    ],
                    borderWidth: 1
                },
                {
                    label: data.cpu_labels[3],
                    data: data.cpu_core_dual_counts_all_departments,
                    backgroundColor: [
                        '#fe7167',
                    ],
                    borderColor: [
                        '#fe1201',
                    ],
                    borderWidth: 1
                },
            ]
        },
    });
}

async function bar_ocs_department_memory(url) {
    const data = await fetch_url(url)
    // console.log(data)

    const ctx = document.getElementById('bar_ocs_department_memory').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.departments_labels,
            datasets: [
                {
                    label: data.ranking_labels[0],
                    data: data.ranking_a,
                    backgroundColor: [
                        '#86cbf9',
                    ],
                    borderColor: [
                        '#0b97f4',
                    ],
                    borderWidth: 1
                },
                {
                    label: data.ranking_labels[1],
                    data: data.ranking_b,
                    backgroundColor: [
                        '#7fe686',
                    ],
                    borderColor: [
                        '#2ad535',
                    ],
                    borderWidth: 1
                },
                {
                    label: data.ranking_labels[2],
                    data: data.ranking_c,
                    backgroundColor: [
                        '#ffe97f',
                    ],
                    borderColor: [
                        '#ffd500',
                    ],
                    borderWidth: 1
                },
                {
                    label: data.ranking_labels[3],
                    data: data.ranking_d,
                    backgroundColor: [
                        '#fe7167',
                    ],
                    borderColor: [
                        '#fe1201',
                    ],
                    borderWidth: 1
                },
            ]
        },
    });
}