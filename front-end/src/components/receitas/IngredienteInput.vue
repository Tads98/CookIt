<template>
  <div>
    <div class="row">
        <div class="ing-tag border border-dark p-1 rounded-pill">
            <span class="p-1 border-right border-dark">Ingrediente</span>
            <span class="p-1 border-right border-dark">Q</span>
            <span class="p-1">Unidade</span>
        </div>
    </div>
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
        <span class="p-1">{{
          ingrediente.unidade_medida_ingrediente
        }}</span>
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
        <option value="1" selected>Unidade</option>
        <option value="2">Xícara</option>
        <option value="3">Colher de Sopa</option>
        <option value="4">Colher de Chá</option>
        <option value="5">Dente de Alho</option>
        <option value="6">Mililitro(ml)</option>
        <option value="7">Litros</option>
        <option value="8">Gramas</option>
        <option value="9">Quilograma(kg)</option>
        <option value="10">ao gosto</option>
      </select>
      <input
        min=1
        class="form-control col-2"
        type="number"
        v-model="tagIngredienteQuantidade"
      />
      <button type="button" class="btn btn-secondary" @click="addTag">
          <i class="fas fa-plus"></i>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "IngredienteInput",
  data() {
    return {
      ingredientes: [],
      ing_ativo: null,
      ingrediente: null,
      tagIngredienteNome: "",
      tagIngredienteQuantidade: 1,
      tagIngredienteUnidade: "",
    };
  },
  methods: {
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
  },
};
</script>

<style>
.ing-tag{
    background-color: #F3EFEF;
}
</style>