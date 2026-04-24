<script setup>
let text = 'Contact Us';

</script>
<template>
    <a href="#" class="banner">{{ text }}</a>
</template>
<style scoped>
.banner {
    background: #462C7D;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px;
    cursor: pointer;
}

.banner a {
    text-decoration: none;
    color: white;
}

.banner:hover {
    background: #610c9f;
}
</style>
