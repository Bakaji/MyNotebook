import axios from "axios";

export default {
    state: {
        __state_collections: [],
        __state_notes: [],
        __state_first_collection_load: false,
        __state_first_collection_notes_load: false,
        __state_selected_collection: null,
        __state_selected_note: null
    },

    getters: {
        getCollections: (state) => state.__state_collections,
        getCollectionNames: (state) => state.__state_collections.map(coll => coll.collection_name),
        getNotesNames: (state) => state.__state_notes.map(m => m.note_title),
        getSelectedCollection: (state) => state.__state_selected_collection,
        isCollectionsLoaded: (state) => state.__state_first_collection_load,
        isCollectionNotesLoaded: (state) => state.__state_first_collection_notes_load,
        collectionExists: (state) => (collection_id) => state.__state_collections.find(a => a.collection_id.toString() === collection_id.toString()) !== undefined,
        noteExists: (state) => (note_id) => state.__state_notes.find(a => a.note_id.toString() === note_id.toString()) !== undefined,

        getNotes: (state) => state.__state_notes,
        getSelectedNote: (state) => state.__state_selected_note,
        noteSelected: (state) => state.__state_selected_note !== null
    },
    mutations: {
        setCollections: function (state, collections) {
            state.__state_collections.length = 0;
            for (let i = 0; i < collections.length; i++)
                state.__state_collections.push(collections[i]);
            state.__state_first_collection_load = true;
            return state;
        },
        setSelectedCollection: (state, collection) => {
            state.__state_selected_collection = collection;
            state.__state_notes.length = 0;
            state.__state_selected_note = null;
            state.__state_first_collection_notes_load = false;
            return state
        },
        setSelectedCollectionById: (state, collection_id) => {
            state.__state_selected_collection = state.__state_collections.find(a => a.collection_id.toString() === collection_id.toString());
            state.__state_notes.length = 0;
            return state
        },
        setSelectedNoteById: (state, note_id) => {
            state.__state_selected_note = state.__state_notes.find(a => a.note_id.toString() === note_id.toString());
            return state
        },
        setSelectedCollectionNotes: (state, notes) => {
            state.__state_notes.length = 0;
            if (notes) {
                for (let i = 0; i < notes.length; i++)
                    state.__state_notes.push(notes[i])
            }
            state.__state_selected_note = notes.length > 0 ? state.__state_notes[0] : null;
            state.__state_first_collection_notes_load = true;
            return state;
        },
        setSelectedNote: (state, note) => {
            state.__state_selected_note = note;
            return state;
        }
    },
    actions: {
        loadCollectionsFromServer: async function ({commit}) {
            const rest = await axios.get('/api/collections/');
            if (rest.status === 200) {
                const collections = rest.data;
                commit("setCollections", collections)
            }
        },
        loadSelectedCollectionNotes: async function ({commit, state}) {
            const collect_id = state.__state_selected_collection.collection_id;
            if (collect_id) {
                const result = await axios.get(`/api/collections/${collect_id}/notes/`);
                if (result.status === 200) {
                    commit("setSelectedCollectionNotes", result.data)
                }
            }
        },
        createNewCollection: async function ({dispatch}, data) {
            const result = await axios.post('/api/collections/create/', data);
            if (result.status === 200) {
                console.log("collection successfully created");
                dispatch("hideAddCollectionModal");
                dispatch("loadCollectionsFromServer");
            } else {
                dispatch("setAddCollectionErrors", result.data)
            }
        },
        createNewNote: async function ({dispatch, state}, data) {
            const coll_id = state.__state_selected_collection.collection_id;
            if (coll_id) {
                const result = await axios.post(`/api/collections/${coll_id}/notes/create/`, data);
                if (result.status === 200) {
                    console.log("note successfully created");
                    dispatch("loadSelectedCollectionNotes");
                } else {
                    dispatch("setAddCollectionErrors", result.data)
                }
            }
        },
        editSelectedNote: async function ({dispatch, state}, data) {
            const coll_id = state.__state_selected_collection.collection_id;
            if (coll_id) {
                const note_id = state.__state_selected_note.note_id;
                const result = await axios.put(`/api/collections/${coll_id}/notes/${note_id}/update/`, data);
                if (result.status === 200) {
                    console.log("note successfully updated");
                    dispatch("loadSelectedCollectionNotes");
                } else {
                    dispatch("setAddCollectionErrors", result.data)
                }
            }
        },
        deleteNewNote: async function ({dispatch, state}) {
            const coll_id = state.__state_selected_collection.collection_id;
            if (coll_id) {
                const note_id = state.__state_selected_note.note_id;
                const result = await axios.delete(`/api/collections/${coll_id}/notes/${note_id}/delete/`);
                if (result.status === 200) {
                    console.log("note successfully deleted");
                    dispatch("loadSelectedCollectionNotes");
                }
            }
        },
        selectCollection: ({commit}, collection) => {
            commit('setSelectedCollection', collection)
        },
        editSelectedCollection: async function ({dispatch, state}, data) {
            const result = await axios.put(`/api/collections/${state.__state_selected_collection.collection_id}/update/`, data);
            if (result.status === 200) {
                console.log("collection updated successfully");
                dispatch("hideEditCollectionModal");
                dispatch("loadCollectionsFromServer")
            }
        },
        deleteSelectedCollection: async function ({dispatch, state}) {
            const result = await axios.delete(`/api/collections/${state.__state_selected_collection.collection_id}/delete/`);
            if (result.status === 200) {
                dispatch("loadCollectionsFromServer")
            }
        },
        selectNote: ({commit}, note) => {
            commit("setSelectedNote", note);
        },
    },
}