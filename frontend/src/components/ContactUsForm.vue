<script setup>
import DecoTitles from './DecoTitles.vue';
import WhyUsCard from './WhyUsCard.vue';
import Button from './Button.vue';
</script>
<template>
    <form action="">
        <h2>Book Now!</h2>
        <div class="form-items">
            <input type="text" placeholder="Name*" required />
            <input type="text" placeholder="Phone Number*" required />
            <input type="email" placeholder="Email*" required />
            <textarea name="message" id="message" placeholder="Enter your message here" required></textarea>
        </div>
        <Button text="Send Message" type="submit" />
    </form>

</template>

<style scoped>
form {
    padding: 20px;
    background-color: white;
    border-radius: 20px;
    border: 1px solid #eeeeee;

    h2 {
        margin-bottom: 20px;
        color: #462C7D;
        font-weight: bold;
    }
}

.form-items {
    display: flex;
    flex-direction: column;
    overflow-x: hidden;
    gap: 20px;

    input,
    textarea {
        width: 100%;
        padding: 10px;
        border-radius: 15px;
        outline: none;
        border: 1px solid #eeeeee;
        background-color: #F5E7F5;
    }

    textarea {
        max-width: 100%;
    }

}

button {
    margin-top: 20px;
    padding: 10px;
    border-radius: 5px;
    background-color: #462C7D;
    color: white;
}
</style>
