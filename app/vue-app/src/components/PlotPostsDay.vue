<template>
    <div v-bind:id="'postsday-'+pid" class="plot"></div>
</template>

<script>
import Plotly from 'plotly.js-dist'

function renderPlot(tweets, retweets, title, plot_id) {
    Plotly.newPlot(
        document.getElementById(plot_id),
        [
            {
                x: Object.keys(tweets.hour).map(function (key) { return tweets.hour[key]; }),
                y: Object.keys(tweets.id).map(function (key) { return tweets.id[key]; }),
                stackgroup: 'one',
                name: 'Tweets'
            },
            {
                x: Object.keys(retweets.hour).map(function (key) { return retweets.hour[key]; }),
                y: Object.keys(retweets.id).map(function (key) { return retweets.id[key]; }),
                stackgroup: 'one',
                name: 'Retweets'
            }
        ],
        {
            title: title,
            xaxis: {
                title: 'Hour'
            },
            yaxis: {
                title: 'Posts number'
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

export default {
    name: "PlotPostsDay",
    props: ["party", "title", "pid"],
    mounted() {
        var tweets = require('../data/'+this.party+'_tweets_day.json')
        var retweets = require('../data/'+this.party+'_retweets_day.json')
        var plot_id = 'postsday-'+this.pid
        renderPlot(tweets, retweets, this.title, plot_id)
    },
    watch: {
        party: function update() {
            var tweets = require('../data/'+this.party+'_tweets_day.json')
            var retweets = require('../data/'+this.party+'_retweets_day.json')
            var plot_id = 'postsday-'+this.pid
            renderPlot(tweets, retweets, this.title, plot_id)
        }
    }
}
</script>

<style scoped>

</style>