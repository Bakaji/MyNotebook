<template>
    <div class="flex-container flex-from-start">
        <router-view/>
    </div>
</template>

<script>
    import {mapActions, mapGetters} from "vuex";

    export default {
        name: "CollectionView",
        methods: {
            ...mapActions(['loadCollectionsFromServer',]),
        },
        mounted: function () {
            this.loadCollectionsFromServer()
        },
        computed: {
            ...mapGetters(['collections']),
        }

    }
</script>

<style lang="scss">

</style>