<template>
    <div class="flex-container">
        <div class="content" v-on:click="do_nothing">
            <h2>Add new note</h2>
            <form class="" v-on:submit.prevent="createNote">
                <label id="note_title_name" for="note_title_value">Note title</label>
                <input id="note_title_value" type="text" v-model="newNote.note_title"/>
                <span id="note_title_errors" class="errors">{{this.titleError}}</span>

                <label id="note_content_name" for="note_content_value">note content</label>
                <textarea id="note_content_value" v-model="newNote.note_content"/>
                <span id="note_content_errors" class="errors">{{contentError}}</span>

                <div class="button-container">
                    <button v-on:click="this.$router.go(-1)">Cancel</button>
                    <input type="submit" value="Create" :disabled='invalidInput'>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
    import {mapGetters} from "vuex";

    export default {
        name: "AddNote",
        data: () => ({
            newNote: {
                note_title: '',
                note_content: ''
            }
        }),
        methods: {
            do_nothing: (e) => {
                e.stopPropagation();
            },
            createNote: function () {
                const data = this.newNote;
                this.$store.dispatch("createNewNote", data);
                this.$router.go(-1);
            }
        },
        computed: {
            ...mapGetters(['getNotesNames']),
            titleError: function () {
                const note_name = this.newNote.note_title;
                if (note_name.match('^\\s*$'))
                    return "empty input";
                if (note_name.match('[^a-zA-Z0-9\\s]'))
                    return "name should be alphanumeric and spaces";
                if (this.getNotesNames.indexOf(note_name) >= 0)
                    return "title already used";
                return "";
            },
            contentError: function () {
                const description = this.newNote.note_content;
                if (description.match('^\\s*$'))
                    return "empty input";
                if (description.match('[^a-zA-Z0-9\\s]'))
                    return "name should be alphanumeric and spaces";
                return "";
            },
            invalidInput: function () {
                return this.titleError !== '' || this.contentError !== '';
            }
        }
    }
</script>

<style lang="scss">
    @import "../../styles/palette";

    $height: 50px;
    $small_height: 30px;
    .content {
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
        margin: auto;

        h2 {
            margin-bottom: 50px;
        }
    }

    form {
        width: 80%;
        display: flex;
        flex-wrap: wrap;

        label {
            flex-basis: 100%;
            height: 30px;
        }

        span {
            flex-basis: 100%;
            display: block;
            color: red;
            height: 30px;
            margin-bottom: 30px;
        }

        input, textarea {
            flex-basis: 100%;
        }

        textarea {
            height: 150px;
        }

        .button-container {
            flex-basis: 100%;

            button, input[type='submit'] {
                margin-top: 10px;
                float: right;
                width: 150px;
                height: 30px;
                margin-left: 30px;
            }

            button {
                background-color: red;
            }
        }
    }

    @media screen and (min-width: 800px) {
        form {
            label {
                flex-basis: 30%;
            }

            input, textarea {
                flex-basis: 70%;
            }
        }
    }
</style>