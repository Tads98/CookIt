<template>
  <nav class="navbar navbar-expand-lg d-flex justify-content-between fixed-top">
    <a class="navbar-brand" href="{% url 'receita:limpar' %}">
      <img src="{% static 'imgs/cookit_logo.svg' %}" alt="Logo" height="36px" />
    </a>
    <form
      class="form-inline <!--mr-auto my-2 my-lg-0-->"
      method="GET"
      action="{% url 'receita:busca' %}"
    >
      <div id="search" class="input-group">
        <!--TODO: implementar uma forma de limpar sessões neste campo abaixo-->
        <input
          id="search-input"
          class="form-control"
          type="search"
          placeholder="Busque sua receita"
          aria-label="Busca"
          name="termo"
          value="{{ request.GET.termo }}"
        />
        <button id="search-button" class="btn btn-success" type="submit">
          <i class="fas fa-search"></i>
        </button>
      </div>
    </form>

    <div class="" id="navbarSupportedContent">
      <ul class="nav">
        {% csrf_token %} {% if request.user.is_authenticated %}
        <li class="nav-item dropdown">
          <a
            class="nav-link"
            href="{% url 'receita:cadastrar_receita' %}"
            role="button"
          >
            <h5><i style="font-size: 25px" class="fas fa-book"></i></h5>
          </a>
        </li>
        <li class="nav-item dropdown">
          <a
            class="nav-link"
            href="#"
            id="navbarDropdown"
            role="button"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >
            <h5><i style="font-size: 25px" class="fas fa-bell"></i></h5>
          </a>
          <div
            class="dropdown-menu dropdown-menu-right"
            aria-labelledby="navbarDropdown"
          >
            <a class="dropdown-item" href="#">Action</a>
            <a class="dropdown-item" href="#">Another action</a>
            <div class="dropdown-divider"></div>
            <a id="nav-icon" class="dropdown-item" href="#"
              >Something else here</a
            >
          </div>
        </li>
        <li class="nav-item dropdown">
          <a
            class="nav-link"
            href="#"
            id="navbarDropdown"
            role="button"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >
            <h5><i style="font-size: 25px" class="fas fa-heart"></i></h5>
          </a>
          <div
            class="dropdown-menu dropdown-menu-right"
            aria-labelledby="navbarDropdown"
          >
            <a class="dropdown-item" href="#">Action</a>
            <a class="dropdown-item" href="#">Another action</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#">Something else here</a>
          </div>
        </li>
        <li class="nav-item dropdown">
          <a
            class="nav-link"
            href="#"
            id="navbarDropdown"
            role="button"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >
            <img
              src="{% static 'imgs/cookit_user.svg' %}"
              alt=""
              height="25px"
            />
          </a>

          <div
            class="dropdown-menu dropdown-menu-right"
            aria-labelledby="navbarDropdown"
          >
            <a class="dropdown-item" href="{% url 'usuario:criar' %}">Perfil</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="{% url 'usuario:logout' %}">Sair</a>
          </div>
        </li>
        <html>
          {% else %}
          <button
            id="login-button"
            class="btn btn-primary"
            onclick="location.href = '{% url 'usuario:criar' %}';loginOpen()"
          >
            Login
          </button>
          <!--<button id="cadastro-button" class="btn btn-secondary"
                onclick="location.href = '{% url 'usuario:criar' %}';cadastroOpen()">
                Cadastro
            </button>-->
        </html>
      </ul>

      {% endif %}
    </div>
  </nav>
</template>

<script>
export default {};
</script>

<style>
.navbar {
  background-color: #f3efef !important;
  border-bottom: 1px solid #707070;
}

#nav-icon {
  color: black;
  vertical-align: middle;
}

.nav-link {
  padding: 0 1vw 0 1vw;
}

.navbar-brand {
  align-self: center;
  justify-content: center;
  font-size: 0;
}

#nav-icon-span {
  font-size: 12px;
}

#search-input {
  outline: none;
  box-shadow: none !important;
  border-radius: 36px 0 0 36px;
  width: 20vw;
}

#search-button {
  padding: 0 1em 0 1em;
  background-color: white;
  border: 1px solid gray;
  color: gray;
  margin-left: -1px;
  border-radius: 0 36px 36px 0 !important;
}

#search-button i {
  vertical-align: middle;
}

i {
  text-decoration: none !important;
  color: black;
}
</style>