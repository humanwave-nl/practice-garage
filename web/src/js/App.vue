<template>
    <div id="app">
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <a class="navbar-brand" href="#">Home</a>
        </nav>
        <router-view/>
    </div>
</template>

<script>
    export default {
      name: 'app'
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        display: grid;
        grid-template-columns: 1fr;
        grid-template-rows: 60px 1fr;
        grid-column-gap: 0px;
        grid-row-gap: 0px;
    }
</style>
