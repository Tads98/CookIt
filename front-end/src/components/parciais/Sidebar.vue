<template>
  <nav id="sidebar">
    <button onclick="Close(sidebar)" class="btn sidebar-close">
      <i class="fas fa-times"></i>
    </button>
    <form method="GET" action="">
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
          <input
            class="form-control"
            id="portions"
            type="number"
            min="1"
            name="porcoes"
          />
        </div>
        <div class="form-group">
          <label class="input-group-text input-label-sidebar"
            >Tmp de prep</label
          >
          <input id="prep-time" type="time" class="form-control" />
        </div>
        <div class="form-group">
          <label class="input-group-text input-label-sidebar"
            >Dificuldade</label
          >
          <select
            id="difficulty"
            name="dificuldade"
            class="form-control custom-select"
          >
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
                <input type="checkbox" name="sabor" value="D" />
                <i class="a-icon a-icon-checkbox"></i>
              </label>
              <span>Doce</span>
            </span>
            <br />
            <span>
              <label>
                <input type="checkbox" name="sabor" value="S" />
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
          <input class="form-check-input" type="checkbox" value="" />
          <label class="form-check-label" for="defaultCheck1">
            Café da manhã
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" />
          <label class="form-check-label" for="defaultCheck1"> Almoço </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" />
          <label class="form-check-label" for="defaultCheck1"> Lanche </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" />
          <label class="form-check-label" for="defaultCheck1"> Janta </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" />
          <label class="form-check-label" for="defaultCheck1">
            Sobremesas
          </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" />
          <label class="form-check-label" for="defaultCheck1"> Bebidas </label>
        </div>
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" />
          <label class="form-check-label" for="defaultCheck1"> Vegana </label>
        </div>
      </div>
      <button class="search-button btn btn-primary" type="submit">
        Filtrar
      </button>
    </form>
  </nav>
</template>

<script>
import axios from "axios";

  export default {
    data: function () {
      return {
        breakfast: [],
        lunch: [],
        sneak: [],
        dinner: [],
        dessert: [],
        drinks: [],
        vegan: [],
        sabor: [
        {
          char: "S",
          text: "Salgado",
        },
        {
          char: "D",
          text: "Doce",
        },
      ],
        loading: true,
        selected: {
            breakfast: [],
            lunch: [],
            sneak: [],
            dinner: [],
            dessert: [],
            drinks: [],
            sabor: [
            {
              char: "S",
              text: "Salgado",
            },
            {
              char: "D",
              text: "Doce",
            },
          ],
        }
      }
    },

    mounted() {
      this.loadBreakfast();
      this.loadLunch();
      this.loadSneak();
      this.loadDinner();
      this.loadDessert();
      this.loadDrinks();
      this.loadVegan();
      this.loadSabor();
    },

    watch:{
      selected: {
        handler: function() {
            this.loadBreakfast();
            this.loadLunch();
            this.loadSneak();
            this.loadDinner();
            this.loadDessert();
            this.loadDrinks();
            this.loadVegan();
            this.loadSabor();
        },
        deep: true
      }
    },

    methods: {
      loadBreakfast: function () {
        axios.get('/api/breakfast', {
                params: _.omit(this.selected, 'breakfast')
        })
        .then((response) => {
          this.categories = response.data.data;
        })
        .catch(function (error){
          console.log(error);
        });
      },
      
      loadLunch: function () {
        axios.get('/api/lunch', {
                params: _.omit(this.selected, 'lunch')
        })
        .then((response) => {
          this.lunch = response.data.data;
          this.loading = false;
        })
        .catch(function (error){
          console.log(error);
        });
      },

      loadSneak: function () {
        axios.get('/api/sneak', {
                params: _.omit(this.selected, 'sneak')
        })
        .then((response) => {
          this.sneak = response.data.data;
          this.loading = false;
        })
        .catch(function (error){
          console.log(error);
        });
      },

      loadDinner: function () {
        axios.get('/api/dinner', {
                params: _.omit(this.selected, 'dinner')
        })
        .then((response) => {
          this.dinner = response.data.data;
          this.loading = false;
        })
        .catch(function (error){
          console.log(error);
        });
      },

      loadDessert: function () {
        axios.get('/api/dessert', {
                params: _.omit(this.selected, 'dessert')
        })
        .then((response) => {
          this.dessert = response.data.data;
          this.loading = false;
        })
        .catch(function (error){
          console.log(error);
        });
      },

      loadDrink: function () {
        axios.get('/api/drink', {
                params: _.omit(this.selected, 'drink')
        })
        .then((response) => {
          this.drink = response.data.data;
          this.loading = false;
        })
        .catch(function (error){
          console.log(error);
        });
      },

      loadVegan: function () {
        axios.get('/api/vegan', {
                params: _.omit(this.selected, 'vegan')
        })
        .then((response) => {
          this.vegan = response.data.data;
          this.loading = false;
        })
        .catch(function (error){
          console.log(error);
        });
      }
    },

    loadSabor: function () {
        axios.get('/api/sabor', {
                params: _.omit(this.selected, 'sabor')
        })
        .then((response) => {
          this.sabor = response.data;
          this.loading = false;
        })
        .catch(function (error){
          console.log(error);
        });
      }
    };
</script>

<style scoped>
/* Sidebar */

#sidebar {
  padding: 1em;
  width: 12%;
  background-color: #f3efef;
  border-right: 1px solid black;
  float: left;
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