<script></script>

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
      <div class="service-box">
        <div class="service-header">
          <!-- Image title here -->
          <h5>Service 1</h5>
        </div>
      </div>
      <div class="service-box">
        <div class="service-header">
          <!-- Image title here -->
          <h5>Service 2</h5>
        </div>
        <ul>
            <li>Home</li>
            <li>About Us</li>
            <li>Gallery</li>
            <li>Blog</li>
            <div class="banner">Get in Touch</div>
        </ul>
    </nav>

    <header>
        <h1>Mummy Rach Metamorphosis Center</h1>
        <span class="action-statement">You get what you deserve</span>
        <button>Contact Us</button>
    </header>
    <main>
        <section id="offers">
            <div class="service-box">
                <div class="service-header">
                    <!-- Image title here -->
                    <h5>Service 1</h5>
                </div>
            </div>
            <div class="service-box">
                <div class="service-header">
                    <!-- Image title here -->
                    <h5>Service 2</h5>
                </div>
            </div>

            <div class="service-box">
                <div class="service-header">
                    <!-- Image title here -->
                    <h5>Service 3</h5>
                </div>
            </div>

            <div class="service-box">
                <div class="service-header">
                    <!-- Image title here -->
                    <h5>Service 4</h5>
                </div>
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
  background: #e95793;
  border-radius: 5px;
}

.nav-container a {
  text-decoration: none;
  color: white;
  font-weight: bolder;
}

.logo {
  background: #e95793;
  padding: 8px;
  border-radius: 5px;
  height: inherit;
  font-weight: bold;
  font-size: 30px;
  cursor: pointer;
}

.banner {
  align-self: center;
  margin-left: 20px;
  background: #610c9f;
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
  background: #610c9f;
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
  font-size: 60px;
  color: whitesmoke;
}
</style>
