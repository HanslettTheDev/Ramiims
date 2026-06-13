<script setup>
import Button from './Button.vue';
import SpecialBtn from './SpecialBtn.vue';

function toggleNavBarOn() {
    document.getElementById("nav-items").style.width = "250px";
}


function toggleNavBarOff() {
    document.getElementById("nav-items").style.width = "0px";
}
</script>

<template>
    <nav>
        <div id="nav" class="nav-container">
            <div class="logo">
                <img src="../assets/images/logo-full-black.png" alt="Rammims black logo version">
            </div>
            <span @click="toggleNavBarOn()" class="bar-menu">
                <img src="../assets/images/bar.png" alt="styled bar menu">
            </span>
            <div id="nav-items" class="nav-items">
                <a class="closebtn" @click="toggleNavBarOff()">&times;</a>
                <ul>
                    <li class="active"><a href="">Home</a></li>
                    <li><a href="">About Us</a></li>
                    <li><a href="">Gallery</a></li>
                    <li><a href="">Blog</a></li>

                </ul>

                <div class="nav-btn">
                    <Button text="Contact Us" />
                </div>

                <div class="nav-footer-text">
                    Developed by Venom
                </div>

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
    width: 100%;
    position: fixed;
    left: 0;
    z-index: 999;
    background-color: white;
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
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: black;
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
    background-color: white;
    width: 0;
    position: fixed;
    top: 0;
    right: 0;
    overflow-x: hidden;
    padding-top: 65px;
    transition: ease-in 0.5s;

    .active {
        background-color: #462C7D;

        a {
            color: white;
        }
    }

    .closebtn {
        border-radius: 100%;
        padding: 5px;
        width: 50px;
        text-align: center;
        position: absolute;
        top: 0;
        right: 25px;
        font-size: 35px;
        margin-left: 50px;
        cursor: pointer;
    }

    .nav-btn {
        padding-top: 60px;
        text-align: center;
    }

    .nav-footer-text {
        position: absolute;
        bottom: 0;
        right: 0;
        transform: translate(-30%);
        margin-bottom: 50px;
        text-decoration: underline;
    }


    ul {
        padding: 0;
        text-align: center;
        list-style: none;
        display: flex;
        flex-direction: column;
        align-items: center;


        li {
            width: 70%;
            border-radius: 20px;
            color: white;
            margin-top: 30px;
            padding: 10px;
            border: 1px solid #831C91;

            a {
                font-weight: bold;
                height: 100%;
            }

            &:hover {
                background-color: #ff0085;

                a {
                    color: white;
                }
            }

        }


    }

}
</style>
