<template>
  <div style="background-color: #FEF6FF">
    <form>
    <h3>Авторизация</h3>
    <div>
      <input v-model="login" class="inputs" type="text" placeholder="Пользователь">
      <br>
      <input v-model="password" class="inputs"  type="password" placeholder="Пароль">
      <br>
      <router-link to="/">
        <button class="input_button" @click="login_to">Войти</button>
      </router-link>

    </div>

  </form>
  </div>
</template>

<script>
export default {
  name: "Login_Wind",
  data(){
    return {
      login: "",
      password: ""
    }
  },
  methods: {
    login_to ( ) {
      let user = {
        "username": this.login,
        "password": this.password
      }
      // if(this.login === "admin" && this.password === "admin") {
      //   user.name = "Светлов С.С."
      //   user.token = "admin"
      // }
      // else if (this.login === "user" && this.password === "user") {
      //   user.name = "Борисова Д.М."
      //   user.token = "user"
      // }
      // else if (this.login === "bukh" && this.password === "bukh") {
      //   user.name = "Петров Б.П."
      //   user.token = "bukh"
      // }
      // else if (this.login === "zav" && this.password === "zav") {
      //   user.name = "Иванова И.И."
      //   user.token = "zav"
      // }
      this.$store.dispatch('auth/loginUser', user)
    }
  }
}
</script>

<style scoped>
  .inputs {
    margin: 3%;
    border: none;
    box-shadow: inset 0 -1px 0 rgb(153 168 192 / 80%);
    box-sizing: border-box;
    display: inline-block;
    outline: 0;
    width: 25vw;
  }
  .inputs ::-webkit-input-placeholder {
    font-size: 18px;
    color: #3B39498C;
  }
  form {
    top: 25%;
    left: 2vh;
    right: 2vw;
    bottom: 2vh;
    position: absolute;
  }
  button {
    background: linear-gradient(90deg,#6F0681, #2E079E);
    color: white;
    width: 27%;
    height: 2em;
    box-shadow: 2px 2px 14px rgba(43.5, 2.4, 50.6, 0.53);
    border-radius: 5px;
  }
</style>