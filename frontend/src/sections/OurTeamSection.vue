<script setup>
import ServiceBox from '@/components/ServiceBox.vue';
import DecoratedTitles from '@/components/DecoratedTitles.vue';
import TeamProfile from '@/components/TeamProfile.vue';
</script>

<template>
    <section id="our-team">
        <DecoratedTitles title='Our Team' />
        <div class="team-container">
            <TeamProfile />
            <TeamProfile />
            <TeamProfile />
            <TeamProfile />
        </div>
    </section>

</template>

<style scoped>
#our-team {
    margin-top: 50px;
    color: black;
    text-align: center;
    background-color: #FAF3ED;

}

.team-container {
    margin-top: 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
    flex-wrap: wrap;
    gap: 30px;
    padding-bottom: 70px;
}
</style>
