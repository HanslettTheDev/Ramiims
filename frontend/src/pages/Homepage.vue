<script setup>
import offersCard from "../Components/offersCard.vue";
</script>

<template>
  <nav>
    <div class="nav-bg-image"></div>
    <div class="nav-container">
      <div class="logo">
        <span>R@MIMS</span>
      </div>
      <ul>
        <li><a href="">Home</a></li>
        <li><a href="">About Us</a></li>
        <li><a href="">Gallery</a></li>
        <li><a href="">Blog</a></li>
        <div class="banner"><a href="#">Get in Touch</a></div>
      </ul>
    </div>
  </nav>

  <header>
    <h1>R@mims Metamorphosis Center</h1>
    <div class="banner"><a href="#">Learn More</a></div>
  </header>

  <main>
    <section id="offers">
      <h1>What We Offer</h1>
      <div class="offers-container">
        <offersCard
          message="Hello world this is a message And this text is going to be 
          to be added line by line
          "
          service="Main service"
        >
        </offersCard>
        <offersCard
          message="Hello world this is a message And this text is going to be 
          to be added line by line
          "
          service="Main service"
        >
        </offersCard>
        <offersCard
          message="Hello world this is a message And this text is going to be 
          to be added line by line
          "
          service="Main service"
        >
        </offersCard>
      </div>
    </section>

    <section id="customer-section">
      <div class="left-side">
        <h3>What makes us a customer favorite</h3>
        <div class="left-side-body">
          <div class="image-header">
            <img src="" alt="some image" />
          </div>
          <p>Yes there is some content here</p>
        </div>
        <div class="left-side-body">
          <div class="image-header">
            <img src="" alt="some image" />
          </div>
          <p>Yes there is some content here</p>
        </div>
        <div class="left-side-body">
          <div class="image-header">
            <img src="" alt="some image" />
          </div>
          <p>Yes there is some content here</p>
        </div>
      </div>

      <div class="right-side">
        <form action="">
          <input type="text" placeholder="Name" />
          <input type="text" placeholder="Phone Number" />
          <textarea name="message" id=""></textarea>
          <button class="">Contact Us</button>
        </form>
      </div>
    </section>
    <section id="gallery">
      <h1>Gallery</h1>
      <div class="image-container">
        <img src="" alt="" />
        <img src="" alt="" />
        <img src="" alt="" />
        <img src="" alt="" />
      </div>

      <button class="">More Pictures</button>
    </section>
  </main>
  <footer>
    <p>Build by Venom</p>
  </footer>
</template>

<style scoped>
/*
NAVBAR SECTION
*/

nav {
  width: 100%;
  height: 100vh;
  font-weight: normal;
}

.nav-bg-image {
  width: 100%;
  height: 100%;
  background-image: url("../assets/images/home.jpeg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: 100% 100%;
  filter: blur(10px);
  -webkit-filter: blur(10px);
}

.nav-container {
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
  margin-top: 60px;
}

.nav-container ul {
  list-style: none;
  display: flex;
  flex-direction: row;
  font-size: 20px;
}

.nav-container ul li {
  margin-left: 15px;
  margin-right: 15px;
  padding: 7px;
}

.nav-container ul li:hover {
  background: var(--primary-color);
  border-radius: 5px;
}

.nav-container a {
  text-decoration: none;
  color: var(--text-color);
  font-weight: bolder;
}

.logo {
  background: var(--primary-color);
  padding: 8px;
  border-radius: 5px;
  color: white;
  height: inherit;
  font-weight: bold;
  font-size: 30px;
  cursor: pointer;
}

.banner {
  align-self: center;
  margin-left: 20px;
  background: var(--secondary-color);
  font-weight: bold;
  border-radius: 10px;
  padding: 10px;
  cursor: pointer;
}

.banner a {
  text-decoration: none;
  color: white;
}

.banner:hover {
  background: var(--secondary-color);
}

header {
  width: 100%;
  position: absolute;
  top: 40%;
  left: 0;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

header h1 {
  color: whitesmoke;
}

/* MAIN SECTION
Offers section
*/

main {
  border: 1px solid red;
}

#offers {
  border: 1px solid green;
  color: black;
  background: var(--alternate-background-color);
  padding: 3% 7%;
  text-align: center;
  margin-top: 30px;
}

.offers-container {
  margin-top: 80px;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-evenly;
}
</style>
