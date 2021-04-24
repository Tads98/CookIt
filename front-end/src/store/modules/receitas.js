import axios from 'axios';

const state = {
    receitas: [],
    pesquisa: {
        nome_receita: '',
        sabor_receita: [],
        categoria: [],
        dificuldade: '',
        ingredientes: [],
        n_ingredientes: [],
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
            + '&categoria__in=' + getters.getPesquisa.categoria
            + '&ingredientes__nome_ingrediente__in=' + getters.getPesquisa.ingredientes
            + '&ingredientes_not=' + getters.getPesquisa.n_ingredientes
        );

        commit ('setReceitas', response.data)
    },

    async deleteReceita({ commit }, id) {
        await axios.delete(`http://localhost:8000/api/receita/${id}`);
        
        commit('removeReceita', id);
    }
}

const mutations = {
    setReceitas: (state, receitas) => (state.receitas = receitas),
    RemoveReceitas: (state, id) =>
        (state.receitas = state.receitas.filter(receita => receita.id !== id)),
};

export default {
    state,
    getters,
    actions,
    mutations
}