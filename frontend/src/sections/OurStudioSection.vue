<script setup>
import ServiceBox from '@/components/ServiceBox.vue';
import DecoratedTitles from '@/components/DecoratedTitles.vue';
</script>

<template>
    <section id="customer-favorite">
        <DecoratedTitles title='Our Studio' />
        <div class="favorite-container">
            <ServiceBox />
            <ServiceBox />
            <ServiceBox />
            <ServiceBox />
        </div>
    </section>

</template>

<style scoped>
#customer-favorite {
    margin-top: 50px;
    color: black;
    text-align: center;
    background-color: #FAF3ED;

}

.favorite-container {
    margin-top: 50px;
    display: flex;
    flex-direction: column;
    gap: 30px;
    padding-bottom: 70px;
}
</style>
