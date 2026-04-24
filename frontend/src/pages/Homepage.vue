<script setup>
import NavBar from '@/components/NavBar.vue';
import OffersSection from '@/components/OffersSection.vue';
import Footer from '@/components/Footer.vue';
import GallerySection from '@/components/GallerySection.vue';
import OurStudioSection from '@/components/OurStudioSection.vue';
import Header from '@/components/Header.vue';
import CustomerSection from '@/components/CustomerSection.vue';

</script>

<template>

    <!-- Nav bar section -->
    <NavBar />

    <main>

        <!-- Header section -->
        <Header />

        <!-- Offers section -->
        <div class="sections">
            <OffersSection />
            <OurStudioSection />
            <CustomerSection />
            <GallerySection />
        </div>



    </main>
    <Footer />
</template>

<style scoped></style>
