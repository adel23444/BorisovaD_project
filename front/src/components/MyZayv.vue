<template>
  <div class="my_zayv">
    <div style="display: flex; justify-content: space-between">
      <h1 style="width: 90%;">Мои заявки</h1>
      <div class="zayv_buttons">
        <div class="button_zay">
          <p style="margin-bottom: 2%">Все</p>
          <hr>
        </div>
        <div class="button_zay">
          <p style="margin-bottom: 2%">Текущие</p> <hr>
        </div>
        <div class="button_zay">
          <p style="margin-bottom: 2%">Завершенные</p> <hr>
        </div>
      </div>
    </div>

    <div class="list_zay">
      <ZayAvka v-for="(propert, $index) in zayvaks" :key="$index"
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
          status_zay: 0
        },
        {
          type: 0,
          tov_name: "Бумага А4",
          count: 2,
          cena: 200,
          num: 154,
          status_zay: 1,
          date: "17.12.2021",
        },
        {
          type: 2,
          comment: "Не работает кондиционер",
          date: "11.11.2021",
          status_zay: 1,
          num: 130
        }
      ]
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
    justify-content: space-between;
    width: 70%;
  }
  .button_zay {
    color: rgba(59, 22, 87, 1);
    font-weight: 700;
    font-size: 20px;
  }
</style>