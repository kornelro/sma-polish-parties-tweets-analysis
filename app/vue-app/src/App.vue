<template>
  <div>
    <Header />
    <Menu v-on:change-mode="changeMode"/>
    <PlotsParty v-if="!plotsPartyHidden" v-bind:party="party" />
    <PlotsComparision v-if="!plotsComaperisionHidden" />
  </div>
</template>

<script>
import Header from './components/layout/Header.vue'
import Menu from './components/layout/Menu.vue'
import PlotsParty from './components/PlotsParty.vue'
import PlotsComparision from './components/PlotsComparision'

export default {
  name: 'App',
  components: {
    Header,
    Menu,
    PlotsParty,
    PlotsComparision
  },
  data() {
    return {
      plotsPartyHidden: false,
      plotsComaperisionHidden: true
    }
  },
  methods: {
    changeMode() {
      this.plotsPartyHidden = !this.plotsPartyHidden
      this.plotsComaperisionHidden = !this.plotsComaperisionHidden
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.plot {
  margin-left: 15%;
  margin-right: 15%;
  padding: 0;
}
</style>
