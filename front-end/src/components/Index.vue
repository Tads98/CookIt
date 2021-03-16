<template>
  <div class="cards-tela-inicial row row-cols-1 row-cols-sm-2 row-cols-md-2 row-cols-lg-3">
    <h2>Hello</h2>
    <div class="col mb-4">
      <div v-for="receita in receitas" v-bind:key="receita.id" class="card receita-tela-inicial h-100">
        <a href="">
          <!--TODO: o tamanho da imagem precisa ser fixo e seu container também-->
          <img src="" alt="" class="card-img-top" />
          <img src="cocktail.jpeg" class="card-img-top" alt="..." />
        </a>
        <div class="card-body">
          <a href="" class="fav-tela-inicial">
            <i class="far fa-heart"></i>
          </a>
          <a href="">
            <h5 class="card-title">{{ receita.nome_receita }}</h5>
          </a>
          <p class="card-text">
            Publicado por
            <a style="font-size: 12px" href="">
              <strong>UwU Man</strong>
            </a>
          </p>
          <p class="card-text">
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
          </p>
          <p class="card-text descricao-tela-inicial"></p>
          <hr />
          <div class="row">
            <div class="info-tela-inicial col">
              <div class="row">
                <div class="col">
                  <i style="font-size: 25px" class="far fa-clock"></i>
                  <p>5 minutos</p>
                </div>
                <div class="col">
                  <i style="font-size: 25px" class="fas fa-concierge-bell"></i>
                  <p>5 porções</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <button
          onclick="window.location.href='';"
          class="see-more-tela-inicial btn"
        >
          <i class="fas fa-book-open"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Index",
  data() {
    return {
        receitas: []
    }
  },
  mounted() {
    this.getReceitas()
  },
  methods: {
    getReceitas() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/receita/",
        auth: {
          username: "admin",
          password: "12345",
        }
      }).then(response => this.receitas = response.data);
    }
  }
}
</script>

<style>
</style>