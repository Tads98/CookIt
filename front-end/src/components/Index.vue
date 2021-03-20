<template>
<<<<<<< HEAD
  <div
    class="cards-tela-inicial row row-cols-1 row-cols-sm-2 row-cols-md-2 row-cols-lg-3"
  >
    <div class="col mb-4">
      <div class="card receita-tela-inicial h-100">
        <a href="">
          <!--TODO: o tamanho da imagem precisa ser fixo e seu container também-->
          <img
            src=""
            alt=""
            class="card-img-top"
          />
=======
  <div class="cards-tela-inicial row row-cols-1 row-cols-sm-2 row-cols-md-2 row-cols-lg-3">
    
    <div class="col mb-4">
      <div v-for="receita in receitas" v-bind:key="receita.id" class="card receita-tela-inicial h-100">
        <a href="">
          <!--TODO: o tamanho da imagem precisa ser fixo e seu container também-->
          <img src="" alt="" class="card-img-top" />
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
          <img src="cocktail.jpeg" class="card-img-top" alt="..." />
        </a>
        <div class="card-body">
          <a href="" class="fav-tela-inicial">
            <i class="far fa-heart"></i>
          </a>
          <a href="">
<<<<<<< HEAD
            <h5 class="card-title">Nome Receita</h5>
=======
            <h5 class="card-title">{{ receita.nome_receita }}</h5>
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
          </a>
          <p class="card-text">
            Publicado por
            <a style="font-size: 12px" href="">
<<<<<<< HEAD
              <strong>UwU Man</strong>
=======
              <strong>{{ receita.dono_receita.usuario }}</strong>
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
            </a>
          </p>
          <p class="card-text">
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
          </p>
<<<<<<< HEAD
          <p class="card-text descricao-tela-inicial">
          </p>
=======
          <p class="card-text descricao-tela-inicial"></p>
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
          <hr />
          <div class="row">
            <div class="info-tela-inicial col">
              <div class="row">
                <div class="col">
                  <i style="font-size: 25px" class="far fa-clock"></i>
<<<<<<< HEAD
                  <p>
                    5 minutos
                  </p>
                </div>
                <div class="col">
                  <i style="font-size: 25px" class="fas fa-concierge-bell"></i>
                  <p>
                    5 porções
                  </p>
=======
                  <p>5 minutos</p>
                </div>
                <div class="col">
                  <i style="font-size: 25px" class="fas fa-concierge-bell"></i>
                  <p>5 porções</p>
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
                </div>
              </div>
            </div>
          </div>
        </div>
        <button
          onclick="window.location.href='';"
<<<<<<< HEAD
          class="see-more-tela-inicial btn">
=======
          class="see-more-tela-inicial btn"
        >
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
          <i class="fas fa-book-open"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
<<<<<<< HEAD
export default {};
</script>

<style>
=======
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
* {
    font-family: 'Montserrat', sans-serif;
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

body {
    margin-top: 70px !important;
    background-color: lightgray;
}
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
.receita-tela-inicial {
  /*    padding: 2em 2em 0 2em !important; */
  background-color: white;
  /*    border-radius: 0.5em; */
}
<<<<<<< HEAD

=======
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
.cards-tela-inicial {
  /*    margin: 1em !important;
        border-radius: 1em;
        border: 1px solid #707070; */
  padding-top: 1em;
}
<<<<<<< HEAD

=======
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
a {
  text-decoration: none !important;
  color: black;
}
<<<<<<< HEAD

a:hover {
  color: black;
}

=======
a:hover {
  color: black;
}
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
.utensils-tela-inicial {
  text-align: center;
  height: 2em;
  width: 2em;
  border: 1px solid gray;
  background-color: lightgray;
}
<<<<<<< HEAD

=======
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
div p,
ul li {
  font-size: 12px;
}
.prep-mode-tela-inicial {
    border-bottom: 1px solid gray;
    margin-bottom: 1em;
}
<<<<<<< HEAD

=======
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
.ingredients-tela-inicial {
    padding-left: 2em !important;
    border-left: 1px solid gray;
}
<<<<<<< HEAD

=======
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
.see-more-tela-inicial {
    width: 100%;
    align-self: center;
    /*    border-radius: 1em 1em 0 0 !important; */
    border-top: 1px solid gray;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    border-bottom-right-radius: .50em;
    border-bottom-left-radius: .50em;
    background-color: lightgray;
    color: black;
    /*    font-size: 1.5em; */
}
<<<<<<< HEAD

=======
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
.see-more-tela-inicial:hover {
    background-color: gray;
    border-color: black;
}
<<<<<<< HEAD

.info-tela-inicial {
    text-align: center;
}

.fa-star {
    color: orange;
}

#keywords {
    border-bottom: 1px solid black;
}

=======
.info-tela-inicial {
    text-align: center;
}
.fa-star {
    color: orange;
}
#keywords {
    border-bottom: 1px solid black;
}
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
.card-img-top {
    object-fit: cover;
    object-position: center;
    height: 180px;
    border-top-left-radius: .50em;
    border-top-right-radius: .50em;
}
<<<<<<< HEAD

=======
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
.descricao-tela-inicial {
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    text-align: justify !important;
    margin-bottom: 1em;
    height: 70px;
}
<<<<<<< HEAD

=======
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
.card-title {
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
    color: #ABA11B;
    font-weight: bold;
    text-align: center;
}
<<<<<<< HEAD

=======
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
.fav-tela-inicial {
    position: relative !important;
    float: right !important;
}
<<<<<<< HEAD

.card-text {
    text-align: center;
}

hr {
    border-color: black;
}
</style>
=======
.card-text {
    text-align: center;
}
hr {
    border-color: black;
}

</style>
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
