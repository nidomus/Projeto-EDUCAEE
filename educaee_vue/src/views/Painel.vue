<template>
    <div class="container is-fluid">

        <div class="columns is-multiline is-vcentered is-centered">

            <div class="column is-7">
                <div class="box" style="background-color: #FFE600; border-radius: 20px;">
                    <div class="columns is-centered is-vcentered">
                        <div class="column is-four-fifths pr-0">
                            <h1 id="titulo" class="is-size-1 ml-6 pl-6 has-text-centered"><strong>MEU PAINEL</strong>
                            </h1>
                        </div>

                        <div class="column is-narrow pl-0">
                            <div class="buttons is-left">
                                <button class="button is-danger is-rounded is-medium" @click="logout()">Sair</button>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <div class="column is-12">
                <div>
                    <div class="columns is-multiline is-centered is-vcentered">

                        <div class="column is-narrow p-5">

                            <a href="">
                                <div class="box p-6 botao has-text-centered" style="background-color: #60FF28;">
                                    <h1 class="title has-text-centered is-size-3 mb-0">Iniciar Sessão</h1>
                                    <img src="@/assets/play.png" alt="" style="height: 95%;">

                                </div>
                            </a>
                        </div>
                        <div class="column is-narrow p-5">

                            <router-link :to="{ 'name': 'Alunos' }">
                                <div class="box p-6 botao has-text-centered" style="background-color: #05FFF0;">
                                    <h1 class="title has-text-centered is-size-3 mb-5">Meus Alunos</h1>
                                    <img src="@/assets/alunos.png" alt="">

                                </div>
                            </router-link>
                        </div>
                        <div class=" column is-narrow p-5">

                            <router-link :to="{ 'name': 'CadastrarAluno' }">
                                <div class="box p-6 botao has-text-centered" style="background-color: #FF00F5;">
                                    <h1 class="title has-text-centered is-size-3 mb-4">Adicionar Aluno</h1>
                                    <img src="@/assets/add_aluno.png" alt="" style="height: 70%;">

                                </div>
                            </router-link>
                        </div>

                    </div>
                </div>
            </div>
            <div class="column is-12">
                <div>
                    <div class="columns is-multiline is-centered is-vcentered">

                        <div class="column is-narrow p-5">

                            <a href="">
                                <div class="box p-6 botao has-text-centered" style="background-color: #FF6928;">
                                    <h1 class="title has-text-centered is-size-3 mb-4">Atividades</h1>
                                    <img src="@/assets/atividades.png" alt="" style="height: 85%;">

                                </div>
                            </a>
                        </div>
                        <div class="column is-narrow p-5">

                            <router-link :to="{ 'name': 'Alunos' }">
                                <div class="box p-6 botao has-text-centered" style="background-color: #60FF28;">
                                    <h1 class="title has-text-centered is-size-3 mb-4">Minhas Sessões</h1>
                                    <img src="@/assets/minhas_sessoes.png" alt="" style="height: 85%;">

                                </div>
                            </router-link>
                        </div>
                        <div class="column is-narrow p-5">

                            <router-link :to="{ 'name': 'CadastrarAluno' }">
                                <div class="box p-6 botao has-text-centered" style="background-color: #D9D9D9;">
                                    <h1 class="title has-text-centered is-size-3 mb-4">Relatório</h1>
                                    <img src="@/assets/relatorio.png" alt="" style="height: 85%;">

                                </div>
                            </router-link>
                        </div>

                    </div>
                </div>
            </div>

        </div>
    </div>
</template>



<script>
import router from '@/router';
import axios from 'axios';
import { toast } from 'bulma-toast'

export default {
    name: "Painel",
    data() {
        return {

        }
    },
    methods: {

        logout() {
            this.$store.commit('logoutUser')
            this.$store.commit('removeToken')
            this.$router.push('/log-in')
        }

    }
}
</script>

<style>
.botao {
    border-radius: 60px;
    box-shadow: 10px 10px;
    height: 300px;
    width: 335px;

}

#titulo {

    font-family: Poppins;
    font-weight: bolder;
    font-size: larger;

}
</style>