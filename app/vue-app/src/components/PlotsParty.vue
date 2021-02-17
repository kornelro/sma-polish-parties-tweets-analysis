<template>
    <div>
        <div>
            <label for="parties">Choose Twitter account:  </label>
            <select name="parties" id="selectparty" v-model="party">
                <option value="pisorgpl">pisorgpl</option>
                <option value="Porozumienie__">Porozumienie__</option>
                <option value="SolidarnaPL">SolidarnaPL</option>
                <option value="platforma_org">platforma_org</option>
                <option value="Nowoczesna">Nowoczesna</option>
                <option value="Zieloni">Zieloni</option>
                <option value="inicjatywaPL">inicjatywaPL</option>
                <option value="KONFEDERACJA_">KONFEDERACJA_</option>
                <option value="RuchNarodowy">RuchNarodowy</option>
                <option value="Partia_KORWiN">Partia_KORWiN</option>
                <option value="nowePSL">nowePSL</option>
                <option value="KUKIZ15">KUKIZ15</option>
                <option value="__Lewica">__Lewica</option>
                <option value="partiarazem">partiarazem</option>
            </select>
        </div>
        <div>
            <PlotPosts v-bind:party="party" v-bind:title="'Posts number in time'" v-bind:pid="''" />
            <PlotReactions v-bind:party="party" v-bind:title="'Reactions number in time'" v-bind:pid="''" />
            <PlotMentions v-bind:party="party" v-bind:title="'Mentions number in time'" v-bind:pid="''" />
            <PlotPostsPolarity v-bind:party="party" v-bind:title="'Posts polarity in time'" v-bind:pid="''" />
            <PlotMentionsPolarity v-bind:party="party" v-bind:title="'Mentions number in time'" v-bind:pid="''" />
            <PlotPostsDay v-bind:party="party" v-bind:title="'Posts number in day scope'" v-bind:pid="''" />
            <PlotPostsWeek v-bind:party="party" v-bind:title="'Posts number in week scope'" v-bind:pid="''" />
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
            party: 'pisorgpl'
        }
    }
}
</script>

<style scoped>

</style>