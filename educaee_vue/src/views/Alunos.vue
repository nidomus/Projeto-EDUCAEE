<template>
    <div class="container">

        <div class="columns is-centered is-multiline">

            <div class="column is-12">
                <div class="box">
                    <h1 class="title is-size-1 has-text-centered">Alunos</h1>
                </div>
            </div>

            <div class="column is-12">



            </div>

            <div class='column is-12'>
                <div class="box">
                    <div class="table-container">

                        <table class="table is-fullwidth">

                            <thead>

                                <th><span class="is-size-4">Nome</span></th>
                                <th><span class="is-size-4">Idade</span></th>
                                <th><span class="is-size-4">Ano</span></th>
                                <th><span class="is-size-4">Ações</span></th>

                            </thead>


                        </table>


                    </div>
                </div>
                <router-link :to="{ 'name': 'CadastrarAluno' }" class="navbar-item">
                    <button class="button is-success is-fullwidth">Adicionar Aluno</button>
                </router-link>

            </div>

        </div>



    </div>
</template>



<script>
import axios from 'axios';
import { toast } from 'bulma-toast'

export default {
    name: "Alunos",
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
}
</script>