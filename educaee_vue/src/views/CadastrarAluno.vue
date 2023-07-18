<template>
    <div class="container">
        <div class="columns is-centered is-multiline is-scrollable">

            <div class="column is-12">
                <div class="box" style="background-color: #FFE600; border-radius: 20px;">
                    <div class="columns is-centered is-vcentered">
                        <div class="column is-one-fifth mr-0 pr-0">
                            <div class="buttons is-left">
                                <button class="button is-success is-rounded is-medium"
                                    @click="this.$router.push('/painel')">Painel</button>
                            </div>
                        </div>
                        <div class="column is-three-fifths pr-0">
                            <h1 id="titulo" class="is-size-1 ml-6 pl-5 has-text-centered"><strong>ADICIONAR ALUNO</strong>
                            </h1>
                        </div>

                        <div class="column is-one-fifth pl-0">
                            <div class="buttons is-right">
                                <button class="button is-danger is-rounded is-medium" @click="logout()">Sair</button>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <div class="column is-12">

                <div class="box p-6" id="box-add">

                    <form @submit.prevent="submitForm" class="p-4  is-scrollable">

                        <div class="columns">

                            <div class="column is-12">
                                <div class="columns">

                                    <div class="column is-narrow pr-10">
                                        <div>
                                            <img id="profile_pic" :src="`${foto_aluno}`">
                                        </div>
                                        <br>

                                        <div class="file is-dark is-centered">
                                            <label class="file-label">
                                                <input class="file-input" type="file" name="resume" id="foto_aluno"
                                                    v-on:change="salvar_foto">
                                                <span class="file-cta">
                                                    <span class="file-icon">
                                                        <font-awesome-icon icon="camera" />
                                                    </span>
                                                    <span class="file-label">
                                                        Escolha uma foto
                                                    </span>
                                                </span>
                                            </label>
                                        </div>

                                    </div>

                                    <div class="column is-8">
                                        <div class="columns is-multiline">
                                            <div class="column is-12">
                                                <div class="field ">
                                                    <div class="control">
                                                        <label class="label has-text-light">Nome completo do Aluno* </label>
                                                        <input type="text" width="40" class="input" v-model="nome">

                                                    </div>
                                                </div>
                                            </div>

                                            <div class="column is-narrow">
                                                <div class="field">
                                                    <label class="label has-text-light">Data de nascimento*</label>
                                                    <div class="control">
                                                        <input type="date" class="input" v-model="password1">
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="column is-narrow">
                                                <div class="field ">
                                                    <label class="label has-text-light">Sexo*</label>
                                                    <div class="control ">
                                                        <div class="select">
                                                            <select>
                                                                <option>F</option>
                                                                <option>M</option>
                                                            </select>
                                                        </div>
                                                    </div>

                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                            </div>
                        </div>

                        <div class="columns is-vcentered is-centered">
                            <div class="column is-8">
                                <div class="field">
                                    <label class="label has-text-light">Escola de Origem*</label>
                                    <div class="control">
                                        <input type="text" name="password2" class="input">
                                    </div>
                                </div>
                            </div>

                            <div class="column is-2 is-narrow">
                                <div class="field">
                                    <label class="label has-text-light">Ano/Série</label>
                                    <div class="control ">
                                        <div class="select">
                                            <select>
                                                <option>-----</option>
                                                <option>5º ano</option>
                                                <option>6º ano</option>
                                                <option>7º ano</option>
                                            </select>
                                        </div>
                                    </div>

                                </div>
                            </div>
                            <div class="column is-2">
                                <div class="field">
                                    <label class="label has-text-light">Turma</label>
                                    <div class="control">
                                        <div class="select">
                                            <select>
                                                <option>-----</option>
                                                <option>A</option>
                                                <option>B</option>
                                                <option>C</option>
                                            </select>
                                        </div>
                                    </div>

                                </div>
                            </div>
                        </div>
                        <div class="columns">
                            <div class="column is-10">
                                <div class="field">
                                    <label class="label has-text-light">Nome completo do responsável*</label>
                                    <div class="control">
                                        <input type="text" name="password2" class="input">
                                    </div>
                                </div>
                            </div>

                            <div class="column is-2">
                                <div class="field">
                                    <div class="field">
                                        <label class="label has-text-light">Parentesco</label>
                                        <div class="control">
                                            <input type="text" name="password2" class="input">
                                        </div>
                                    </div>

                                </div>
                            </div>
                        </div>
                        <div class="notification is-danger is-light" v-if="errors.length">
                            <p v-for=" error  in  errors " v-bind:key="error">{{ error }}</p>
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
    </div>
</template>



<script>
import axios from 'axios';
import imagem_padrao from '../assets/aluna.png'
import { toast } from 'bulma-toast'

export default {
    name: "CadastrarAluno",
    data() {
        return {
            username: '',
            password1: '',
            password2: '',
            errors: [],
            foto_aluno: imagem_padrao
        }
    },

    methods: {

        salvar_foto(event) {
            console.log(event.target.files)
            this.foto_aluno = event.target.files[0]
        }

    }
}
</script>

<style>
.is-scrollable {
    display: flex;
    overflow-y: visible;
    flex-direction: column;
}

#profile_pic {

    border: 10px solid black;
    background-color: white;
    padding: auto;

    border-radius: 50%;

}

#box-add {
    border: 5px solid black;
    background-color: #FF00F5;
    border-radius: 20px;
    color: white;

}
</style>
