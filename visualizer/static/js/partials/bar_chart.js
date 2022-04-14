
// 3rd party
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Tooltip, BarElement, CategoryScale } from 'chart.js'

// Internal
import htmlTemplate from "~/visualizer/templates/partials/bar_chart.html"

// TODO: comment
ChartJS.register(Tooltip, BarElement, CategoryScale)

// TODO: Rename to HubSpokeGraph?
const BarChart = {
    delimiters: ['${', '}'],
    template: htmlTemplate,
    components: {
        Bar,
    },
    props: [
        'chartData',
    ],

    //
    // -- Initial state
    //

    data() {
        return {
            // chartData: {
            //     labels: [ 'January', 'February', 'March' ],
            //     datasets: [ { data: [40, 20, 12] } ],
            // },
        }
    },

    //
    // -- Lifecycle hooks
    //

    created: function() {
    },

    //
    // -- Computed properties
    //

    computed: {
        chartOptions() {
            return {
                plugins: {
                    legend: {
                      display: false,
                    },
                },
                responsive: false, // don't resize to display; data will easily become unreadable
                scales: {
                    x: {
                        type: 'category',
                        ticks: {
                            autoSkip: false,
                        },
                    },
                },
                onClick: this.handleChartClick,
            }
        },
        width() {
            return 100 + (this.chartData.labels.length * 25)
        },
        height() {
            return 800
        },
    },

    // 
    // -- Watchers
    // 

    watch: {
    },

    // 
    // -- Methods
    // 

    methods: {
        emitChartClick(vizId) {
                 
        },
        handleChartClick(event, activeElements, chart) {
            // If there is an active chart element, use its index to unpack the chart dataset
            if (activeElements[0]) {
                let elemIdx = activeElements[0].index
                let vizId = chart.data.datasets[0].vizIds[elemIdx]
                // Emit signal to parent component
                this.$emit('chart-click', vizId)
            }
        },
    },
}

export default BarChart