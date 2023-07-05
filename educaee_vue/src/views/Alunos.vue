<template>
    <div class="container">

        <div class="columns is-centered is-multiline">

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
                            <h1 id="titulo" class="is-size-1 ml-6 pl-5 has-text-centered"><strong>MEUS ALUNOS</strong>
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
                <div class="box" id="barra-pesquisa">
                    <div class="columns p-1">
                        <div class=" column p-0 is-one-fifth">
                            <div class="field">
                                <div class="control">
                                    <input type="text" placeholder="Nome" class="input is-medium">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>


            </div>

            <div class='column is-12'>
                <div class="box" id="box-tabela">
                    <div class="table-container">

                        <table class="table is-fullwidth">


                            <thead>
                                <th class="has-text-centered"><span class="is-size-4">Nome</span></th>
                                <th class="has-text-centered"><span class="is-size-4">Idade</span></th>
                                <th class="has-text-centered"><span class="is-size-4">Ano</span></th>
                                <th class="has-text-centered"><span class="is-size-4">Ações</span></th>

                            </thead>

                            <tbody>



                            </tbody>

                        </table>


                    </div>
                    <div class="buttons is-right">
                        <router-link :to="{ 'name': 'CadastrarAluno' }">
                            <button id="botao-adicionar" class="button is-rounded is-large">+</button>
                        </router-link>
                    </div>
                </div>


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


<style>
#barra-pesquisa {

    background-color: #05FFF0;
    border-radius: 10px;
}

#box-tabela {
    background-color: #05FFF0;
    border-radius: 10px;

}

#botao-adicionar {

    background-color: #40A403;
    color: white;
    font-family: Poppins;
    font-size: 25px;
    font-weight: bolder;
    border-radius: 60px;

}
</style>