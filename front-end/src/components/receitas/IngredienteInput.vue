<template>
  <div>
    <div
      v-for="(ingrediente, index) in ingredientes"
      :key="'ingrediente' + index"
    >
      <span></span>
    </div>
    <div class="row form-group">
      <div
        v-for="(ingrediente, index) in ingredientes"
        :key="'ingrediente' + index"
      >
        <span v-if="ing_ativo !== index" @click="ing_ativo = index">{{
          ingrediente
        }}</span>
        <input v-else
          type="text"
          v-model="ingredientes[index]"
          v-focus
          :style="{ width: ing_ativo + 'ch' }"
          @keyup.enter="ing_ativo = null"
          @blur="ing_ativo = null"
        />
        <span @click="removeTag(index)"
          ><i class="fas fa-times-circle"></i
        ></span>
      </div>
      <input
        multiple
        id="input"
        type="text"
        class="form-control rounded-pill col-5"
        placeholder="Ingrediente"
        v-model="tagInput"
        @keyup.enter="addTag"
      />
      <button type="button" @click="addTag">Adicionar</button>
      <select class="form-control col-3" name="" id="unidade-medida">
        <option value="1">Unidade</option>
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
      <input class="form-control col-2" type="number" />
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
      nome_ingrediente: "",
      quant_ingrediente: "",
      uni_ingrediente: "",
    };
  },
  methods: {
    addTag() {
      if (!this.tagInput == "") {
        this.ingredientes.push(this.tagInput);
      }
      this.tagInput = "";
    },
    removeTag(index) {
      this.ingredientes.splice(index, 1);
    },
  },
};
</script>

<style>
</style>