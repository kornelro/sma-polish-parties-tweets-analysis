<template>
    <div v-bind:id="'mentionspolarity-'+pid"  class="plot"></div>
</template>

<script>
import Plotly from 'plotly.js-dist'

function renderPlot(tweets, title, plot_id) {
    Plotly.newPlot(
        document.getElementById(plot_id),
        [
            {
                x: Object.keys(tweets),
                y: Object.keys(tweets).map(function (key) { return tweets[key]; }),
                name: 'Tweets'
            }
        ],
        {
            title: title,
            xaxis: {
                title: 'Date'
            },
            yaxis: {
                title: 'Polarity',
                range: [-1.2,1.2]
            },
            height: 300,
            legend: {
                orientation: 'h',
                x:0.1,
                y:1.2
            }
        }
    )
}

function sortOnKeys(dict) {

    var sorted = [];
    for(var key in dict) {
        sorted[sorted.length] = key;
    }
    sorted.sort();

    var tempDict = {};
    for(var i = 0; i < sorted.length; i++) {
        tempDict[sorted[i]] = dict[sorted[i]];
    }

    return tempDict;
}

function getDatePolarityDict(dict) {

    var date = Object.keys(dict.date).map(function (key) { return dict.date[key]; })
    var polarity = Object.keys(dict.polarity).map(function (key) { return dict.polarity[key]; })
    var new_dict = {}
    date.forEach((key, i) => new_dict[key] = polarity[i]);

    return sortOnKeys(new_dict)
}

export default {
    name: "PlotPostsPolarity",
    props: ["party", "title", "pid"],
    mounted() {
        var tweets = require('../data/'+this.party+'_mentions_polarity.json')
        tweets = getDatePolarityDict(tweets)
        var plot_id = 'mentionspolarity-'+this.pid
        renderPlot(tweets, this.title, plot_id)
    },
    watch: {
        party: function update() {
            var tweets = require('../data/'+this.party+'_mentions_polarity.json')
            tweets = getDatePolarityDict(tweets)
            var plot_id = 'mentionspolarity-'+this.pid
            renderPlot(tweets, this.title, plot_id)
        }
    }
}
</script>

<style scoped>

</style>