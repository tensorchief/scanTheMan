<template>
  <a target="_blank" v-bind:href="scan">{{ title }}</a>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ScanButton',
  props: ['title'],
  computed: {
    scan () {
      return `${axios.defaults.baseURL}api/v1.0/scan`
    }
  }
}
</script>

<style scoped>

</style>
