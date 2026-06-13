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
    width: 100%;
    padding: 5px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 20px;

    .service-header {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;

        img {
            height: 50px;
            width: 50px;
            margin-bottom: 10px;
        }

        h3 {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            gap: 5px;

            span {
                width: 10%;
                height: 5px;
                background-color: #ff0085;
            }

        }

    }

    .service-body {
        width: 200px;
        text-align: left;
    }
}
</style>
