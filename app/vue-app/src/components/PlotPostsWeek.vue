<template>
    <div v-bind:id="'postsweek-'+pid" class="plot"></div>
</template>

<script>
import Plotly from 'plotly.js-dist'

function renderPlot(tweets, retweets, title, plot_id) {
    Plotly.newPlot(
        document.getElementById(plot_id),
        [
            {
                x: Object.keys(tweets.week_day).map(function (key) { return tweets.week_day[key]; }),
                y: Object.keys(tweets.id).map(function (key) { return tweets.id[key]; }),
                stackgroup: 'one',
                name: 'Tweets'
            },
            {
                x: Object.keys(retweets.week_day).map(function (key) { return retweets.week_day[key]; }),
                y: Object.keys(retweets.id).map(function (key) { return retweets.id[key]; }),
                stackgroup: 'one',
                name: 'Retweets'
            }
        ],
        {
            title: title,
            xaxis: {
                title: 'Week day',
                tickmode: 'array',
                tickvals: [0, 1, 2, 3, 4, 5, 6],
                ticktext: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
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
    name: "PlotPostsWeek",
    props: ["party", "title", "pid"],
    mounted() {
        var tweets = require('../data/'+this.party+'_tweets_week.json')
        var retweets = require('../data/'+this.party+'_retweets_week.json')
        var plot_id = 'postsweek-'+this.pid
        renderPlot(tweets, retweets, this.title, plot_id)
    },
    watch: {
        party: function update() {
            var tweets = require('../data/'+this.party+'_tweets_week.json')
            var retweets = require('../data/'+this.party+'_retweets_week.json')
            var plot_id = 'postsweek-'+this.pid
            renderPlot(tweets, retweets, this.title, plot_id)
        }
    }
}
</script>

<style scoped>

</style>