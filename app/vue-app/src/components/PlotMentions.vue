<template>
    <div v-bind:id="'mentions-'+pid" class="plot"></div>
</template>

<script>
import Plotly from 'plotly.js-dist'

function renderPlot(mentions, title, plot_id) {
    Plotly.newPlot(
        document.getElementById(plot_id),
        [
            {
                x: Object.keys(mentions.date).map(function (key) { return mentions.date[key]; }),
                y: Object.keys(mentions.id).map(function (key) { return mentions.id[key]; }),
                stackgroup: 'one',
                name: 'Mentions'
            }
        ],
        {
            title: title,
            xaxis: {
                title: 'Date'
            },
            yaxis: {
                title: 'Mentions number'
            },
            height: 300,
        }
    )
}

export default {
    name: "PlotMentions",
    props: ["party", "title", "pid"],
    mounted() {
        var mentions = require('../data/'+this.party+'_mentions_num.json')
        var plot_id = "mentions-"+this.pid
        renderPlot(mentions, this.title, plot_id)
    },
    watch: {
        party: function update() {
            var mentions = require('../data/'+this.party+'_mentions_num.json')
            var plot_id = "mentions-"+this.pid
            renderPlot(mentions, this.title, plot_id)
        }
    }
}
</script>

<style scoped>
    
</style>