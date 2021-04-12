import Vue from 'vue';
import Vuex from 'vuex';
import receitas from './modules/receitas';

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        receitas,
    },
});