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
@font-face {
  font-family: 'Poppins';
  src: url('./assets/fonts/Poppins-Regular.woff') format('woff');
  font-weight: normal;
}

@import '../node_modules/bulma'
</style>

<style>
.hero-body {
  background-image: url("./assets/background_img.svg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  height: 100vh;

}

html {
  height: auto;
}
</style>