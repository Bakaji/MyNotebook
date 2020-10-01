<!--suppress ALL -->
<template>
    <div class="card"
         :class=assignColor
         v-on:click="go_to_details">
        <div class="card-container">
            <div class="card-header" v-on:click="go_to_details">
                {{collection.collection_name }}
                <router-link :id=id :to=link></router-link>
            </div>
            <div class="card-options">
                <div class="menu-container" v-on:click="do_nothing"
                     v-on:mouseleave="menu_visible=false">
                    <font-awesome-icon :icon="['fas','ellipsis-v']" class="outlined"
                                       v-on:click.prevent="selectThis"/>
                    <ul class="menu" v-if="this.menu_visible">
                        <li v-on:click="showEditCollectionModal">
                            <span>Edit</span>
                        </li>
                        <li style="color: red" v-on:click="confirmDelete">
                            <span>Delete</span>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="card-footer">
                <span>notes: {{collection.notes_count}}</span>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapActions} from "vuex";

    export default {
        name: "CollectionCard",
        props: {
            collection: {
                required: true,
                type: Object,
                default: null
            }
        },
        data: function () {
            return {
                menu_visible: false
            }
        },
        methods: {
            ...mapActions(['showEditCollectionModal', 'selectCollection', 'deleteSelectedCollection']),
            go_to_details: function () {
                this.selectCollection(this.collection);//todo wtf
                const link = document.getElementById(this.id);
                if (link)
                    link.click();
            },
            confirmDelete: function () {
                this.$showDialog("are you sure you want to delete ", this.deleteSelectedCollection);
            },
            do_nothing: (e) => e.stopPropagation(),
            selectThis: function () {
                this.selectCollection(this.collection)
                this.menu_visible = true
            }
        },
        computed: {
            assignColor: function () {
                if
                (['violet', 'blue', 'green', 'red', 'orange', 'yellow'].indexOf(this.collection.collection_color) > -1)
                    return `card-background-${this.collection.collection_color}`;
                return "card-background-blue";
            },
            link: function () {
                return `collection/${this.collection.collection_id}`
            },
            id: function () {
                return `collection_id_${this.collection.collection_id}`
            }
        }
    }
</script>

<style lang="scss">
    @import "../../styles/palette";

    $card-height: 130px;
    .danger {
        color: red;
    }

    .card {
        cursor: pointer;
        margin: 8px;
        border-radius: 10px;
        padding: 10px;
        display: inline-block;

        max-height: $card-height;
        min-width: $card-height;

        flex-basis: $card-height;
        flex-grow: 1;

        &:hover {
            box-shadow: 3px 3px 8px 0 #ddd;
        }

        .card-container {
            height: 100%;
            width: 100%;

            display: grid;
            grid-template-columns: 3fr 20px;
            grid-template-rows: 20px 3fr 20px;

            .card-header {
                grid-column: 1/2;
                grid-row: 1/3;
                color: white;
                overflow-wrap: anywhere;
            }

            $time: 0.3s;

            .card-options {
                grid-column: 2/3;
                grid-row: 1/2;

                border: 0.5px solid transparent;
                border-radius: 5px;
                transition: border-top-color $time,
                border-left-color $time,
                border-right-color $time,
                border-bottom-color $time;

                .menu-container {
                    position: relative;
                    width: 100%;
                    height: 100%;
                    display: flex;
                    justify-content: center;
                    align-items: center;

                    .menu {
                        border: 1px solid $light_background_color;
                        background-color: white;
                        position: absolute;
                        right: 10px;
                        top: 10px;
                        z-index: 2;

                        li {
                            height: 35px;
                            width: 85px;
                            position: relative;
                            color: $primary_color;
                            font-weight: bold;
                            font-size: 14px;
                            border-bottom: 0.5px solid $light_background_color;

                            span {
                                position: absolute;
                                top: 50%;
                                left: 50%;
                                transform: translate(-50%, -50%);
                            }

                            &:hover {
                                background-color: $light_background_color;
                            }
                        }
                    }

                    svg {
                        color: white;
                        cursor: pointer;
                        position: absolute;
                        width: 10px;
                    }
                }

                &:hover {
                    border-top-color: $light_background_color;
                    border-left-color: $light_background_color;
                    border-right-color: $light_background_color;
                    border-bottom-color: $light_background_color;
                }
            }

            .card-footer {
                grid-column: 1/3;
                grid-row: 3/4;
                position: relative;

                span {
                    color: white;
                    position: absolute;
                    right: 0;
                    bottom: 0;
                }
            }

        }
    }
</style>