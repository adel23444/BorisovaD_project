<template>
  <div class="zay">
    <div style="display: flex; justify-content: space-between">
      <p class="zay_zagol">{{types(propert.type)}}</p>
      <p class="zay_zagol" style="margin-right: 6%">№{{propert.num}}</p>
    </div>

    <div style="display: flex; margin: 0%">
      <div v-if="propert.type === 0" class="zay_params">
        <div style="display: flex;">
          <img style="width: 1.5vw; margin-right: 1em " src="../assets/comment.svg" alt="comment">
          <p>{{propert.tov_name}}</p>
        </div>
        <p>Количество: {{propert.count}} шт.</p>
        <p>Стоимость: {{propert.cena}} рублей</p>
        <div style="width: 10%"></div>
      </div>
      <div v-else-if="propert.type === 1" class="zay_params params_transport">
        <div style="display: flex;">
          <img style="width: 1.5vw; margin-right: 1em " src="../assets/address.svg" alt="address">
          <p>Адрес: {{propert.addr}}</p>
        </div>
        <p>Пункт назначения: {{propert.punkt}}</p>
        <p>Дата: {{propert.data_dost}} в {{propert.vrem}}</p>
        <div style="width: 2%"></div>
      </div>
      <div v-else-if="propert.type === 2" class="neispravn">
        <div style="display: flex;">
          <img style="width: 1.5vw; margin-right: 1em " src="../assets/address.svg" alt="address">
          <p>{{propert.comment}}</p>
        </div>
        <div style="width: 15%"></div>
      </div>

      <div>
        <div v-if="propert.status_zay === 0" class="status_active">
          <p style="color: white; ">{{statuses(propert.status_zay)}}</p>
        </div>
        <div v-else-if="propert.status_zay === 1" class="status_closed">
          <p style="color: white; ">{{statuses(propert.status_zay)}}</p>
        </div>
      </div>
    </div>
    <div style="display: flex; justify-content: space-evenly; width: 15%; align-items: center">
      <img style="height: 4vh; width: 4vw" src="../assets/Calendar.svg" alt="calendar">
      <p style="font-size: 14px">{{propert.date}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "ZayAvka",
  props: {
    propert: {
      type: Object
    },
  },
  methods: {
    types(type) {
      if (type === 0) {
        return "Канцелярия"
      }
      if (type === 1) {
        return "Транспорт"
      }
      if (type === 2) {
        return "Неисправность"
      }
    },
    statuses(status) {
      if (status === 0) {
        return "Активная"
      }
      else {
        return "Завершена"
      }
    }
  }
}
</script>

<style scoped>
  .zay {
    background-color: rgba(227, 206, 206, 0.5);
    margin: 3%;
    border-radius: 32px;
    width: 85%;
    height: 15%;
    padding: 1vh 4vw;
  }
  p {
    color: rgba(46, 7, 158, 1);
  }
  .zay_zagol {
    font-size: 24px;
    font-weight: 700;
    margin-top: 2%;
    margin-bottom: 0.5%;
  }
  .zay_params {
    display: flex;
    justify-content: space-around;
    width: 80%;
    font-weight: 600;
    font-size: 18px;
    align-items: center;
  }
  .params_transport {
    font-size: 13px;
  }
  .neispravn {
    display: flex;
    width: 80%;
    font-weight: 600;
    font-size: 18px;
    align-items: center;
  }
  .status_active {
    background-color: rgba(31, 104, 5, 1);
    font-size: 20px;
    font-weight: 800;
    padding: 0px 24px;
    border-radius: 32px;
  }
  .status_closed {
    background-color: rgba(31, 104, 5, 0.6);
    font-size: 20px;
    font-weight: 800;
    padding: 0px 24px;
    border-radius: 32px;
  }
</style>