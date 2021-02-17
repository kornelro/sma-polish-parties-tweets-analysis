<template>
    <div v-bind:id="'postspolarity-'+pid" class="plot"></div>
</template>

<script>
import Plotly from 'plotly.js-dist'

function renderPlot(tweets, retweets, title, plot_id) {
    Plotly.newPlot(
        document.getElementById(plot_id),
        [
            {
                x: Object.keys(tweets),
                y: Object.keys(tweets).map(function (key) { return tweets[key]; }),
                name: 'Tweets',
            },
            {
                x: Object.keys(retweets),
                y: Object.keys(retweets).map(function (key) { return retweets[key]; }),
                name: 'Retweets',
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
        var tweets = require('../data/'+this.party+'_tweets_polarity.json')
        tweets = getDatePolarityDict(tweets)
        var retweets = require('../data/'+this.party+'_retweets_polarity.json')
        retweets = getDatePolarityDict(retweets)
        var plot_id = 'postspolarity-'+this.pid
        renderPlot(tweets, retweets, this.title, plot_id)
    },
    watch: {
        party: function update() {
            var tweets = require('../data/'+this.party+'_tweets_polarity.json')
            tweets = getDatePolarityDict(tweets)
            var retweets = require('../data/'+this.party+'_retweets_polarity.json')
            retweets = getDatePolarityDict(retweets)
            var plot_id = 'postspolarity-'+this.pid
            renderPlot(tweets, retweets, this.title, plot_id)
        }
    }
}
</script>

<style scoped>

</style>