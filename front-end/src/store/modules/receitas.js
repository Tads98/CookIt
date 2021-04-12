import axios from 'axios';

const state = {
    receitas: [],
};

const getters = {
    allReceitas: state => state.receitas,
};

const actions = {
    async fetchReceitas({ commit }) {
        const response = await axios.get(
            'http://localhost:8000/api/receita/'
        );

        commit ('setReceitas', response.data)
    },
    async basicSearch({ commit }, e) {
        const response = await axios.get(
            'http://localhost:8000/api/receita/?search=' + e
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