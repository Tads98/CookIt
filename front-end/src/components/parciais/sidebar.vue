<template>
  <nav id="sidebar">
    <button onclick="Close(sidebar)" class="btn sidebar-close">
        <i class="fas fa-times"></i>
    </button>
    <form method="GET" action="{% url 'receita:busca' %}">
        <div id="order-by">
            <div class="form-group">
                <label class="input-group-text input-label-sidebar">Ordenar:</label>
                <select class="form-control custom-select">
                    <option>Nome</option>
                    <option>Visualizações</option>
                    <option>Avaliações</option>
                    <option>Mais recente</option>
                    <option>Mais antigo</option>
                </select>
            </div>
            <h4 class="stars-sidebar">
                <span class="fa fa-star"></span>
                <span class="fa fa-star"></span>
                <span class="fa fa-star"></span>
                <span class="fa fa-star"></span>
                <span class="fa fa-star"></span>
            </h4>
        </div>
        <div id="intel">
            <div class="form-group">
                <label class="input-group-text input-label-sidebar">Porções</label>
                <input class="form-control" id="portions" type="number" min="1" name="porcoes">
            </div>
            <div class="form-group">
                <label class="input-group-text input-label-sidebar">Tmp de prep</label>
                <input id="prep-time" type="time" class="form-control">
            </div>
            <div class="form-group">
                <label class="input-group-text input-label-sidebar">Dificuldade</label>
                <select id="difficulty" name="dificuldade" class="form-control custom-select">
                    <option value="F">Fácil</option>
                    <option value="M">Médio</option>
                    <option value="D">Difícil</option>
                    <option value="C">Super</option>
                </select>
            </div>
            <div class="form-group">
                <h6><b>Sabor:</b></h6>
                <div class="form-check">

                    <!--TODO: implementar como receber no backend dois valores ao mesmo tempo-->
                    <span>
                        <label>
                            <input type="checkbox" name="sabor" value="D">
                            <i class="a-icon a-icon-checkbox"></i>
                        </label>
                        <span>Doce</span>
                    </span>
                    <br>
                    <span>
                        <label>
                            <input type="checkbox" name="sabor" value="S">
                            <i class="a-icon a-icon-checkbox"></i>
                        </label>
                        <span>Salgado</span>
                    </span>

                </div>
            </div>
        </div>
        <div id="categories" class="form-group">
            <h6><b>Categorias:</b></h6>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="">
                <label class="form-check-label" for="defaultCheck1">
                    Café da manhã
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="">
                <label class="form-check-label" for="defaultCheck1">
                    Almoço
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="">
                <label class="form-check-label" for="defaultCheck1">
                    Lanche
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="">
                <label class="form-check-label" for="defaultCheck1">
                    Janta
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="">
                <label class="form-check-label" for="defaultCheck1">
                    Sobremesas
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="">
                <label class="form-check-label" for="defaultCheck1">
                    Bebidas
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="">
                <label class="form-check-label" for="defaultCheck1">
                    Vegana
                </label>
            </div>
        </div>
        <button class="search-button btn btn-primary" class="btn btn-success" type="submit">
            Filtrar
        </button>
    </form>
</nav>
</template>

<script>
export default {
    name: 'Sidebar'
}
</script>

<style>
    /* Sidebar */

    #sidebar {
        padding: 1em;
        width: 12%;
        background-color: #F3EFEF;
        border-right: 1px solid black;
    }

    .stars-sidebar {
        font-size: 1em;
    }

    #order-by {
        border-bottom: 1px solid black;
        padding-bottom: 1em;
    }

    #intel,
    #categories {
        padding-top: 1em;
    }

    #intel {
        border-bottom: 1px solid black;
    }

    #sidebar .input-label-sidebar {
        border-radius: 1em 1em 0 0;
        margin-bottom: -1px;
    }

    #sidebar label,
    #sidebar select,
    #sidebar input {
        font-size: 12px;
        text-align: center;
        padding: 0;
    }

    #sidebar select,
    #sidebar input {
        border-radius: 0 0 1em 1em;
    }
</style>