<template>
  <div id="app">
    <b-container fluid>
      <b-row>
        <b-col cols="6">
          <b-img alt="Logo" :src="require('./assets/Octocat.png')" fluid></b-img>
        </b-col>
        <b-col cols="6">
          <ScanButton title="Scan"/>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import ScanButton from './components/ScanButton.vue'

export default {
  name: 'App',
  components: {
    ScanButton
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
