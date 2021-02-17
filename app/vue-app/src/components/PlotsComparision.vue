<template>
    <div>
        <label for="type">Choose plots type:  </label>
        <select name="type" id="selecttype" v-model="type">
            <option value="Posts number in time">Posts number in time</option>
            <option value="Reactions number in time">Reactions number in time</option>
            <option value="Mentions number in time">Mentions number in time</option>
            <option value="Posts polarity in time">Posts polarity in time</option>
            <option value="Mentions polarity in time">Mentions polarity in time</option>
            <option value="Posts number in day scope">Posts number in day scope</option>
            <option value="Posts number in week scope">Posts number in week scope</option>
        </select>
    </div>
    <div>
        <!-- 
        <PlotPostsDay v-bind:party="party" />
        <PlotPostsWeek v-bind:party="party" /> -->
        <div v-if="type == 'Posts number in time'">
            <div v-bind:key="party" v-for="party in parties">
                <PlotPosts v-bind:party="party" v-bind:title="party" v-bind:pid="party" />
            </div>
        </div>

        <div v-if="type == 'Reactions number in time'">
            <div v-bind:key="party" v-for="party in parties">
                <PlotReactions v-bind:party="party" v-bind:title="party" v-bind:pid="party" />
            </div>
        </div>

        <div v-if="type == 'Mentions number in time'">
            <div v-bind:key="party" v-for="party in parties">
                <PlotMentions v-bind:party="party" v-bind:title="party" v-bind:pid="party" />
            </div>
        </div>

        <div v-if="type == 'Posts polarity in time'">
            <div v-bind:key="party" v-for="party in parties">
                <PlotPostsPolarity v-bind:party="party" v-bind:title="party" v-bind:pid="party" />
            </div>
        </div>

        <div v-if="type == 'Mentions polarity in time'">
            <div v-bind:key="party" v-for="party in parties">
                <PlotMentionsPolarity v-bind:party="party" v-bind:title="party" v-bind:pid="party" />
            </div>
        </div>

        <div v-if="type == 'Posts number in day scope'">
            <div v-bind:key="party" v-for="party in parties">
                <PlotPostsDay v-bind:party="party" v-bind:title="party" v-bind:pid="party" />
            </div>
        </div>

        <div v-if="type == 'Posts number in week scope'">
            <div v-bind:key="party" v-for="party in parties">
                <PlotPostsWeek v-bind:party="party" v-bind:title="party" v-bind:pid="party" />
            </div>
        </div>

    </div>
</template>

<script>
import PlotPosts from './PlotPosts'
import PlotReactions from './PlotReactions'
import PlotMentions from './PlotMentions'
import PlotPostsPolarity from './PlotPostsPolarity'
import PlotMentionsPolarity from './PlotMentionsPolarity'
import PlotPostsDay from './PlotPostsDay'
import PlotPostsWeek from './PlotPostsWeek'
export default {
    name: "PlotsParty",
    components: {
        PlotPosts,
        PlotReactions,
        PlotMentions,
        PlotPostsPolarity,
        PlotMentionsPolarity,
        PlotPostsDay,
        PlotPostsWeek
    },
    data() {
        return {
            parties: [
                "pisorgpl",
                "Porozumienie__",
                "SolidarnaPL",
                "platforma_org",
                "Nowoczesna",
                "Zieloni",
                "inicjatywaPL",
                "KONFEDERACJA_",
                "RuchNarodowy",
                "Partia_KORWiN",
                "nowePSL",
                "KUKIZ15",
                "__Lewica",
                "partiarazem",
            ],
            type: 'Posts number in time'
        }
    }
}
</script>

<style scoped>

</style>