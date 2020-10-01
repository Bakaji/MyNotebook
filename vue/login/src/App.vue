<template>
    <div id="app">
        <Login/>
    </div>
</template>

<style lang="scss">
    @import "styles/default";

    #app {
        height: 100vh;
        width: 100vw;
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>
<script>
    import Login from "./views/Login";

    export default {
        components: {Login}
    }
</script>