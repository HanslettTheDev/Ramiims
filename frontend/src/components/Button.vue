<script setup>
const props = defineProps(['type', 'text', 'class'])
</script>
<template>
    <button :type="type" :class="class">{{ text }}</button>
</template>

<style scoped>
button {
    margin-top: 20px;
    padding: 10px;
    border-radius: 5px;
    background-color: #462C7D;
    color: white;
    cursor: pointer;
    outline: none;

    &:hover {
        background-color: #831C91;
    }
}
</style>
