<script setup>
import HomeLayout from '@/layouts/HomeLayout.vue';
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
import OffersSection from '@/sections/OffersSection.vue';
import GallerySection from '@/sections/GallerySection.vue';
import Header from '@/components/Header.vue';
import CustomerSection from '@/sections/CustomerSection.vue';
import OurStudioSection from '@/sections/OurStudioSection.vue';

</script>

<template>

    <HomeLayout>
        <!-- Header section -->
        <Header />

        <!-- Offers section -->
        <div class="sections">
            <OffersSection />
            <OurStudioSection />
            <CustomerSection />
            <GallerySection />
        </div>

    </HomeLayout>


</template>

<style scoped></style>
