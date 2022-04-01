<template>
  <div>
    <NavBar />
    <MyDoc />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import MyDoc from "@/components/MyDoc";
export default {
  name: "Doc_Wind",
  components: {
    MyDoc,
    NavBar
  }
}
</script>

<style scoped>

</style>