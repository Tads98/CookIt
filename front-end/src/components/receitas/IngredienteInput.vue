<template>
  <div>
    <div class="row">
      <div
        class="ing-tag border border-dark p-1 rounded-pill"
        v-for="(ingrediente, index) in ingredientes"
        :key="'ingrediente' + index"
      >
        <span class="p-1 border-right border-dark">{{
          ingrediente.nome_ingrediente
        }}</span>
        <span class="p-1 border-right border-dark">{{
          ingrediente.quantidade_ingrediente
        }}</span>
        <!--        <span class="p-1">{{
          ingrediente.unidade_medida_ingrediente
        }}</span>-->
        <div v-for="opt in ingredienteUnidadeData" :key="opt.char">
          <span v-if="ingrediente.unidade_medida_ingrediente == opt.char">
            {{ opt.text }}
          </span>
        </div>
        <span @click="removeTag(index)">
          <i class="fas fa-times-circle"></i>
        </span>
      </div>
    </div>
    <div class="row form-group">
      <input
        multiple
        id="input"
        type="text"
        class="form-control rounded-pill col-5"
        placeholder="Ingrediente"
        v-model="tagIngredienteNome"
      />
      <select
        class="custom-select col-3"
        name=""
        id="unidade-medida"
        v-model="tagIngredienteUnidade"
      >
        <option value="U" selected>Unidade</option>
        <option value="X">Xícara</option>
        <option value="C">Colher de Sopa</option>
        <option value="CH">Colher de Chá</option>
        <option value="D">Dente de Alho</option>
        <option value="M">Mililitro(ml)</option>
        <option value="L">Litros</option>
        <option value="G">Gramas</option>
        <option value="KG">Quilograma(kg)</option>
        <option value="AGS">ao gosto</option>
      </select>
      <input
        min="1"
        class="form-control col-2"
        type="number"
        v-model="tagIngredienteQuantidade"
      />
      <button type="button" class="btn btn-secondary" @click="addTag">
        <i class="fas fa-plus"></i>
      </button>
      <button type="button" class="btn btn-secondary" @click="addIngredientes">
        teste
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: [ "ingredientes" ],

  data() {
    return {
      ingrediente_ids: [],
      ing_ativo: null,
      ingrediente: null,
      tagIngredienteNome: "",
      tagIngredienteQuantidade: 1,
      tagIngredienteUnidade: "",
      ingredienteUnidadeData: [
        {
          char: "U",
          text: "Unidade",
        },
        {
          char: "X",
          text: "Xícara",
        },
        {
          char: "C",
          text: "Colher de Sopa",
        },
        {
          char: "CH",
          text: "Colher de Chá",
        },
        {
          char: "M",
          text: "Mililitro(ml)",
        },
        {
          char: "L",
          text: "Litros",
        },
        {
          char: "G",
          text: "Gramas(g)",
        },
        {
          char: "KG",
          text: "Quilograma(kg)",
        },
        {
          char: "AGS",
          text: "a gosto",
        },
      ],
    };
  },
  methods: {
    addIngredientes() {
      for(var i = 0; i < this.ingredientes.length; i++){
        axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/ingrediente/",
        data: this.ingredientes[i],
        auth: {
          username: "admin",
          password: "12345",
        },
        headers:{
          Accept: "application/json",
          "Content-Type": "application/json",
        }
      })
        .then((response) => {
          // your action after success
          // this.ingrediente_ids.push(response.id)
          this.ingrediente_ids.push(response.data.id)
          console.log(response);
        })
        .catch((error) => {
          // your action on error success
          console.log(error);
        });
      }
      console.log(this.ingredientes)
    },
    addTag() {
      if (
        this.tagIngredienteNome != "" &&
        this.tagIngredienteUnidade != "" &&
        this.tagIngredienteQuantidade != ""
      ) {
        this.ingrediente = {
          nome_ingrediente: this.tagIngredienteNome,
          unidade_medida_ingrediente: this.tagIngredienteUnidade,
          quantidade_ingrediente: this.tagIngredienteQuantidade,
        };
        console.log(this.ingrediente);
        this.ingredientes.push(this.ingrediente);
      }
      this.tagIngredienteNome = "";
      this.tagIngredienteQuantidade = "";
      this.tagIngredienteUnidade = "";
    },
    removeTag(index) {
      this.ingredientes.splice(index, 1);
    },
    getIngredientes(){
      return this.ingredientes;
    },
  },
};
</script>

<style>
.ing-tag {
  background-color: #f3efef;
}
</style>