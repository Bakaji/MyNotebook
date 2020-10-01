<template>
    <div class="modal-container flex-container" v-on:click="hideAddCollectionModal">
        <div class="modal-card" v-on:click="do_nothing">
            <form class="modal-content" v-on:submit.prevent="createCollection">
                <h3>Add collection</h3>
                <label for="coll_name">Name</label>
                <input id="coll_name" type="text" v-model="targetedCollection.collection_name"/>
                <span class="errors">{{this.nameError}}</span>
                <label for="coll_desc">Description</label>
                <input id="coll_desc" type="text" v-model="targetedCollection.description"/>
                <span class="errors">{{descriptionError}}</span>
                <label for="coll_clr">Color</label>
                <div class="select-container">
                    <select id="coll_clr" v-model="targetedCollection.collection_color"
                            :value="targetedCollection.collection_color">
                        <option>Blue</option>
                        <option>Green</option>
                        <option>Red</option>
                        <option>Violet</option>
                        <option>Orange</option>
                        <option>Yellow</option>
                    </select>
                    <div class="arrow"></div>
                </div>
                <div class="button-container">
                    <input type="submit" value="Create" :disabled='invalidInput'>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
    import {mapActions, mapGetters} from "vuex";

    export default {
        name: "AddCollectionModel",
        data: () => ({
            targetedCollection: {
                collection_name: '',
                description: '',
                collection_color: 'Blue',
            }
        }),
        methods: {
            ...mapActions(['hideAddCollectionModal']),
            do_nothing: (e) => {
                e.stopPropagation();
            },
            createCollection: function () {
                const data = this.targetedCollection;
                data['collection_color'] = data['collection_color'].toLowerCase();
                this.$store.dispatch("createNewCollection", data)
            },
        },
        computed: {
            ...mapGetters(['getCollectionNames']),
            nameError: function () {
                const collection_name = this.targetedCollection.collection_name;
                if (collection_name.match('^\\s*$'))
                    return "empty input";
                if (collection_name.match('[^a-zA-Z0-9\\s]'))
                    return "name should be alphanumeric and spaces";
                if (this.getCollectionNames.indexOf(collection_name) >= 0)
                    return "name already used";
                return "";
            },
            descriptionError: function () {
                const description = this.targetedCollection.description;
                if (description.match('^\\s*$'))
                    return "empty input";
                if (description.match('[^a-zA-Z0-9\\s]'))
                    return "name should be alphanumeric and spaces";
                return "";
            },
            invalidInput: function () {
                return this.nameError !== '' || this.descriptionError !== '' || this.color === '';
            }
        }
    }
</script>

<style lang="scss">
    @import "../../styles/palette";


    .modal-card {
        max-width: 700px;

        .modal-content {
            height: 95%;
            width: 95%;
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;

            h3 {
                flex-basis: 90%;
            }

            label {
                flex: 1;
                flex-basis: 33%;
            }

            .errors {
                flex: 100%;
                height: 15px;
                font-size: 12px;
                font-weight: bold;
                color: red;
            }

            input, .select-container, textarea {
                flex: 2;
                flex-basis: 66%;
            }

            .select-container {
                position: relative;

                select {
                    appearance: none;
                    position: absolute;
                    right: 0;
                    top: 0;
                    width: 100%;
                    cursor: pointer;
                }

                .arrow {
                    position: absolute;
                    display: block;
                    right: 0;
                    top: 0;
                    height: 30px;
                    width: 30px;
                    pointer-events: none;
                    background-color: $secondary_color;

                    &::before, &::after {
                        content: 'ˆ';
                        height: 15px;
                        color: white;
                        width: 15px;
                        font-size: 30px;
                        position: absolute;
                        right: 5px;
                        top: -1px;
                    }

                    &::after {
                        content: 'ˇ';
                        top: 9px;
                    }
                }
            }

            .button-container {
                flex-basis: 100%;
                display: flex;
                justify-content: flex-end;

                input {
                    flex-basis: 120px;
                    height: 40px;
                    max-width: 120px;

                    &:disabled {
                        background-color: red;
                    }
                }
            }
        }
    }
</style>