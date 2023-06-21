<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view />
</template>


<!-- Importando o CSS Bulma para o projeto -->
<style lang="scss">
@import '../node_modules/bulma'
</style>
