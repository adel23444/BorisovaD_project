<template>
  <div class="new_zay">
    <h2>Новая заявка</h2>
    <div style="margin: 3%">
      <h3>Выберите вид заявки</h3>
      <select  v-model="selected_vid" v-on:click="check_selected">
        <option value="" disabled selected hidden>Вид заявки</option>
        <option v-for="param in select_params" :key="param.value" v-bind:value="param.value">
          {{param.label}}
        </option>
      </select>

      <div style="margin-top: 2%" v-if="selected_vid==='trans'">
        <div class="num_date">
          <p>№</p>
          <input v-model="num" class="input_num" type="number">
          <div class="space"></div>
          <p>от</p>
          <input class="input_num" type="date" v-model="currDate">
        </div>
        <br>
        <div>
          <table>
            <tr>
              <td style="width: 17%">
                <div class="data_block"></div>
                <p>Сотрудник:</p>
              </td>
              <td>
                <div class="data_block"><input class="input_main" type="text"></div>

              </td>
              <td style="width: 17%">
                <div class="data_block"></div>
                <p>Вид заявки:</p>
              </td>
              <td>
                <div class="data_block"><input class="input_main" type="text"></div>

              </td>
            </tr>
            <tr>
              <td>
                <div class="data_block"></div>
                <p>Отдел:</p>
              </td>
              <td>
                <div class="data_block"><input class="input_main" type="text"></div>

              </td>
              <td>
                <div class="data_block"></div>
                <p>Дата:</p>
              </td>
              <td>
                <div class="data_block"> <input class="input_main" type="date"></div>

              </td>
            </tr>
            <tr>
              <td>
                <div class="data_block"></div>
                <p>Кабинет:</p>
              </td>
              <td >
                <div class="data_block" >
                  <input class="input_main" type="number">
                </div>
              </td>
              <td>
                <div class="data_block"></div>
                <p>Время:</p>
              </td>
              <td>
                <div class="data_block">
                  <input class="input_main" type="time">
                </div>

              </td>
            </tr>
          </table>
        </div>
        <br> <br>
        <div style="display: flex; align-items: center">
          <p style="margin-right: 1%">Пункт назначения:</p>
          <input class="input_main" style="width: 69%; height: 50%" type="text">
        </div>
        <div>
          <p>Комментарий</p>
          <textarea rows="7" placeholder="Напишите комментарий..."></textarea>
        </div>
      </div>


      <div style="margin-top: 2%" v-else-if="selected_vid==='neisp'">
        <div class="num_date">
          <p>№</p>
          <input class="input_num" type="number">
          <div class="space"></div>
          <p>от</p>
          <input class="input_num" type="date" v-model="currDate">
        </div>
        <br>
        <div>
          <table>
            <tr>
              <td style="width: 17%">
                <div class="data_block"></div>
                <p>Сотрудник:</p>
              </td>
              <td>
                <div class="data_block"><input class="input_main" type="text"></div>
              </td>
              <td style="width: 17%">
                <div class="data_block"></div>
                <p>Вид заявки:</p>
              </td>
              <td>
                <div class="data_block"><input class="input_main" type="text"></div>
              </td>
            </tr>
            <tr>
              <td>
                <div class="data_block"></div>
                <p>Отдел:</p>
              </td>
              <td>
                <div class="data_block"><input class="input_main" type="text"></div>
              </td>
            </tr>
            <tr>
              <td>
                <div class="data_block"></div>
                <p>Кабинет:</p>
              </td>
              <td >
                <div class="data_block" >
                  <input class="input_main" type="number">
                </div>
              </td>
            </tr>
          </table>
        </div>
        <br> <br>
        <div>
          <p>Комментарий</p>
          <textarea rows="7" placeholder="Напишите комментарий..."></textarea>
        </div>
      </div>
      <div style="margin-top: 2%" v-if="this.selected_vid==='canc'">
        <div class="num_date">
          <p>№</p>
          <input class="input_num" type="number">
          <div class="space"></div>
          <p>от</p>
          <input class="input_num" type="date" v-model="currDate">
        </div>
        <br>
        <div>
          <table>
            <tr>
              <td style="width: 17%">
                <div class="data_block"></div>
                <p>Сотрудник:</p>
              </td>
              <td>
                <div class="data_block"><input class="input_main" type="text"></div>

              </td>
              <td style="width: 17%">
                <div class="data_block"></div>
                <p>Вид заявки:</p>
              </td>
              <td>
                <div class="data_block"><input class="input_main" type="text"></div>

              </td>
            </tr>
            <tr>
              <td>
                <div class="data_block"></div>
                <p>Отдел:</p>
              </td>
              <td>
                <div class="data_block"><input class="input_main" type="text"></div>
              </td>
            </tr>
            <tr>
              <td>
                <div class="data_block"></div>
                <p>Кабинет:</p>
              </td>
              <td >
                <div class="data_block" >
                  <input class="input_main" type="number">
                </div>
              </td>

            </tr>
          </table>
        </div>
        <br> <br>

        <table>
          <thead>
            <th><div class="head">№</div></th>
            <th> <div class="head">Наименование</div></th>
            <th> <div class="head">Количество, шт.</div></th>
            <th> <div class="head">Цена за ед., руб.</div></th>
            <th> <div class="head">Итого, руб.</div></th>
          </thead>
          <tbody>
            <tr v-for="tovar in tovars" :key="tovar.id">
              <td class="t_body">{{tovar.id}}</td>
              <td class="t_body">{{tovar.naim}}</td>
              <td class="t_body">{{tovar.kolvo}}</td>
              <td class="t_body">{{tovar.cena}}</td>
              <td class="t_body">{{tovar.itogo}}</td>
            </tr>
            <tr>
              <td class="t_body">{{curr_id+1}}</td>
              <td class="t_body"><input v-model="naim" class="input_table" type="text"></td>
              <td class="t_body"><input v-model="kolvo" class="input_table" type="number"></td>
              <td class="t_body"><input v-model="cena" class="input_table" type="number"></td>
              <td class="t_body">{{this.itogo}}</td>
            </tr>
          </tbody>
        </table>
        <div style="display: flex; flex-direction: row">
          <div @click="add_totovars">
            <img style="pointer-events: none" src="../assets/action_plus.svg" alt="plus">
          </div>
          <div @click="remove_tovfavorit
          ars">
            <img style="pointer-events: none" src="../assets/action_minus.svg" alt="minus">
          </div>
        </div>
      </div>
      <br> <br> <br>
      <div v-if="selected_vid!==''" class="buttons">
        <button @click="cancel" class="button_cancel">Отменить</button>
        <button @click="ok" class="button_ok">Отправить</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MakeZay",
  data () {
    return {
      select_params: [
        { value: 'trans', label: 'Транспорт' },
        { value: 'canc', label: 'Канцелярия' },
        { value: 'neisp', label: 'Неисправность' }
      ],
      canc_tovars: [],
      num: 0,
      naim: '',
      selected_vid: '',
      cena: 0,
      kolvo: 0,
      currDate: new Date().toLocaleDateString()
    }
  },
  computed: {
    curr_id () {
      return this.canc_tovars.length
    },
    itogo () {
      return this.cena*this.kolvo
    },
    tovars () {
      return this.canc_tovars
    }
  },
  created() {
    this.init()
  },
  methods: {
    init () {
      this.canc_tovars = [
        {
          id: 1,
          naim: "Бумага, листы",
          kolvo: 2,
          cena: 100,
          itogo: 200
        }
      ]
    },
    check_selected () {
      console.log(this.selected_vid)
    },
    cancel () {
      alert('Вы отменили заявку.')
      this.$router.push('/')
    },
    ok () {
      alert(`Заявка №${this.num} подтверждена!`)
      this.$router.push('/')
    },
    add_totovars () {
      this.canc_tovars.push({
        id: this.curr_id+1,
        naim: this.naim,
        cena: this.cena,
        kolvo: this.kolvo,
        itogo: this.itogo
      })
      this.naim = ''
      this.cena = this.kolvo = 0
    },
    remove_tovars () {
      this.canc_tovars.pop()
    }
  }
}
</script>

<style scoped>
  .new_zay {
    margin: 5%  ;
    text-align: left;
  }
  h2, h3 {
    color: #3B1657;
  }
  p {
    color: rgba(59, 57, 73, 0.55);
    font-weight: 700;
  }
  table {
    border-collapse: collapse;
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
    padding: 5%;
    text-align: center;
  }
  .t_body {
    background-color: rgba(227, 206, 206, 0.5);
    padding: 2% 0%;
    text-align: center;
    border: 2px solid rgba(46, 7, 158, 0.3);
    border-top: none;
    color: #3B1657;
    font-weight: 400;
  }
  .t_body:first-child {
    border-left: none;

  }
  .t_body:last-child {
    border-right: none;
  }
  .space {
    width: 20%;
  }
  .num_date{
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  table {
    width: 90%;
  }
  .data_block {
    display: flex;
    flex-direction: row;
    margin: 4% -10%;
  }

  .input_num {
    height: 50%;
    width: 10%;
    border: none;
    border-bottom: 1px solid rgba(11, 16, 64, 0.57);
    color: #3B1657;
    font-weight: 700;
  }
  .input_main {
    height: 50%;
    width: 70%;
    border: none;
    border-bottom: 1px solid rgba(11, 16, 64, 0.57);
    color: #3B1657;
    font-weight: 700;
  }
  textarea {
    width: 81%;
    padding: 2%;
    background-color: rgba(227, 206, 206, 0.5);
    border-radius: 14px;
    border: 0px;
    resize: none;
  }
  select {
    border: none;
    border-bottom: 1px solid rgba(11, 16, 64, 0.57);
    width: 20%;
    background-color: white;
    color: #3B1657;
    font-weight: 700;
  }
  .input_table {
    border: none;
    background-color: initial;
    color: #3B1657;
    font-size: 18px;
    text-align: center;
  }
  .buttons {
    display: flex;
    justify-content: space-evenly;
  }
  .button_cancel {
    background-color: #ED0C0C;
    color: white;
    padding: 1% 3%;
    border-radius: 5px;
    box-shadow: 2px 2px 14px rgba(60, 9, 166, 0.53);
    font-weight: 700;
  }
  .button_ok {
    background-color: #1F6805;
    color: white;
    padding: 1% 3%;
    border-radius: 5px;
    box-shadow: 2px 2px 14px rgba(60, 9, 166, 0.53);
    font-weight: 700;
  }
</style>