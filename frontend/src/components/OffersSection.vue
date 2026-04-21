<script setup>
import ServiceBox from './ServiceBox.vue';
</script>

<template>
    <section id="offers">
        <h2>What We Offer</h2>
        <img class='offer-image' src="../assets/images/flower.png" alt="flower drawn image">
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
    padding: 20px;
    color: black;
    text-align: center;

    .offer-image {
        height: 20px;
    }
}

h2 {
    color: #ff0085;
    padding-bottom: 20px;
    font-weight: bold;
}

.services-container {
    margin-top: 50px;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 20px;
}


.service-box {
    width: 150px;
    padding: 5px;

    .service-header {
        text-align: center;

        h3 {
            display: flex;
            align-items: center;
            gap: 5px;

            span {
                width: 20%;
                height: 5px;
                border: 1px solid red;
                background-color: #ff0085;
            }

        }

    }

    .service-body {
        text-align: left;
    }
}
</style>
