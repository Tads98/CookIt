import axios from 'axios';

const state = {
    receitas: [],
    pesquisa: {
        nome_receita: '',
        sabor_receita: [],
        categoria: '',
        dificuldade: [],
    }
};

const getters = {
    allReceitas: state => state.receitas,
    getPesquisa: state => state.pesquisa, 
};

const actions = {
    async fetchReceitas({ commit }) {
        const response = await axios.get(
            'http://localhost:8000/api/receita/'
        );

        commit ('setReceitas', response.data)
    },
    async basicSearch({ commit, getters }) {
        const response = await axios.get(
            'http://localhost:8000/api/receita/?nome_receita__icontains=' + getters.getPesquisa.nome_receita
            + '&sabor_receita__in=' + getters.getPesquisa.sabor_receita + '&dificuldade=' + getters.getPesquisa.dificuldade
            + '&categoria=' + getters.getPesquisa.categoria
        );

        commit ('setReceitas', response.data)
    }
}

const mutations = {
    setReceitas: (state, receitas) => (state.receitas = receitas),
};

export default {
    state,
    getters,
    actions,
    mutations
}