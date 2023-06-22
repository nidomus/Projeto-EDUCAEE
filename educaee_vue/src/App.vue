<template>
  <div>
    <section class="hero is-fullheight">
      <div class="hero-body">
        <router-view />
      </div>
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

<style>
body {
  background-image: url("./assets/plano_de_fundo.jpeg");
  background-size: cover;
  height: 100vh;

}

html {
  height: auto;
}
</style>