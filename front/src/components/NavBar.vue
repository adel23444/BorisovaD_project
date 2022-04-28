<template>
  <div>
    <div class="nav_bar">
      <div class="user_info">
        <img src="../assets/person.svg" alt="person">
        <div class="user">Пользователь: <br> {{ user }}</div>
      </div>
      <div class="space"></div>
      <div v-if="isBukh" class="nav_buttons" @click="changeStage($event)">
        <button value="doc" class="clicked_button" v-on:click="click('/doc')">Документы</button>
        <button value="zay" style="margin-left: 10px" v-on:click="click('/')" class="clicked_button">Заявки</button>
      </div>
      <div v-if="isAdmin" class="nav_buttons" @click="changeStage($event)">
        <button value="zay" style="margin-left: 10px" class="clicked_button" v-on:click="click('/')" >Заявки</button>
        <button value="doc" class="clicked_button" v-on:click="click('/doc')">Аналитика</button>
        <button value="zay" style="margin-left: 10px" class="clicked_button" v-on:click="click('/users')" >Пользователи</button>
      </div>
      <div class="space"></div>
      <div class="logout" style="cursor: pointer" v-on:click="logout">
        <p>Выйти</p>
        <img src="../assets/logout.svg" style="width: 50px; height: 52px; margin-left: 10%" alt="logout">
      </div>
    </div>

  </div>

</template>

<script>
export default {
  name: "NavBar",
  computed: {
    isBukh ( ) {
      return this.$store.getters['auth/User'] === 'bukh'
    },
    isAdmin () {
      return this.$store.getters['auth/User'] === 'admin'
    },
    user () {
      return this.$store.getters['auth/UserName']
    }
  },
  methods: {
    changeStage (event) {
      const elements = document.querySelectorAll('.clicked_button')
      console.log(elements)
      console.log(event)
      elements.forEach((element)=>{
        if (event.target.value === element.value){
          element.style.backgroundColor = 'rgba(255, 255, 255, 0.25)'
        }
        else {
          element.style.backgroundColor = '#50068f'
        }
        console.log(element)
      })
    },
    click( param ) {
      this.$router.push(param)
    },
    logout () {
      this.$store.dispatch('auth/logout')
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
  .nav_bar {
    background: linear-gradient(90deg,#6F0681, #2E079E);
    display: flex;
    justify-content: space-around;
  }
  .nav_buttons {
    display: flex;
    justify-content: center;
    align-items: end;
  }
  .user_info {
    display: flex;
    width: 20%;
    align-items: center;
    padding: 1.5% 2%;
  }
  .user {
    color: white;
    font-size: 12px;
    margin: 0 5%;
    font-weight: 600;
  }
  .space {
    width: 19%;
  }
  .logout {
    display: flex;
    color: white;
    align-items: center;
    font-size: 16px;
    font-weight: 600;
  }
  .clicked_button {
    color: white;
    font-size: 18px;
    background-color: rgba(255, 255, 255, 0.25);
    border-bottom: none;
    padding: 3% 10%;
    border: 2px solid #FFF;
    box-sizing: border-box;
    border-top-left-radius: 14px;
    border-top-right-radius: 14px;
    font-weight: 700;
    border-bottom: none;
    height: 60%;
    margin-left: 5px;
  }
</style>