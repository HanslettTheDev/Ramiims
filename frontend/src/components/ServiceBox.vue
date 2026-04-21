<script>

</script>

<template>

    <div class="service-box">
        <div class="service-header">
            <!-- Image title here -->
            <img src="../assets/images/brush.png" alt="brush image">
            <h3><span></span> Service 1</h3>
        </div>
        <div class="service-body">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates maiores, maxime aliquid culpa
            similique accusamus, </div>
    </div>

</template>

<style scoped>
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
