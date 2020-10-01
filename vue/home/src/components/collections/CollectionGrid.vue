<template>
    <div class="container">
        <AddCollectionModal v-if="AddCollectionModalVisible"/>
        <EditCollectionModal v-if="EditCollectionModalVisible"
                             :key="getSelectedCollection.collection_id"/>

        <div class="header">
            <div><h1>Collections</h1></div>
            <div class="add-button" v-on:click="showAddCollectionModal">Add +</div>
        </div>
        <div class="collection-grid">
            <CollectionCard v-for="coll in getCollections" :key="coll.collection_id"
                            :collection=coll></CollectionCard>
        </div>
    </div>
</template>

<script>
    import {mapActions, mapGetters} from "vuex";
    import CollectionCard from "./CollectionCard";
    import AddCollectionModal from "../modals/AddCollectionModal";
    import EditCollectionModal from "../modals/EditCollectionModal";

    export default {
        name: "Collection_grid",
        components: {
            CollectionCard,
            AddCollectionModal,
            EditCollectionModal
        },
        data() {
            return {
                actionsArray: ["delete selected collection"],
            }
        },
        computed: {
            ...mapGetters(
                ['getCollections',
                    'AddCollectionModalVisible',
                    'EditCollectionModalVisible',
                    'confirmationModalVisible',
                    'getSelectedCollection',
                    'AddNoteModalVisible'
                ])
        },
        methods: {
            ...mapActions(['showAddCollectionModal'])
        }
    }
</script>

<style lang="scss">
    @import '../../styles/palette';

    .container {
        display: flex;
        height: 100%;
        width: 100%;
        flex-direction: column;
    }

    .header {
        flex: 0;
        display: flex;
        flex-basis: 70px;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;

        div {
            flex: 1;

            h1 {
                margin-left: 20px;
                color: $primary_color;
            }
        }

        .add-button {
            flex: 0;
            flex-basis: 45px;
            font-weight: bold;
            color: $secondary_color;
            cursor: pointer;
            transition: color .15s;

            &:hover {
                color: $primary_color;
            }
        }

    }

    .collection-grid {
        flex: 1;
        padding: 0 8px;
        display: flex;
        flex-wrap: wrap;
        position: relative;
    }
</style>