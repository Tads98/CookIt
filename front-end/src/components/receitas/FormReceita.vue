<template>
  <div class="container">
        <h3>Inserindo Sua Receita</h3>
        <form class="form">
          <div class="form-group">
            <input type="text" class="form-control rounded-pill" placeholder="Nome da receita">
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
            <input type="file" class="form-control" name="" id=""/>
          </div>
          <div class="form-group row">
            <div class="form-group col-sm">
              <input multiple id="input" type="text" class="form-control rounded-pill" placeholder="Ingredientes">
            </div>
            <div class="form-group col-sm">
              <input id="input" type="text" class="form-control rounded-pill" placeholder="Categorias">
            </div>
          </div>
          <div id="prep" class="row">
            <div id="prep-mode" class="form-group col-sm">
              <div class="jumbotron">
                <h4>Modo de Preparo</h4>
                <textarea class="form-control" type="text"></textarea>
              </div>
            </div>
            <div id="general" class="form-group col-sm">
              <div class="jumbotron">
                <h4>Caracteristicas gerais</h4>
                <div class="form-group">
                  <div class="custom-control custom-radio custom-control-inline">
                    <input type="radio" id="customRadioInline1" name="customRadioInline1" class="custom-control-input">
                    <label class="custom-control-label" for="customRadioInline1">Doce</label>
                  </div>
                  <div class="custom-control custom-radio custom-control-inline">
                    <input type="radio" id="customRadioInline2" name="customRadioInline1" class="custom-control-input">
                    <label class="custom-control-label" for="customRadioInline2">Salgado</label>
                  </div>
                </div>
                <div class="form-group input-group">
                  <div class="input-group-prepend">
                    <label class="input-group-text">Porções</label>
                  </div>
                  <input class="form-control" id="portions" type="number" min="1">
                </div>
                <div class="form-group input-group">
                  <div class="input-group-prepend">
                    <label class="input-group-text">Tempo de preparo</label>
                  </div>
                  <input id="prep-time" type="time" class="form-control">
                </div>
                <div class="form-group input-group">
                  <div class="input-group-prepend">
                    <label class="input-group-text">Nível de dificuldade</label>
                  </div>
                  <select id="difficulty" class="form-control custom-select">
                    <option id="easy" value="1">Fácil</option>
                    <option id="medium" value="2">Médio</option>
                    <option id="hard" value="3">Difícil</option>
                    <option id="super" value="4">Super</option>
                  </select>
                </div>
                <textarea type="text" class="form-group form-control" placeholder="Observações adicionais"></textarea>
              </div>
            </div>
          </div>
          <button id="submit-button" type="submit" class="btn btn-primary btn-block rounded-pill">Postar</button>
        </form>
      </div>
</template>

<script>
export default {};
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
    color: black
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
*/    resize: none;
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
    background-color: #B1FF62;
}

#medium {
    background-color: #FFE132;
}

#hard {
    background-color: #FC1D00;
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