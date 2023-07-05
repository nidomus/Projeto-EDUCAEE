<template>
    <div class="container">
        <div class="columns is-multiline is-centered">
            <div class="column is-12">
                <div class="level-item">
                    <br>
                    <h1 class="is-size-1 titulo">Olá, seja bem-vindo(a) </h1>
                </div>

            </div>

            <div :class="`column is-6-desktop is-12-touch`">
                <div class=" box p-6  form-box">

                    <form @submit.prevent="submitForm">

                        <div class="field">
                            <label class="label">Usuário:</label>
                            <div class="control">
                                <input class="input is-medium" type="text" name="text" placeholder='Insira seu usuário'
                                    required v-model="username">

                            </div>
                        </div>

                        <div class="field pt-5">
                            <label class="label">Senha:</label>
                            <div class="control">
                                <input class="input is-medium" placeholder="Insira sua senha" type="password"
                                    name="password1" required v-model="password">

                            </div>
                        </div>

                        <br>
                        <div class="notification is-danger is-light" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>

                        <div class="field ">
                            <div class="control">
                                <div class="buttons full-width is-right">
                                    <button class="button is-medium" :class="{ 'is-loading': this.carregando }"
                                        id="btn-entrar">Logar</button>
                                </div>
                            </div>

                        </div>

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
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)

                    axios.defaults.headers.common['Authorization'] = 'Token ' + token

                    localStorage.setItem('token', token)
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

                        this.$store.commit('setUser', { 'id': response.data.id, 'username': response.data.username })

                        localStorage.setItem('username', response.data.username)
                        localStorage.setItem('userid', response.data.id)

                    })
                    .catch(error => {

                        console.log(error)

                    })


                // this.$store.commit('setIsLoading', true)
                this.$router.push('/painel/')

            }

            this.error = true
            this.username = ''
            this.password = ''
            this.carregando = false

        }
    }
}

</script>

<style>
.label {
    font-family: Poppins;
    font-size: large;
    z-index: 99999;
}

.form-box {
    background-color: rgb(255, 255, 255, 0.85);
    border-radius: 20px;
    z-index: -999999;
}

.titulo {

    font-family: Poppins;
    color: #FF4D00;
    font-weight: bolder;
}

#btn-entrar {
    background-color: #40A403;
    color: white;
    font-family: Poppins;
}
</style>