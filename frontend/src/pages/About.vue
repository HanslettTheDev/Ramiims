<script setup>
import HomeLayout from '@/layouts/HomeLayout.vue';
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';
import AboutUsImage from '@/components/AboutUsImage.vue';
import PageTitles from '@/components/PageTitles.vue';
import OurTeamSection from '@/sections/OurTeamSection.vue';
</script>

<template>

    <HomeLayout>

        <header>
            <PageTitles title="About Us" />
            <AboutUsImage />
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur aspernatur laborum illo tempore magni?
                Magnam illo debitis cumque assumenda eligendi beatae aperiam dolor illum id saepe! Maiores nam adipisci
                iusto?</p>
        </header>

        <OurTeamSection />
    </HomeLayout>


</template>

<style scoped>
header {
    text-align: center;

    p {
        color: black;
        text-align: left;
        padding: 5px;
    }
}
</style>
