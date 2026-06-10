<script setup>
import ContactUsForm from '@/components/ContactUsForm.vue';
import DecoratedTitles from '@/components/DecoratedTitles.vue';
import WhyUsCard from '@/components/WhyUsCard.vue';
</script>
<template>
    <section id="customer-section">
        <DecoratedTitles title='What makes us a customer favorite' />
        <div class="left-side">
            <WhyUsCard />
            <WhyUsCard />
            <WhyUsCard />
            <WhyUsCard />
        </div>

        <div class="right-side">
            <ContactUsForm />
        </div>
    </section>

</template>

<style scoped>
#customer-section {
    background-color: #F4E7F4;
    border-radius: 5px;
    text-align: center;
}

h3 {
    color: black;
}

.left-side {
    padding: 10%;
    display: flex;
    flex-direction: column;
    gap: 50px;
}

.right-side {
    margin-top: 50px;
    padding: 10px;
    height: 200px;
    padding-bottom: 50px;
}
</style>
