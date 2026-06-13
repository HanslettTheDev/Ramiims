<template>

    <div class="team-profile-container">
        <div class="image-container">
            <img src="../assets/images/ramiims.jpeg" alt="Profile picture of x user">
        </div>
        <div class="profile-name">
            <p>
                Venom Raiders
            </p>
        </div>
    </div>
</template>

<style scoped>
.team-profile-container {
    width: 130px;
    height: 130px;
    position: relative;

    .image-container {
        width: 100%;
        height: 100%;

        img {
            width: inherit;
            height: inherit;
            border-radius: 20px;
        }
    }


    .profile-name {
        width: 100%;
        height: 50px;
        position: absolute;
        bottom: -20px;
        z-index: 999;
        background-color: transparent;
        text-align: center;
        display: flex;
        justify-content: center;

        p {
            color: black;
            align-self: center;
            display: flex;
            align-items: center;
            width: 90%;
            min-height: 35px;
            height: fit-content;
            border: 2px solid #462C7D;
            border-radius: 10px;
            background-color: white;
            padding: 2px;
        }
    }


}
</style>
