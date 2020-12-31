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
      return `${axios.defaults.baseURL}api/v1.0/scan?r=${new Date().getTime()}`
    }
  },
  data: function () {
    return {
      sources: [
        { value: null, text: 'Select one' },
        { value: 'ADF Duplex', text: 'duplex' },
        { value: 'ADF Front', text: 'front' }
      ],
      opts: {
        source: null
      }
    }
  }
}
</script>

<style scoped>

</style>
