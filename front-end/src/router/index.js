import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../components/Index.vue'
import PaginaReceita from '../components/receitas/PaginaReceita'
import FormReceita from '../components/receitas/FormReceita'
import EditarPerfil from '../components/usuario/EditarPerfil'
import LoginCadastro from '../components/usuario/LoginCadastro'


Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Index',
        component: Index
    },
    {
        path: '/FormReceita/',
        name: 'FormReceita',
        component: FormReceita
    },
    {
        path: '/PaginaReceita/:id', 
        name: 'PaginaReceita',
        component: PaginaReceita
    },
    {
        path: '/EditarPerfil/',
        name: 'EditarPerfil',
        component: EditarPerfil
    },
    {
        path: '/LoginCadastro/',
        name: 'LoginCadastro',
        component: LoginCadastro
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router