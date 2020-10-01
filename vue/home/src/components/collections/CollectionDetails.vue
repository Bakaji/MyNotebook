<template>
    <div class="collection-details" :key="this.getSelectedCollection.collection_id">
        <div class="header">
            <div class="menu-wrapper" v-on:click="menuToggle">
                <font-awesome-icon :icon="['fas','bars']"></font-awesome-icon>
                <span>Notes</span>
            </div>
            <button>
                <router-link :to="add_note_link">Add note</router-link>
            </button>
        </div>
        <div class="collection-content">
            <ul id="note_list" class="notes-list" :class="{'hidden':menu_hidden}"
                :key="menu_hidden">
                <li v-for="item in getNotes" :key="item.note_id">
                    <div class="note-container" v-on:click="selectThis(item)">
                        <div class="note-title">
                            {{item.note_title}}
                        </div>
                    </div>
                </li>
            </ul>
            <div class="details-form" v-if="noteSelected" :key="this.getSelectedNote.note_id">
                <div class="note-header">
                    <h3>Note: {{this.getSelectedNote.note_title}}</h3>
                    <h4>last update : {{this.formedDate}}</h4>
                </div>
                <p>{{this.getSelectedNote.note_content}}</p>
                <div class="buttons">
                    <button>
                        <router-link :to="edit_selected_note_link">
                            Edit
                        </router-link>
                    </button>
                    <button class="danger" v-on:click="promptDelete">Delete</button>
                </div>
            </div>
            <div class="details-form" v-else>
                <h3>Select note to view details</h3>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapActions, mapGetters} from "vuex";

    export default {
        name: "CollectionDetails",
        computed: {
            ...mapGetters(['getSelectedCollection', 'getNotes', 'noteSelected',
                'getSelectedNote']),
            add_note_link: function () {
                return `/collection/${this.getSelectedCollection.collection_id}/create-note/`;
            },
            edit_selected_note_link: function () {
                const s = this.getSelectedNote;
                if (s)
                    return `/collection/${this.getSelectedCollection.collection_id}/notes/${s.note_id}/edit/`;
                return "";
            },
            formedDate: function () {
                const date = this.getSelectedNote.note_update_date;
                const
                    y = date.slice(0, 4), m = date.slice(5, 7), d = date.slice(8, 10),
                    h = date.slice(11, 13), mi = date.slice(14, 16),
                    s = date.slice(17, 19);
                return `${y}-${m}-${d} at ${h}:${mi}:${s}`;
            }
        },
        data: function () {
            return {
                menu_hidden: false
            }
        },
        created() {
            this.$store.dispatch("loadSelectedCollectionNotes");
        },
        methods: {
            ...mapActions(['deleteNewNote']),
            goHome: function () {
                this.$store.dispatch("goHome")
            },
            menuToggle: function () {
                if (window.innerWidth <= 680) {
                    this.menu_hidden = !this.menu_hidden;
                } else {
                    this.menu_hidden = false;
                }
            },
            selectThis: async function (item) {
                this.$store.dispatch("selectNote", item);
                this.menuToggle();
            },
            promptDelete: function () {
                this.$showDialog("Are you sure you want to delete this note ?", this.deleteNewNote);
            }
        },

    }
</script>

<style lang="scss">
    @import "../../styles/default";

    .collection-details {
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }

    .header {
        flex: 0;
        flex-basis: 75px;
        padding-top: 16px;
        display: flex;
        justify-content: space-between;
        align-items: center;

        button {
            background-color: transparent;
            color: $primary_color;
            font-size: 16px;
        }
    }

    .menu-wrapper {
        color: $primary_color;
        cursor: pointer;

        span {
            margin-left: 15px;
        }
    }

    .collection-content {
        flex: 1;
        display: flex;
        width: 100%;
        justify-content: flex-start;
        position: relative;
    }

    .notes-list {
        width: 100%;
        height: 100%;
        position: absolute;
        background-color: #fafafa;
        top: 0;
        left: 0;
    }

    .details-form {
        flex: 1;
        padding: 15px;
        display: flex;
        flex-direction: column;

        p {
            display: block;
            margin-top: 20px;
            flex: 1;
        }

        p::before {
            content: "note content :";
            display: block;
            color: $primary_color;
            text-decoration: underline;
            margin: 10px 0;
        }

        .buttons {
            flex-basis: 70px;
            display: flex;
            align-items: center;
            justify-content: space-around;

            button {
                height: 40px;
                width: 120px;
                margin-left: 20px;
                a{
                    display: flex;
                    height: 100%;
                    width: 100%;
                    align-items: center;
                    justify-content: center;
                    color: white;
                }
            }

            button.danger {
                background-color: red;
                color: white;
            }
        }
    }

    .note-header {
        flex: 0;
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        width: 100%;

        h3, h4 {
            flex-basis: 260px;
        }

        h4 {
            text-align: end;
        }
    }

    .hidden {
        display: none;
    }

    @media screen and (min-width: 680px) {
        .notes-list {
            width: 300px;
        }
        .details-form {
            position: absolute;
            left: 300px;
            top: 0;
            height: 100%;
            width: calc(100% - 300px);

            .buttons {
                justify-content: flex-end;
            }
        }
    }

    .note-container {
        border-bottom: 1.5px solid #dadada;
        cursor: pointer;
        background-color: $light_background_color;
        color: $primary_color;
        height: 50px;
        display: flex;
        align-items: center;
        padding-left: 15px;
    }

    .note-container:hover {
        background-color: #dadada;
    }

    .note-container:active {
        background-color: $primary_color;
        color: $light_background_color;
    }
</style>