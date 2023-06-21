<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title"> Sign up</h1>

                <form @submit.prevent="submitForm">

                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" name="email" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Senha</label>
                        <div class="control">
                            <input type="password" name="password1" class="input" v-model="password1">
                        </div>
                    </div>

                    <div class="field">
                        <label>Repita sua Senha</label>
                        <div class="control">
                            <input type="password" name="password2" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger is-light" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Cadastrar</button>
                        </div>
                    </div>

                </form>

            </div>


        </div>


    </div>
</template>



<script>
import axios from 'axios';
import { toast } from 'bulma-toast'

export default {
    name: "CadastrarAluno",
    data() {
        return {
            username: '',
            password1: '',
            password2: '',
            errors: []
        }
    },
}
</script>