<script setup>
import SpecialBtn from './SpecialBtn.vue';

</script>

<template>
    <nav>
        <div class="nav-container">
            <div class="logo">
                <img src="../assets/images/Asset 11.png" alt="Rammims black logo version">
            </div>
            <span class="bar-menu">
                <img src="../assets/images/bar.png" alt="styled bar menu">
            </span>
            <div class="nav-items">
                <a class="closebtn" onclick="closeNav()">&times;</a>
                <ul>
                    <li><a href="">Home</a></li>
                    <li><a href="">About Us</a></li>
                    <li><a href="">Gallery</a></li>
                    <li><a href="">Blog</a></li>
                    <li>
                        <SpecialBtn />
                    </li>

                </ul>
            </div>
        </div>
    </nav>
</template>

<style scoped>
/*
NAVBAR SECTION
*/

nav {
    padding: 15px;
    position: relative;
}


.logo {
    width: 50px;
    height: 50px;
    /* background: #e95793; */
    /* padding: 8px; */
    /* border-radius: 5px; */
    /* height: inherit; */
    /* font-weight: bold; */
    /* font-size: 30px; */
    /* cursor: pointer; */

    img {
        width: inherit;
        height: inherit;
    }
}


.nav-container {
    /* position: absolute; */
    /* top: 0; */
    /* left: 0; */
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: black;

    ul {
        display: none;
        list-style: none;
        display: flex;
        flex-direction: row;
        font-size: 12px;
    }
}


.bar-menu {
    width: 40px;
    height: 40px;

    img {
        width: inherit;
        height: inherit;
    }
}

.nav-items {
    height: 100%;
    width: 0;
    position: fixed;
    top: 0;
    right: 0;
    z-index: 999;
    overflow-x: hidden;
    padding-top: 65px;
    display: block;
    transition: ease-in 0.5s;

    .closebtn {
        position: absolute;
        top: 0;
        right: 25px;
        font-size: 35px;
        margin-left: 50px;
    }

    ul {
        display: flex;
        flex-direction: column;
        justify-content: flex-end;

        li {
            align-self: center;
            margin-top: 30px;
            /* padding: 8px 8px 8px 32px; */
            padding: 8px 20px;
            border: 1px solid green;
        }

        a:hover {
            background: #e95793;
            border-radius: 5px;
            color: white;
        }
    }


    a {
        border: 1px solid red;
        font-weight: bolder;
        text-decoration: none;
    }

}
</style>
