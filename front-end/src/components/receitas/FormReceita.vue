<template>
  <div class="container">
    <h3>Inserindo Sua Receita</h3>
    <form class="form" v-on:submit.prevent="addReceita">
      <div class="form-group">
        <input
          type="text"
          class="form-control rounded-pill"
          placeholder="Nome da receita"
          v-model="nome_receita"
        />
      </div>
      <div class="form-group">
        <!--  <ul id="thumbnail-input-group" class="jumbotron d-flex justify-content-around p-0">
              <li class="form-control rounded-circle d-flex justify-content-center align-items-center" id="thumbnail-input">
                <a href="">
                  <i class="fas fa-camera"></i>
                </a>
              </li>
              <li class="form-control rounded-circle d-flex justify-content-center align-items-center" id="thumbnail-input">
                <a href="">
                  <i class="fas fa-camera"></i>
                </a>
              </li>
              <li class="form-control rounded-circle d-flex justify-content-center align-items-center" id="thumbnail-input">
                <a href="">
                  <i class="fas fa-camera"></i>
                </a>
              </li>
              <li class="form-control rounded-circle d-flex justify-content-center align-items-center" id="thumbnail-input">
                <a href="">
                  <i class="fas fa-camera"></i>
                </a>
              </li>
              <li class="form-control rounded-circle d-flex justify-content-center align-items-center" id="thumbnail-input">
                <a href="">
                  <i class="fas fa-camera"></i>
                </a>
              </li>
            </ul>-->
        <label for="">Foto</label>
        <input type="file" class="form-control" name="" id="" />
      </div>
      <div class="row">
        <div class="form-group col-sm">
          <IngredienteInput v-bind:ingredientes="ingredientes"/>
        </div>
        <div class="form-group col-sm">
          <input
            id="input"
            type="text"
            class="form-control rounded-pill"
            placeholder="Categorias"
          />
        </div>
      </div>
      <div id="prep" class="row">
        <div id="prep-mode" class="form-group col-sm">
          <div class="jumbotron">
            <h4>Modo de Preparo</h4>
            <textarea
              class="form-control"
              type="text"
              v-model="modo_preparo"
            ></textarea>
          </div>
        </div>
        <div id="general" class="form-group col-sm">
          <div class="jumbotron">
            <h4>Caracteristicas gerais</h4>
            <div class="form-group">
              <div class="custom-control custom-radio custom-control-inline">
                <input
                  type="radio"
                  id="customRadioInline1"
                  name="customRadioInline1"
                  class="custom-control-input"
                />
                <label class="custom-control-label" for="customRadioInline1"
                  >Doce</label
                >
              </div>
              <div class="custom-control custom-radio custom-control-inline">
                <input
                  type="radio"
                  id="customRadioInline2"
                  name="customRadioInline1"
                  class="custom-control-input"
                />
                <label class="custom-control-label" for="customRadioInline2"
                  >Salgado</label
                >
              </div>
            </div>
            <div class="form-group input-group">
              <div class="input-group-prepend">
                <label class="input-group-text">Porções</label>
              </div>
              <input
                class="form-control"
                id="portions"
                type="number"
                min="1"
                v-model="porcoes"
              />
            </div>
            <div class="form-group input-group">
              <div class="input-group-prepend">
                <label class="input-group-text">Tempo de preparo</label>
              </div>
              <input
                id="prep-time"
                type="number"
                class="form-control"
                v-model="tempo_preparo"
              />
            </div>
            <div class="form-group input-group">
              <div class="input-group-prepend">
                <label class="input-group-text">Nível de dificuldade</label>
              </div>
              <select
                id="difficulty"
                class="form-control custom-select"
                v-model="dificuldade"
              >
                <option id="easy" value="F">Fácil</option>
                <option id="medium" value="M">Médio</option>
                <option id="hard" value="D">Difícil</option>
                <option id="super" value="C">Super</option>
              </select>
            </div>
            <textarea
              type="text"
              class="form-group form-control"
              placeholder="Observações adicionais"
              v-model="observacoes_adicionais"
            ></textarea>
          </div>
        </div>
      </div>
      <button
        id="submit-button"
        type="submit"
        class="btn btn-primary btn-block rounded-pill"
      >
        Postar
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import IngredienteInput from './IngredienteInput';

export default {
  name: "FormReceita",

  components:{
    IngredienteInput,
  },

  data() {
    return {
      nome_receita: "",
      modo_preparo: "",
      porcoes: 0,
      sabor_receita: "D",
      tempo_preparo: 0,
      tempo_unidade_medida: "M",
      fotos: null,
      categoria: "A",
      dificuldade: "F",
      data_publicacao: "",
      slug: "",
      observacoes_adicionais: "",
      ingredientes: [],
      //Tag Ingrediente
    };
  },


  methods: {
    addReceita() {
      console.log(this.ingredientes)
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/post-receita/",
        data: {
          nome_receita: this.nome_receita,
          modo_preparo: this.modo_preparo,
          dono_receita: 1,
          porcoes: this.porcoes,
          sabor_receita: this.sabor_receita,
          tempo_preparo: this.tempo_preparo,
          tempo_unidade_medida: this.tempo_unidade_medida,
          fotos: this.fotos,
          categoria: this.categoria,
          dificuldade: this.dificuldade,
          data_publicacao: this.data_publicacao,
          slug: this.slug,
          observacoes_adicionais: this.observacoes_adicionais,
          ingredientes: this.ingredientes,
        },
        auth: {
          username: "admin",
          password: "12345",
        },
      })
        .then((response) => {
          /*let newReceita = {
            id: response.data.id,
            nome_receita: this.nome_receita,
            modo_preparo: this.modo_preparo,
            porcoes: this.porcoes,
            sabor_receita: this.sabor_receita,
            tempo_preparo: this.tempo_preparo,
            tempo_unidade_medida: this.tempo_unidade_medida,
            fotos: this.fotos,
            categoria: this.categoria,
            dificuldade: this.dificuldade,
            data_publicacao: this.data_publicacao,
            slug: this.slug,
            observacoes_adicionais: this.observacoes_adicionais,
            ingredientes: this.ingredientes,
          };
          */
          //this.receitas.push(newReceita);

          this.nome_receita = "";
          this.modo_preparo = "";
          this.porcoes = 0;
          this.sabor_receita = "";
          this.tempo_preparo = 0;
          this.tempo_unidade_medida = "";
          this.fotos = null;
          this.categoria = "";
          this.dificuldade = "";
          this.data_publicacao = "";
          this.slug = "";
          this.observacoes_adicionais = "";
          this.ingredientes = [];

          console.log(response);
          this.$router.push({name: 'PaginaReceita', params: {id: response.data.id}})
        })
        .catch((error) => {
          console.log(error);
        });
    },
    /*  */
  },
};
</script>

<style scoped>
.container {
  border: none !important;
  margin-top: 70px;
  padding-top: 4rem;
  padding-bottom: 4rem;
  background-color: white;
  border-left: 1px solid darkgray;
  border-right: 1px solid darkgray;
}
#search-input {
  outline: none;
  box-shadow: none !important;
  border-radius: 36px 0 0 36px;
  width: 20vw;
}

#search-button {
  border-radius: 0 36px 36px 0;
  padding: 0 1em 0 1em;
  background-color: white;
  border: 1px solid gray;
  color: gray;
  margin-left: -1px;
}

#search-button i {
  vertical-align: middle;
}

#thumbnail-input-group {
  padding: 1em 0 1em 0 !important;
}

.jumbotron {
  background-color: lightgray;
  border: 1px solid gray;
}

#thumbnail-input {
  list-style-type: none;
  width: 10vw;
  height: 10vw;
  font-size: 4vw;
  color: black;
  border: 1px solid gray;
}

#thumbnail-input a {
  color: black;
}

#prep-time,
textarea,
#portions {
  border: none;
  outline: none;
  box-shadow: none !important;
}

#prep-input {
  height: 60px;
}

textarea {
  /*    width: 100%;
    height: 100%;
*/
  resize: none;
}

h3,
h4 {
  font-weight: bold;
  text-align: center;
  margin-bottom: 1em;
}

.form-control,
.input-group-text,
.custom-control-input {
  border: 1px solid gray !important;
}

#portions,
#prep-time,
#difficulty {
  border-radius: 0 36px 36px 0;
}

.input-group-text {
  border-radius: 36px 0 0 36px !important;
}

#submit-button {
  background-color: white;
  font-weight: bold;
  border: 1px solid gray !important;
  color: black;
  margin: 0 !important;
}

#prep button {
  background-color: lightgray;
  border: 1px solid gray !important;
  color: black;
}

.form {
  align-items: center;
  justify-content: center;
}

#easy {
  background-color: #b1ff62;
}

#medium {
  background-color: #ffe132;
}

#hard {
  background-color: #fc1d00;
}

#super {
  background-color: #191919;
}

textarea,
#prep-mode div div {
  border-radius: 18px !important;
}

#prep .jumbotron {
  height: 460px !important;
}
</style>