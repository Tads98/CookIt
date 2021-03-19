<template>
  <div class="container">
    <div class="container">
      <h3>Inserindo Sua Receita</h3>
      <form enctype="multipart/form-data" method="POST">
        <div class="form-group" id="form_receita_nome_receita">
          <label>Nome da receita:</label>
          <input type="text" class="form-control rounded-pill" />
        </div>

        <div class="form-group" id="form_receita_fotos">
          <label for="inputAddress2">Fotos:</label>
          <input type="file" class="form-control rounded-pill" />
        </div>

        <div class="form-row">
          <div class="form-group col-md-6" id="form_receita_ingredientes">
            <label for="inputPassword4">Ingredientes</label>
            <input type="text" class="form-control" />
            <select class="form-select" aria-label="Default select example">
              <option selected>Open this select menu</option>
              <option value="1">One</option>
              <option value="2">Two</option>
              <option value="3">Three</option>
            </select>
            <input type="text" class="form-control" />
          </div>
          <div
            class="form-group col-md-6"
            id="form_receita_caracteristicas_gerais"
          >
            <label for="inputPassword4">Características gerais</label>
            <div id="form_receita_caracteristicas_gerais_container">
              <div>
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="radio"
                    name="flexRadioDefault"
                    id="flexRadioDefault1"
                  />
                  <label class="form-check-label" for="flexRadioDefault1">
                    Default radio
                  </label>
                </div>
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="radio"
                    name="flexRadioDefault"
                    id="flexRadioDefault2"
                    checked
                  />
                  <label class="form-check-label" for="flexRadioDefault2">
                    Default checked radio
                  </label>
                </div>
                <select class="form-select" aria-label="Default select example">
                  <option selected>Open this select menu</option>
                  <option value="1">One</option>
                  <option value="2">Two</option>
                  <option value="3">Three</option>
                </select>
              </div>
              <div>
                <label for="porcoes">Porções</label>
                <input type="text" class="form-control" />

                <label for="tempo_preparo">Tempo de preparo</label>
                <input type="text" class="form-control" />

                <select class="form-select" aria-label="Default select example">
                  <option selected>Open this select menu</option>
                  <option value="1">One</option>
                  <option value="2">Two</option>
                  <option value="3">Three</option>
                </select>

                <select class="form-select" aria-label="Default select example">
                  <option selected>Open this select menu</option>
                  <option value="1">One</option>
                  <option value="2">Two</option>
                  <option value="3">Three</option>
                </select>
              </div>
            </div>
          </div>
        </div>

        <div class="form-row">
          <div class="form-group col-md-6" id="form_receita_modo-preparo">
            <label for="modo_preparo">Modo de preparo</label>
            <textarea
              name=""
              class="form-control"
              id=""
              cols="30"
              rows="10"
            ></textarea>
          </div>

          <div class="form-group col-md-6" id="form_receita_obs-adicionais">
            <label for="inputPassword4">Observações adicionais</label>
            <textarea
              name=""
              class="form-control"
              id=""
              cols="30"
              rows="10"
            ></textarea>
          </div>
        </div>
        <div class="form-row">
          <button id="form_receita_button" type="submit" class="btn">
            Postar
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.container {
  border: none !important;
  padding-top: 4rem;
  padding-bottom: 4rem;
  background-color: white;
  border-left: 1px solid darkgray;
  border-right: 1px solid darkgray;
}
#thumbnail-input-group-editarreceita {
  padding: 1em 0 1em 0 !important;
}
.jumbotron {
  background-color: lightgray;
  border: 1px solid gray;
}
#thumbnail-input-editarreceita {
  list-style-type: none;
  width: 10vw;
  height: 10vw;
  font-size: 4vw;
  color: black;
  border: 1px solid gray;
}
#thumbnail-input-editarreceita a {
  color: black;
}
#prep-time-editarreceita,
textarea,
#portions-editarreceita {
  border: none;
  outline: none;
  box-shadow: none !important;
}
#prep-input-editarreceita {
  height: 60px;
}
#prep-input-editarreceita textarea {
  min-width: 40px;
  resize: none;
}
textarea {
  width: 100%;
  height: 100%;
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
#portions-editarreceita,
#prep-time-editarreceita,
#difficulty-editarreceita {
  border-radius: 0 36px 36px 0;
}
.input-label-editarreceita {
  border-radius: 36px 0 0 36px !important;
}
#submit-button-editarreceita {
  background-color: white;
  font-weight: bold;
  border: 1px solid gray !important;
  color: black;
  margin: 0 !important;
}
#prep-button-editarreceita {
  background-color: lightgray;
  border: 1px solid gray !important;
  color: black;
}
.form {
  align-items: center;
  justify-content: center;
}
#easy-editarreceita {
  background-color: #b1ff62;
}
#medium-editarreceita {
  background-color: #ffe132;
}
#hard-editarreceita {
  background-color: #fc1d00;
}
#super-editarreceita {
  background-color: #191919;
}
#prep-mode-editarreceita div div {
  border-radius: 18px !important;
}
#prep-editarreceita .jumbotron {
  height: 460px !important;
}
</style>