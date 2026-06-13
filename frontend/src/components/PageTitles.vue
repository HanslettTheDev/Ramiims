<script setup>
const props = defineProps(['title'])
</script>

<template>
    <h2>{{ title }}</h2>

</template>

<style scoped>
h2 {
    padding-top: 60px;
    color: #ff0085;
    padding-bottom: 20px;
    font-weight: bold;
}
</style>
