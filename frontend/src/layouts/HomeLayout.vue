<script setup>
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';

</script>

<template>

    <!-- Nav bar section -->
    <NavBar />

    <main>
        <slot />
    </main>
    <Footer />
</template>

<style scoped>
main {
    padding-top: 90px;
}
</style>
