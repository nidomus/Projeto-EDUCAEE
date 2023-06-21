<template>
    <div class="container">

        <br>
        <br>

        <div class="columns is-multiline is-centered">
            <div class="column is-12">
                <div class="level-item">
                    <br>
                    <span class="is-size-1">Login do Professor</span>
                </div>

            </div>

            <div :class="`column is-5-desktop is-12-touch`">
                <div class=" box p-6  form-box">

                    <form @submit.prevent="submitForm">

                        <div class="field">
                            <label class="form-label">Usuário</label>
                            <div class="control">
                                <input type="text" name="text" placeholder='' required class="input" v-model="username">

                            </div>
                        </div>

                        <div class="field">
                            <label class="form-label">Senha</label>
                            <div class="control">
                                <input type="password" name="password1" required class="input" v-model="password">

                            </div>
                        </div>

                        <br>
                        <div class="notification is-danger is-light" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>

                        <div class="level-item">
                            <div class="field is-centered">
                                <div class="control">
                                    <button class="button is-success" :class="{ 'is-loading': this.carregando }"
                                        id="btn-entrar">Entrar</button>
                                </div>
                            </div>
                        </div>
                        <br>


                    </form>

                </div>
            </div>

        </div>


    </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast'

export default {
    name: "LogIn",
    data() {
        return {
            username: '',
            password: '',
            errors: [],
            error: true,

            user: {
                id: '',
                nome: '',
            },
            token: '',
            carregando: false


        }
    },
    mounted() {
        if (this.$store.state.isAuthenticated) {
            this.$router.back()
        }
    },
    methods: {
        async submitForm() {

            this.carregando = true
            this.errors = []

            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post('/api/v1/token/login/', formData)

                .then(response => {
                    this.token = response.data.auth_token
                    axios.defaults.headers.common['Authorization'] = 'Token ' + this.token
                    console.log('aqui')
                })
                .catch(error => {
                    if (error.response) {
                        this.error = true

                        this.errors.push('Usuário ou Senha incorreto(s)')

                    } else {
                        this.error = true
                        this.errors.push('Algo deu errado. Tente novamente!')
                    }
                })
            if (this.errors.length == 0) {

                await axios
                    .get('/api/v1/users/me')
                    .then(response => {

                        this.user.nome = response.data.username
                        this.user.id = response.data.id

                    })
                    .catch(error => {

                        console.log(error)

                    })

                this.$store.commit('setToken', this.token) // Chama os métodos guardados no Mutations do index.js

                localStorage.setItem('token', this.token)

                this.$store.commit('setUser', { 'id': this.user.id, 'username': this.user.nome })

                localStorage.setItem('username', this.user.nome)
                localStorage.setItem('userid', this.user.id)

                this.$store.commit('setIsLoading', true)
                this.$router.push('/alunos/')

            }

            this.error = true
            this.username = ''
            this.password = ''
            this.carregando = false

        }
    }
}

</script>

<style></style>