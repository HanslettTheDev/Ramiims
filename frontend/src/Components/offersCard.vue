<script setup>
defineProps({
  service: {
    type: String,
  },
  imageUrl: {
    type: String,
    default: "../assets/images/home.jpeg",
  },
  message: {
    type: String,
  },
});
</script>

<template>
  <div class="service-box">
    <div class="service-image">
      <img src="../assets/images/home.jpeg" alt="Sample Service Image" />
    </div>
    <div class="service-header">
      <h3>{{ service }}</h3>
      <p>
        {{ message }}
      </p>
    </div>
  </div>
</template>

<style scoped>
/*Style for OffersCard component*/

.service-box {
  width: 300px;
  height: 400px;
  margin-left: 50px;
  border: 1px solid var(--border-color);
  overflow: hidden;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
  margin-bottom: 30px;
}

.service-image {
  height: 100%;
}

.service-image img {
  width: 100%;
  height: 100%;
}

.service-header {
  text-align: left;
  padding: 10px;
}
</style>
