<script setup>
const props = defineProps(['title'])
</script>

<template>
    <h2>{{ title }}</h2>
    <img class='offer-image' src="../assets/images/flower.png" alt="flower drawn image">

</template>

<style scoped>
.offer-image {
    height: 20px;
}

h2 {
    padding-top: 60px;
    color: #ff0085;
    padding-bottom: 20px;
    font-weight: bold;
}
</style>
