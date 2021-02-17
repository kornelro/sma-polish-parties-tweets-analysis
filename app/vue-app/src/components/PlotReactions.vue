<template>
    <div v-bind:id="'reactions-'+pid" class="plot"></div>
</template>

<script>
import Plotly from 'plotly.js-dist'

function renderPlot(likes, replies, retweets, title, plot_id) {
    Plotly.newPlot(
        document.getElementById(plot_id),
        [
            {
                x: Object.keys(likes.date).map(function (key) { return likes.date[key]; }),
                y: Object.keys(likes.likes).map(function (key) { return likes.likes[key]; }),
                stackgroup: 'one',
                name: 'Likes'
            },
            {
                x: Object.keys(replies.date).map(function (key) { return replies.date[key]; }),
                y: Object.keys(replies.replies).map(function (key) { return replies.replies[key]; }),
                stackgroup: 'one',
                name: 'Replies'
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
                title: 'Reactions number'
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
    name: "PlotReactions",
    props: ["party", "title", "pid"],
    mounted() {
        var likes = require('../data/'+this.party+'_likes_num.json')
        var replies = require('../data/'+this.party+'_replies_num.json')
        var retweets = require('../data/'+this.party+'_retweets_num.json')
        var plot_id = "reactions-"+this.pid
        renderPlot(likes, replies, retweets, this.title, plot_id)
    },
    watch: {
        party: function update() {
            var likes = require('../data/'+this.party+'_likes_num.json')
            var replies = require('../data/'+this.party+'_replies_num.json')
            var retweets = require('../data/'+this.party+'_retweets_num.json')
            var plot_id = "reactions-"+this.pid
            renderPlot(likes, replies, retweets, this.title, plot_id)
        }
    }
}
</script>

<style scoped>

</style>