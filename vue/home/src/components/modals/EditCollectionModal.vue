<template>
    <div class="modal-container flex-container" v-on:click="hideEditCollectionModal">
        <div class="modal-card" v-on:click="do_nothing">
            <form class="modal-content" v-on:submit.prevent="updateCollection">
                <h3>Edit collection : {{targetedCollection.collection_name}}</h3>
                <label for="coll_name">Name</label>
                <input id="coll_name" type="text" v-model="targetedCollection.collection_name"/>
                <span class="errors">{{newNameError}}</span>
                <label for="coll_desc">Description</label>
                <input id="coll_desc" type="text"
                       v-model="targetedCollection.collection_description"/>
                <span class="errors">{{descriptionError}}</span>
                <label for="coll_clr">Color</label>
                <div class="select-container">
                    <select id="coll_clr" v-model="targetedCollection.collection_color"
                            :value="targetedCollection.collection_color">
                        <option>blue</option>
                        <option>green</option>
                        <option>red</option>
                        <option>violet</option>
                        <option>orange</option>
                        <option>yellow</option>
                    </select>
                    <div class="arrow"></div>
                </div>
                <div class="button-container">
                    <input type="submit" value="Update" :disabled='invalidInput'>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
    import {mapActions, mapGetters} from "vuex";

    export default {
        name: "EditCollectionModel",
        data: function () {
            return {
                targetedCollection: {
                    collection_name: '',
                    collection_description: '',
                    collection_color: 'Blue',
                }
            }
        },
        mounted: function () {
            console.log("collection edit component mounted");
            // assign values of targeted collection
            this.targetedCollection.collection_name = this.getSelectedCollection.collection_name;
            this.targetedCollection.collection_description =
                this.getSelectedCollection.collection_description;
            this.targetedCollection.collection_color = this.getSelectedCollection.collection_color;
        },
        methods: {
            ...mapActions(['hideEditCollectionModal']),
            do_nothing: (e) => {
                e.stopPropagation();
            },
            /**
             * updateCollection update collection on submit click
             */
            updateCollection: function () {
                const data = this.targetedCollection;
                data['collection_color'] = data['collection_color'].toLowerCase();
                this.$store.dispatch("editSelectedCollection", data)
            },
        },
        computed: {
            ...mapGetters(['getCollectionNames', 'getSelectedCollection', 'getCollections']),
            newNameError: function () {
                const collection_name = this.targetedCollection.collection_name;
                if (collection_name) {
                    if (collection_name.match('^\\s*$'))
                        return "empty input";
                    if (collection_name.match('[^a-zA-Z0-9\\s]'))
                        return "name should be alphanumeric and spaces";
                    const index = this.getCollectionNames.indexOf(collection_name);
                    if (index >= 0) {
                        const matched_name_id = this.getCollections[index].collection_id;
                        if (matched_name_id !== this.getSelectedCollection.collection_id)
                            return "name already used";
                    }
                }
                return "";
            },
            descriptionError: function () {
                const description = this.targetedCollection.collection_description;
                if (description) {
                    if (description.match('^\\s*$'))
                        return "empty input";
                    if (description.match('[^a-zA-Z0-9\\s]'))
                        return "name should be alphanumeric and spaces";
                    return "";
                } else
                    return "something wrong"
            },
            invalidInput: function () {
                return this.newNameError !== '' || this.descriptionError !== '' ||
                    this.targetedCollection.collection_color === '';
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