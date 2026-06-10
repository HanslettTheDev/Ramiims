<script setup>
import ServiceBox from '@/components/ServiceBox.vue';
import DecoratedTitles from '@/components/DecoratedTitles.vue';
</script>

<template>
    <section id="offers">
        <DecoratedTitles title="What We Offer" />
        <div class="services-container">
            <ServiceBox />
            <ServiceBox />
            <ServiceBox />
            <ServiceBox />
        </div>
    </section>

</template>

<style scoped>
#offers {
    margin-top: 50px;
    color: black;
    text-align: center;
}


.services-container {
    margin-top: 50px;
    display: flex;
    flex-direction: column;
    gap: 50px;
}
</style>
