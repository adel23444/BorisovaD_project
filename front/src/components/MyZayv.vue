<template>
  <div class="my_zayv">
    <div style="display: flex; justify-content: space-between">
      <h1 v-if="isUser||isAdmin" style="width: 50%; margin-left: 3%">Мои заявки</h1>
      <h1 v-if="isBukh" style="width: 50%; margin-left: 3%">Заявки</h1>
      <div class="zayv_buttons" @click="changeStage($event);">
        <div v-if="isBukh" class="button_zay" v-on:click="status_change('my')">
          <p style="margin-bottom: 2%; pointer-events: none">Мои</p>
          <hr style="pointer-events: none;">
        </div>
        <div v-if="isBukh" class="button_zay" v-on:click="status_change('non_nazn')">
          <p style="margin-bottom: 2%; pointer-events: none">Неназначенные</p>
          <hr style="pointer-events: none;">
        </div>
        <div class="button_zay" v-on:click="status_change('')">
          <p style="margin-bottom: 2%; pointer-events: none">Все</p>
          <hr style="pointer-events: none;">
        </div>
        <div class="button_zay" v-on:click="status_change(1)">
          <p style="margin-bottom: 2%; pointer-events: none">Текущие</p>
          <hr style="pointer-events: none;">
        </div>
        <div class="button_zay" v-on:click="status_change(2)">
          <p style="margin-bottom: 2%; pointer-events: none">Завершенные</p>
          <hr style="pointer-events: none;">
        </div>
        <div>
          <router-link to="/new">
            <img style="width: 2.5em; margin-top: 1em;" src="../assets/new_zay.svg" alt="new">
          </router-link>
        </div>
      </div>
    </div>

    <div class="list_zay">
      <ZayAvka v-for="(propert, $index) in zayavka" :key="$index"
               :propert="propert"
      />
    </div>
  </div>
</template>

<script>
import ZayAvka from "@/components/ZayAvka";
export default {
  name: "MyZayv",
  components: {ZayAvka},
  data() {
    return {
      zayvaks: [
        {
          type: 1,
          addr: "Проспект Победы, д. 152",
          punkt: "Почта РФ",
          data_dost: "20.12.2021",
          vrem: "14:00",
          num: 180,
          date: "19.12.2021",
          isp: ''
        },
        {
          type: 0,
          tov_name: "Бумага А4",
          count: 2,
          cena: 200,
          num: 154,
          status_zay: 2,
          date: "17.12.2021",
          isp: 'Иванова И.И.',
          links: [
            {
              name: 'Акт на выдачу'
            },
            {
              name: 'Акт на списание'
            }
          ]
        },
        {
          type: 2,
          comment: "Не работает кондиционер",
          date: "11.11.2021",
          status_zay: 1,
          num: 130,
          isp: 'Петров Б.П.',
          links: [
            {
              name: 'Акт о выполненных работах'
            }
          ]
        },
        {
          type: 2,
          comment: "Не работает принтер",
          date: "11.11.2021",
          status_zay: 2,
          num: 130,
          isp: 'Петров Б.П.',
          links: [
            {
              name: 'Акт о выполненных работах'
            }
          ]
        }
      ],
      status: ''
    }
  },
  computed: {
    user_filter () {
      let zayavka = [...this.zayvaks]
      if (this.isUser) {
        zayavka = this.zayvaks.filter(zayavk => zayavk.isp !== '')
      }
      return zayavka
    },
    zayavka () {
      let zayavka = this.user_filter
      if (this.status === 'my') {
        let name = this.$store.getters['auth/UserName']
        zayavka = zayavka.filter(zaya => zaya.isp === name)
        console.log(zayavka)
      }
      else if (this.status === 'non_nazn') {
        zayavka = zayavka.filter(zayavk => zayavk.isp === '')
        console.log(zayavka)
      }
      else if (this.status) {
        zayavka =  this.zayvaks.filter(zayvak => zayvak.status_zay === this.status)
      }
      return zayavka
    },
    isUser ( ) {
      return this.$store.getters['auth/User'] === 'user'
    },
    isBukh ( ) {
      return this.$store.getters['auth/User'] === 'bukh'
    },
    isAdmin () {
      return this.$store.getters['auth/User'] === 'admin'
    }
  },
  methods: {
    status_change (num) {
      this.status = num
    },
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
  .list_zay {
    margin: 3% 0;
  }
  .zayv_buttons {
    display: flex;
    justify-content: space-evenly;
    width: 70%;
  }
  .button_zay {
    color: rgba(59, 22, 87, 0.7);
    font-weight: 700;
    font-size: 20px;
    cursor: pointer;
  }
  .active_butt {
    color: rgba(59, 22, 87, 1);
    font-weight: 700;
    font-size: 20px;
    cursor: pointer;
  }
</style>