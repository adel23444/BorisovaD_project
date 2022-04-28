<template>
  <div class="my_zayv">
    <div style="display: flex; justify-content: space-between">
      <h1 style="width: 50%; margin-left: 3%">Список пользователей</h1>
      <div style="display: flex; align-items: center; ">
        <p>Создать пользователя</p>
        <img style="width: 2.5em; " src="../assets/new_zay.svg" alt="new">
      </div>
    </div>

    <table>
      <thead>
      <th>
        <div class="head">Учетная запись</div>
      </th>
      <th>
        <div class="head">Пользователь</div>
      </th>
      <th>
        <div class="head">Роль (должность)</div>
      </th>
      <th> <div class="head">Права</div></th>
      <th> <div class="head">Пароль</div></th>
      </thead>
      <tbody>
      <tr v-for="user in users" :key="user.id">
        <td class="t_body">{{user.fio}}</td>
        <td class="t_body">{{user.full_fio}}</td>
        <td class="t_body">{{user.role}}</td>
        <td class="t_body">{{user.rules}}</td>
        <td class="t_body">{{user.password}}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>

export default {
  name: "MyDoc",
  data() {
    return {
      users: [
        {
          id: 1,
          fio: 'Иванова И.И.',
          full_fio: 'Иванова Ирина Ивановна',
          role: 'Бухгалтер',
          rules: 'Создвние заявок, назначение исполнителей, создание документов',
          password: 'qwerty123'
        },
        {
          id: 2,
          fio: '',
          full_fio: '',
          role: '',
          rules: '',
          password: ''
        },
        {
          id: 3,
          fio: '',
          full_fio: '',
          role: '',
          rules: '',
          password: ''
        },
        {
          id: 3,
          fio: '',
          full_fio: '',
          role: '',
          rules: '',
          password: ''
        },
        {
          id: 3,
          fio: '',
          full_fio: '',
          role: '',
          rules: '',
          password: ''
        },
        {
          id: 3,
          fio: '',
          full_fio: '',
          role: '',
          rules: '',
          password: ''
        },
      ],
      type: ''
    }
  },
  computed: {

    isUser ( ) {
      return this.$store.getters['auth/User'] === 'user'
    },
    isBukh ( ) {
      return this.$store.getters['auth/User'] === 'bukh'
    }
  },
  methods: {
    changeStage (event) {
      const elements = document.querySelectorAll('.button_zay')
      elements.forEach((element)=>{
        if (event.target === element){
          element.style.color = 'rgba(59, 22, 87, 1)'
        }
        else {
          element.style.color = 'rgba(59, 22, 87, 0.7)'
        }
      })
    }
  }
}
</script>

<style scoped>
  .my_zayv {
    margin: 2%;
    text-align: left;
    color: #3B1657;
  }

  table {
    border-collapse: collapse;
    width: 100%;
  }
  th {
    color: #3B1657;
    font-weight: 700;
    background-color: rgba(46, 7, 158, 0.2);
    border: 2px solid rgba(46, 7, 158, 0.3);
    border-top: none;
  }
  th:first-child {
    border-top-left-radius: 14px;
    border-left: none;
  }
  th:last-child {
    border-top-right-radius: 14px;
    border-right: none;
  }
  .head {
    padding: 2%;
    text-align: center;
  }
  .t_body {
    background-color: white;
    padding: 2% 0%;
    text-align: center;
    border: 2px solid rgba(46, 7, 158, 0.3);
    border-top: none;
    color: #3B1657;
    font-weight: 400;
  }
</style>