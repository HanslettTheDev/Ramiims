<script setup>
import SpecialBtn from './SpecialBtn.vue';
</script>

<template>
    <header>
        <span class="action-statement">You get what you deserve</span>
        <div class="banner">
            <img src="../assets/images/home.jpeg" alt="homepage image">
            <div class="banner-text">

                <h2>R@mims Metamorphosis Center</h2>
                <SpecialBtn />
            </div>
        </div>
    </header>
</template>

<style scoped>
header {
    width: 100%;
    padding-top: 100px;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.action-statement {
    display: none;
}

.banner {
    position: relative;
    padding: 15px;

    img {
        width: 100%;
        height: inherit;
        border-radius: 20px;
    }

    .banner-text {
        padding-top: 20px;

        h2 {
            color: #ff0086;
            font-weight: bolder;
            padding-bottom: 30px;

        }

    }
}

header h1 {
    font-size: 60px;
    color: whitesmoke;
}

/* background-position: center; */
/* background-repeat: no-repeat; */
/* background-size: 100% 100%; */
/* filter: blur(10px); */
/* -webkit-filter: blur(10px); */
</style>
