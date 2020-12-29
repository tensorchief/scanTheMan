<template>
  <b-button target="_blank" v-bind:href="scan">{{ title }}</b-button>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ScanButton',
  props: ['title'],
  computed: {
    scan () {
      return `${axios.defaults.baseURL}api/v1.0/scan?r=${new Date().getTime()}`
    }
  }
}
</script>

<style scoped>

</style>
