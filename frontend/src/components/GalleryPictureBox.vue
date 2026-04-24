<script setup>
const props = defineProps(['image'])
</script>
<template>
    <div>
        <img :src="'public/' + image" alt="Gallery image" />
    </div>

</template>

<style scoped>
div {
    border: 2px solid #eeeeee;
    padding: 5px;

    &:hover {
        background-color: #FF70BF;
        cursor: pointer;
    }

    img {
        width: 100%;
        height: 100%;
    }

}
</style>
