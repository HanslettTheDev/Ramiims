<script setup>
import ContactUsForm from './ContactUsForm.vue';
import DecoTitles from './DecoTitles.vue';
import WhyUsCard from './WhyUsCard.vue';
</script>
<template>
    <section id="customer-section">
        <DecoTitles title='What makes us a customer favorite' />
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
