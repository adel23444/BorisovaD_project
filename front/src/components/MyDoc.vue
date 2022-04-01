<template>
  <div class="my_zayv">
    <div style="display: flex; justify-content: space-between">
      <h1 style="width: 50%; margin-left: 3%">Документы</h1>
      <div class="zayv_buttons" @click="changeStage($event);">
        <div class="button_zay" v-on:click="type_change('')">
          <p style="margin-bottom: 2%; pointer-events: none">Все</p>
          <hr style="pointer-events: none;">
        </div>
        <div class="button_zay" v-on:click="type_change(2)">
          <p style="margin-bottom: 2%; pointer-events: none">Транспорт</p>
          <hr style="pointer-events: none;">
        </div>
        <div class="button_zay" v-on:click="type_change(1)">
          <p style="margin-bottom: 2%; pointer-events: none">Канцелярия</p>
          <hr style="pointer-events: none;">
        </div>
        <div class="button_zay" v-on:click="type_change(3)">
          <p style="margin-bottom: 2%; pointer-events: none">Неисправность</p>
          <hr style="pointer-events: none;">
        </div>
        <div>
            <img style="width: 2.5em; margin-top: 1em;" src="../assets/new_zay.svg" alt="new">
        </div>
      </div>
    </div>

    <table>
      <thead>
      <th>
        <div class="head">№ Заявки</div>
      </th>
      <th>
        <div class="head">Вид</div>
      </th>
      <th>
        <div class="head">Исполнитель</div>
      </th>
      <th> <div class="head">Статус</div></th>
      <th> <div class="head">Документы</div></th>
      </thead>
      <tbody>
      <tr v-for="doc in docas" :key="doc.id">
        <td class="t_body">{{doc.id}}</td>
        <td class="t_body">{{types(doc.type)}}</td>
        <td class="t_body">{{doc.isp}}</td>
        <td class="t_body">{{statuses(doc.status_zay)}}</td>
        <td v-if="doc.links.length > 0" style="display: flex; flex-direction: row;" class="t_body">
          <div style="display: flex; width: 100%">
            <div style="display: flex; margin-left: 5%;" v-for="link in doc.links" :key="link">
              <img style="width: 1.2em;" src="../assets/download.svg" alt="download">
              <p style="margin-left: 5%; font-size: 12px">{{Object.values(link)[0]}}<a style="text-decoration: none"></a></p>
            </div>
          </div>

        </td>
        <td v-else class="t_body"></td>
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
      docs: [
        {
          id: 154,
          type: 1,
          status_zay: 1,
          isp: 'Петров П.П.',
          links: []
        },
        {
          id: 155,
          type: 1,
          status_zay: 2,
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
          id: 156,
          type: 2,
          status_zay: 2,
          isp: 'Петров П.П.',
          links: [
            {
              name: 'Акт о выполненных работах'
            }
          ]
        },
        {
          id: 157,
          type: 3,
          status_zay: 2,
          isp: 'Петров П.П.',
          links: [
            {
              name: 'Акт о выполненных работах'
            }
          ]
        },
        {
          id: 158,
          type: 3,
          status_zay: 2,
          isp: 'Петров П.П.',
          links: [
            {
              name: 'Акт о выполненных работах'
            }
          ]
        }
      ],
      type: ''
    }
  },
  computed: {
    docas () {
      let zayavka = [...this.docs]
      if (this.type) {
        zayavka = this.docs.filter(zayavka => zayavka.type === this.type)
      }

      return zayavka
    },
    isUser ( ) {
      return this.$store.getters['auth/User'] === 'user'
    },
    isBukh ( ) {
      return this.$store.getters['auth/User'] === 'bukh'
    }
  },
  methods: {
    types(type) {
      if (type === 1) {
        return "Канцелярия"
      }
      if (type === 2) {
        return "Транспорт"
      }
      if (type === 3) {
        return "Неисправность"
      }
    },
    statuses(status) {
      if (status === 1) {
        return "Активная"
      }
      else {
        return "Завершена"
      }
    },
    type_change (num) {
      this.type = num
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