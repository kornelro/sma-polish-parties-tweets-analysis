<template>
    <div v-bind:id="'posts-'+pid" class="plot"></div>
</template>

<script>
import Plotly from 'plotly.js-dist'

function renderPlot(tweets, retweets, title, plot_id) {
    Plotly.newPlot(
            document.getElementById(plot_id),
            [
                {
                    x: Object.keys(tweets.date).map(function (key) { return tweets.date[key]; }),
                    y: Object.keys(tweets.id).map(function (key) { return tweets.id[key]; }),
                    stackgroup: 'one',
                    name: 'Tweets'
                },
                {
                    x: Object.keys(retweets.date).map(function (key) { return retweets.date[key]; }),
                    y: retweets.id ? Object.keys(retweets.id).map(function (key) { return retweets.id[key]; })
                        : Object.keys(retweets.retweets).map(function (key) { return retweets.retweets[key]; }),
                    stackgroup: 'one',
                    name: 'Retweets'
                }
            ],
            {
                title: title,
                xaxis: {
                    title: 'Date'
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
    name: "PlotPosts",
    props: ["party", "title", "pid"],
    mounted() {
        var tweets = require('../data/'+this.party+'_tweets_num.json')
        var retweets = require('../data/'+this.party+'_posted_retweets_num.json')
        var plot_id = "posts-"+this.pid
        renderPlot(tweets, retweets, this.title, plot_id)
    },
    watch: {
        party: function update() {
            var tweets = require('../data/'+this.party+'_tweets_num.json')
            var retweets = require('../data/'+this.party+'_posted_retweets_num.json')
            var plot_id = "posts-"+this.pid
        renderPlot(tweets, retweets, this.title, plot_id)
        }
    }
}
</script>

<style scoped>

</style>