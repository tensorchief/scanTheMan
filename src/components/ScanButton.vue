<template>
  <b-form>
    <b-form-group label="Source:" label-for="source">
      <b-form-select id="source" v-model="opts.source" :options="sources" required/>
    </b-form-group>
    <b-button target="_blank" v-bind:href="scan">{{ title }}</b-button>
  </b-form>

</template>

<script>
import axios from 'axios'

export default {
  name: 'ScanButton',
  props: ['title'],
  computed: {
    scan () {
      return `${axios.defaults.baseURL}api/v1.0/scan` +
        `?r=${new Date().getTime()}` +
        `&source=${this.opts.source}`
    }
  },
  mounted: function () {
    axios.get('/api/options').then(response => {
      this.sources = response.data.sources
      this.opts.source = response.data.sources[0].value
    })
  },
  data: function () {
    return {
      sources: undefined,
      opts: {
        source: null
      }
    }
  }
}
</script>

<style scoped>

</style>
