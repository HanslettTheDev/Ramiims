<script setup>
import Button from './Button.vue';
import DecoTitles from './DecoTitles.vue';
import GalleryPictureBox from './GalleryPictureBox.vue';
</script>
<template>
    <section id="gallery">
        <DecoTitles title="Gallery" />
        <div class="image-wrapper">
            <GalleryPictureBox image="home.jpeg" />
            <GalleryPictureBox image="ramiims.jpeg" />
            <GalleryPictureBox image="logo-black-bg.png" />
            <GalleryPictureBox image="logo-white-bg.png" />
        </div>

        <Button text="More Pictures" />
    </section>
</template>

<style scoped>
#gallery {
    text-align: center;
    margin-top: 200px;
    padding-bottom: 60px;
}


.image-wrapper {
    margin-top: 20px;
    padding: 5px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 5px;
}
</style>
