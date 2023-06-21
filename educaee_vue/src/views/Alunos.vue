<template></template>



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