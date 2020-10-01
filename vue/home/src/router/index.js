import Vue from 'vue'
import VueRouter from 'vue-router'
import Collection_grid from "../components/collections/CollectionGrid";
import CollectionDetails from "../components/collections/CollectionDetails";
import NotFound from "../components/NotFound";
import store from "../store";
import AddNote from "../components/memo/AddNote";
import EditNote from "../components/memo/EditNote";


async function collectionExists(id) {

    if (store.getters.collectionExists(id)) {
        return true;
    }
    if (!store.getters.isCollectionsLoaded) {
        await store.dispatch("loadCollectionsFromServer");
    }

    if (store.getters.collectionExists(id)) {
        await store.commit("setSelectedCollectionById", id);
        return true;
    }
    return false;

}

async function collectionNoteExists(id, note_id) {
    const collection_exists = await collectionExists(id);
    if (collection_exists) {
        if (store.getters.noteExists(note_id)) {
            return true;
        }
        if (!store.getters.isCollectionNotesLoaded) {
            await store.dispatch("loadSelectedCollectionNotes");
        }

        if (store.getters.noteExists(note_id)) {
            await store.commit("setSelectedNoteById", note_id);
            return true;
        }
    }
    return false;
}

const checkExistence = async (to, from, next) => {
    const id = to.params["id"];
    const res = await collectionExists(id);
    if (res)
        next();
    else
        next({name: 'NotFound'});
};

const checkNoteExistence = async (to, from, next) => {
    const id = to.params["id"];
    const note_id = to.params["note_id"];
    const res = await collectionNoteExists(id, note_id);
    if (res)
        next();
    else
        next({name: 'NotFound'});
};
Vue.use(VueRouter);
const routes = [
    {
        path: '/',
        name: 'CollectionsMain',
        component: Collection_grid,
        beforeEnter: (to, from, next) => {
            const redirect = localStorage.getItem("redirect_to");
            if (redirect) {
                localStorage.removeItem("redirect_to");
                next(redirect);
            }
            next()
        }
    },
    {
        path: '/collection/:id',
        name: 'CollectionDetails',
        component: CollectionDetails,
        beforeEnter: checkExistence
    },
    {
        path: '/collection/:id/create-note/',
        name: 'NoteCreate',
        component: AddNote,
        beforeEnter: checkExistence
    },
    {
        path: '/collection/:id/notes/:note_id/edit/',
        name: 'NoteEdit',
        component: EditNote,
        beforeEnter: checkNoteExistence
    },
    {
        path: '*',
        name: 'NotFound',
        beforeEnter: (to, from, next) => {
            next('/not-found')
        },
    },
    {
        path: '/not-found',
        name: 'nf',
        component: NotFound
    }
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});

export default router
