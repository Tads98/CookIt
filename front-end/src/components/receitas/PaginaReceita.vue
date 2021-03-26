<template>
  <div class="container">
    <div id="receita-receita-completa">
      <div id="dados-receita-completa">
        <div class="row">
          <div id="titulo-receita-completa" class="col">
            <h3> Receita </h3>
            <p>
              publicado por <strong> Usuário </strong>
            </p>
            <div>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
            </div>
          </div>
          <div id="thumbnails-receita-completa" class="col">
            <div class="row">
              <!--TODO: ver uma formatação melhor para a imagem-->
              <img
                class="receita-foto rounded-circle"
                style="max-width: 800px"
                src=""
                alt=""
              />
            </div>
          </div>
          <div id="opcoes-receita-completa" class="col-1">
            <a href=""><i class="far fa-heart fa-lg"></i></a>
            <br />
            <a href=""><i class="fas fa-share-alt"></i></a>
            <br />
            <a href=""><i class="fas fa-flag"></i></a>
          </div>
        </div>
        <div class="col-md">
          <div class="row">
            <div class="col mb-3">
              <div id="icones-receita-completa" class="col">
                <div
                  class="col line-receita-completa"
                  style="border: none"
                >
                  <div class="icon-text-receita-completa">
                    <i class="far fa-clock"></i>
                    <br />
                    <p>
                      Tempo de Preparo
                    </p>
                  </div>
                </div>

                <div class="col line-receita-completa">
                  <div class="icon-text-receita-completa">
                    <i class="fas fa-concierge-bell"></i>
                    <br />
                    <p>
                      Porções
                    </p>
                  </div>
                </div>

                <div class="col line-receita-completa">
                  <div class="icon-text-receita-completa">
                    <i class="fas fa-burn"></i>
                    <br />
                    <p>
                      Dificuldade:
                    </p>
                  </div>
                </div>

                <div class="col line-receita-completa">
                  <div class="icon-text-receita-completa">
                    <i class="far fa-heart"></i>
                    <br />
                    <p>Favoritos</p>
                  </div>
                </div>

                <div class="col line-receita-completa">
                  <div class="icon-text-receita-completa">
                    <i class="far fa-comment-alt"></i>
                    <br />
                    <p>Comentários</p>
                  </div>
                </div>

                <div class="col line-receita-completa">
                  <div class="icon-text-receita-completa">
                    <i class="far fa-calendar-alt"></i>
                    <br />
                    <p>Data de publicação</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="row mb-3">
            <div id="ingredientes-receita-completa" class="col">
              <h3>
                Ingredientes
              </h3>

              <div id="alinhamento-ingredientes">
                <p>
                  <strong style="color: #f0a916">
                      Nome do Ingrediente
                  </strong>
                  <strong>Unidade de Medida</strong>
                </p>
              </div>
            </div>

            <div id="modo-de-preparo-receita-completa" class="col">
              <h3>Modo de Preparo</h3>

              <p> [[ Texto ]]</p>
            </div>
          </div>

          <div class="row">
            <div class="col">
              <h3>Observações Adicionais</h3>

              <div id="obad-receita-completa">
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras
                  eu dapibus eros, at interdum odio. Integer at enim eu ligula
                  fermentum gravida. Pellentesque non odio a diam accumsan
                  blandit accumsan vitae lectus. Etiam vitae placerat justo.
                  Etiam vel volutpat nisi. Fusce eleifend arcu vel consequat
                  vestibulum. Aliquam vulputate hendrerit tincidunt. Nulla in
                  porta nunc, nec pulvinar lacus. Nullam vel eros justo.
                  Phasellus quis lacus vel velit mollis bibendum. Etiam volutpat
                  enim non gravida maximus.
                </p>
              </div>
            </div>
            <div class="col">
              <h3>Chef</h3>
              <div id="usuario-receita-completa">
                <div id="dados-usuario-receita-completa" class="row">
                  <i class="fas fa-user-circle col-2"></i>
                  <div class="col">
                    <h4>Dono da Receita</h4>
                    <p>
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                      Cras eu dapibus eros, at interdum odio. Integer at enim eu
                      ligula fermentum gravida.
                    </p>
                  </div>
                </div>
                <div id="icones-usuario-receita-completa" class="row">
                  <div class="col">
                    <i class="far fa-images"></i>
                  </div>
                  <div class="col">
                    <i class="fas fa-book"></i>
                    <p>Receitas</p>
                  </div>
                  <div class="col">
                    <i class="far fa-heart"></i>
                    <p>Favoritos</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div id="comentarios-receita-completa"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
.container {
  margin: 0 auto;
  margin-top: 80px;
  border-left: 1px solid #707070;
  border-right: 1px solid #707070;
}
#receita-receita-completa {
  border: 1px solid #707070;
  border-radius: 1em;
  background-color: #f3efef;
}
#dados-receita-completa,
#comentarios-receita-completa {
  background-color: white;
  border: 1px solid grey;
  border-radius: 1em;
  margin: 1em;
  padding: 1em;
}
#titulo-receita-completa {
  text-align: center;
}
#titulo-receita-completa h3 {
  color: #aba11b;
}
#opcoes-receita-completa {
  display: flex;
  align-items: center;
  flex-direction: column;
}
#icones-receita-completa {
  border: 1px solid #707070;
  background-color: #f3efef;
  border-radius: 1em;
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 1em;
}
.icon-text-receita-completa {
  text-align: center;
  max-width: 7em;
}
.icon-text-receita-completa i {
  font-size: 2em;
}
.icon-text-receita-completa p {
  margin-bottom: 0;
}
.utensils-receita-completa {
  padding: 1em;
  border: 1px solid grey;
  background-color: darkgray;
  max-width: 3.5em;
  max-height: 3.5em;
  text-align: center;
  vertical-align: middle;
  font-size: 1.5em;
  margin-left: 0.5em;
  margin-right: 0.5em;
}
#alinhamento-ingredientes {
  border: 1px solid #707070;
  border-radius: 1em;
  display: flex;
  flex-wrap: wrap;
  padding: 8px;
}
#alinhamento-ingredientes p {
  margin: 5px;
  margin-bottom: 10px;
  padding: 5px;
  padding-left: 8px;
  padding-right: 8px;
  font-size: 12px;
  display: inline-block;
  border: 1px solid #707070;
  border-radius: 1.5em;
  height: 28px;
}
#alinhamento-ingredientes p::-webkit-scrollbar-track {
  box-shadow: inset 0 0 5px grey;
  border-radius: 10px;
}
#modo-de-preparo-receita-completa p {
  border: 1px solid #707070;
  background-color: #f3efef;
  border-radius: 1em;
  font-size: 12px;
  padding: 1em;
  text-align: justify;
  text-justify: initial;
}
#alinhamento-ingredientes,
#modo-de-preparo-receita-completa p {
  min-height: 120px;
  max-height: 240px;
  overflow: auto;
}
#alinhamento-ingredientes::-webkit-scrollbar,
#modo-de-preparo-receita-completa p::-webkit-scrollbar {
  width: 1.5em;
}
/* Handle */
#alinhamento-ingredientes::-webkit-scrollbar-thumb,
#modo-de-preparo-receita-completa p::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 1em;
  border: 0.5em solid transparent;
  background-clip: content-box;
}
/* Handle on hover */
#alinhamento-ingredientes::-webkit-scrollbar-thumb:hover,
#modo-de-preparo-receita-completa p::-webkit-scrollbar-thumb:hover {
  background: #444;
  border-radius: 1em;
  border: 0.5em solid transparent;
  background-clip: content-box;
}
textarea {
  resize: none;
  border-radius: 1em;
  width: 100%;
}
#usuario-receita-completa,
#obad-receita-completa {
  border: 1px solid #707070;
  border-radius: 1em;
  padding: 1em;
}
#icones-usuario-receita-completa,
#usuario-receita-completa i,
#usuario-receita-completa h4 {
  text-align: center;
}
#usuario-receita-completa i {
  font-size: 4em;
}
#icones-usuario-receita-completa i {
  font-size: 2em;
}
.line-receita-completa {
  border-left: 1px solid black;
  height: 65px;
  width: 16.6%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.fa-star {
  color: orange;
}
.receita-foto {
  object-fit: cover;
  /* Do not scale the image */
  object-position: center;
  /* Center the image within the element */
  width: 120px;
  height: 120px;
  margin-bottom: 1rem;
  border: 1px solid #707070;
}
</style>