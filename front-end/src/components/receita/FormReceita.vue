<template>
  <div class="container">
    <div class="container">
      <h3>Inserindo Sua Receita</h3>
      {% include 'parciais/_messages.html' %}
      <form enctype="multipart/form-data" method="POST">
        {% csrf_token %}
        <div class="form-group" id="form_receita_nome_receita">
          <label>Nome da receita:</label>
          {{ receitaform.nome_receita | as_crispy_field }}
        </div>

        <div class="form-group" id="form_receita_fotos">
          <label for="inputAddress2">Fotos:</label>
          {{ receitaform.fotos | as_crispy_field }}
        </div>

        <div class="form-row">
          <div class="form-group col-md-6" id="form_receita_ingredientes">
            <label for="inputPassword4">Ingredientes</label>
            {{ ingredienteform.nome_ingrediente | as_crispy_field }}
            {{ ingredienteform.unidade_medida_ingrediente | as_crispy_field }}
            {{ ingredienteform.quantidade_ingrediente | as_crispy_field }}
          </div>
          <div
            class="form-group col-md-6"
            id="form_receita_caracteristicas_gerais"
          >
            <label for="inputPassword4">Características gerais</label>
            <div id="form_receita_caracteristicas_gerais_container">
              <div>
                {{ receitaform.sabor_receita | as_crispy_field }}
                {{ receitaform.categoria | as_crispy_field }}
              </div>
              <div>
                <label for="porcoes">Porções</label>
                {{ receitaform.porcoes | as_crispy_field }}

                <label for="tempo_preparo">Tempo de preparo</label>
                {{ receitaform.tempo_preparo | as_crispy_field }}

                {{ receitaform.tempo_unidade_medida | as_crispy_field }}

                {{ receitaform.dificuldade | as_crispy_field }}
              </div>
            </div>
          </div>
        </div>

        <div class="form-row">
          <div class="form-group col-md-6" id="form_receita_modo-preparo">
            <label for="modo_preparo">Modo de preparo</label>
            {{ receitaform.modo_preparo | as_crispy_field }}
          </div>

          <div class="form-group col-md-6" id="form_receita_obs-adicionais">
            <label for="inputPassword4">Observações adicionais</label>
            {{ receitaform.observacoes_adicionais | as_crispy_field }}
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

#search-input-editarreceita {
  outline: none;
  box-shadow: none !important;
  border-radius: 36px 0 0 36px;
  width: 20vw;
}

#search-button-editarreceita {
  border-radius: 0 36px 36px 0;
  padding: 0 1em 0 1em;
  background-color: white;
  border: 1px solid gray;
  color: gray;
  margin-left: -1px;
}

#search-button-editarreceita i {
  vertical-align: middle;
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