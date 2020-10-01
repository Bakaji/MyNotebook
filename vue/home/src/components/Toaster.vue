<template>
    <div id="toaster" class="toaster-hidden">
        Toaster
    </div>
</template>

<script>
    import Vue from 'vue';

    Vue.prototype.$toast = function (text, time) {
        if (text) {
            const toaster = document.getElementById("toaster");
            if (toaster) {
                toaster.classList.add("showed");
                document.innerText = text;
                const t = time ? time*1000 : 2000;
                setTimeout(function () {
                    console.log("in timeout f");
                    toaster.classList.remove("showed")
                }, t)
            }
        }
    };
    export default {
        name: "Toaster"
    }
</script>

<style lang="scss">
    .toaster-hidden {
        position: fixed;
        top: 50px;
        left: 50vw;
        transform: translate(-50%, 0);
        text-align: center;
        padding: 15px;
        width: clamp(300px, 70vw, 700px);
        background-color: rgba(255, 0, 0, 0.51);
        color: white;
        opacity: 0;
        pointer-events: none;
        transition: opacity 1s;
    }

    .showed {
        opacity: 1;
    }
</style>