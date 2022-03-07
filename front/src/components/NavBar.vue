<template>
  <div class="nav_bar">
    <div class="user_info">
      <img src="../assets/person.svg" alt="person">
      <div class="user">Пользователь: <br> {{ user }}</div>
    </div>
    <div class="space"></div>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      user: "Борисова Д.М."
    }
  }
}
</script>

<style scoped>
  .nav_bar {
    background: linear-gradient(90deg,#6F0681, #2E079E);
    padding: 1.5% 2%;
    display: flex;
  }
  .user_info {
    display: flex;
    width: 20%;
    align-items: center;
  }
  .user {
    color: white;
    font-size: 1.5vh;
    margin: 0 5%;
    font-weight: 600;
  }
  .space {
    width: 60%;
  }
</style>