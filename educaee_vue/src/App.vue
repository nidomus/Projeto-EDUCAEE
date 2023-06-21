<template>
  <div class="container">
    <section class="section">
      <router-view />
    </section>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',

  beforeCreate() {
    this.$store.commit('initializeStore')

    if (this.$store.state.token) {
      axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
}
</script>
<!-- Importando o CSS Bulma para o projeto -->
<style lang="scss">
@import '../node_modules/bulma'
</style>
