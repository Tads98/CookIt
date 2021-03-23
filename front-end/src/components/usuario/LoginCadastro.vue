<template>
  <div class="bg" style="">
    <div class="container" style="background: none">
      <a href="">
        <img
          class="rounded mx-auto d-block"
          src=""
          alt="Logo"
          height="90px"
          style="margin: 1em"
        />
      </a>
      <div class="row">
        <div class="col-lg mt-3" id="login">
          <div class="row mb-3 no-gutters">
            <div class="col">
              <button id="login-button" onclick="loginOpen()">Login</button>
            </div>
            <div class="col">
              <button id="cadastro-button" onclick="cadastroOpen()">
                Cadastro
              </button>
            </div>
          </div>

          <form id="login-form" method="POST" action="">
            <div class="form-group">
              <input
                type="text"
                name="username"
                class="form-control rounded-pill"
                id="InputUsuario1"
                aria-describedby="usuarioHelp"
                placeholder="Nome de Usuário"
              />
            </div>
            <div class="form-group">
              <input
                name="password"
                type="password"
                class="form-control rounded-pill"
                id="exampleInputPassword1"
                placeholder="Senha"
              />
            </div>
            <button
              type="submit"
              class="btn btn-primary btn-block btn-lg rounded-pill"
            >
              Entrar
            </button>
          </form>
          <form id="cadastro-form" method="POST" action="">
            <h3>Atualizar dados</h3>

            <div class="crispy-form">
              <button
                type="submit"
                class="btn btn-primary btn-block btn-lg rounded-pill"
              >
                Cadastrar
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Cadastro_Nova",
};
</script>

<style scoped>
body {
  width: 100%;
  height: 100%;
  position: fixed;
}

.bg {
  margin-top: -70px !important;
  background-size: contain;
  width: 100%;
  height: 100%;
}

.container {
  width: 420px;
}

#login,
#cadastro {
  background-color: white;
  border-radius: 1em;
  padding: 0 !important;
  padding-bottom: 1em !important;
}

/*    h3 {
        background-color: grey;
        border-top-left-radius: 0.5em;
        border-top-right-radius: 0.5em;
        padding: 0.5em;
    }
*/

#login form {
  padding-left: 1em !important;
  padding-right: 1em;
}

#cadastro-form {
  display: none;
}

button {
  width: 100%;
}

#login-button {
  border-top-left-radius: 0.5em;
  background-color: gray;
}

#cadastro-button {
  border-top-right-radius: 0.5em;
  background-color: lightgray;
}

#login-button,
#cadastro-button {
  border: none;
  font-size: 2em;
  font-weight: bold;
  padding: 0.1em;
  border: none;
  outline: none;
}
</style>