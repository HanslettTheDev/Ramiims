<script setup>
import NavBar from '@/components/NavBar.vue';
import OffersSection from '@/components/OffersSection.vue';
import Footer from '@/components/Footer.vue';
import GallerySection from '@/components/GallerySection.vue';
import Header from '@/components/Header.vue';

</script>

<template>
    <!-- Nav bar section -->
    <NavBar />

    <!-- Header section -->
    <Header />

    <!-- Offers section -->
    <div class="sections">
        <OffersSection />
        <GallerySection />
    </div>

    <Footer />
</template>

<style scoped></style>
