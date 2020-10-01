<template>
    <div id="app">
        <Toaster/>
        <ConfirmationModal/>
        <Inviter/>
        <nav>
            <router-link to="/">Notebook</router-link>
            <div class="menu-container">
                <div class="icon-wrapper" v-on:click="menu_visible=!menu_visible">
                    <font-awesome-icon :icon="['fas','bars']"></font-awesome-icon>
                </div>
                <ul class="menu" v-if="menu_visible">
                    <li>
                        <router-link to="/">Home</router-link>
                    </li>
                    <li>
                        <a href="#" v-on:click="inviting">Invite</a>
                    </li>
                    <li>
                        <a href="#" v-on:click="logout" style="color: red">Logout</a>
                    </li>
                </ul>
            </div>
        </nav>
        <div id="r-view">
            <CollectionView v-if="collectionViewEnabled"/>
            <CalendarView v-else/>
        </div>
    </div>
</template>

<style lang="scss">
    @import "styles/default";

    nav {
        justify-content: space-between;
        padding-right: 30px;

        .menu-container {
            position: relative;

            .icon-wrapper {
                height: 20px;
                width: 20px;

                svg {
                    height: 20px;
                    width: 20px;
                }
            }

            .menu {
                position: absolute;
                z-index: 1;
                right: 0;
                border: 1px solid $primary_color;

                li {
                    width: 70px;
                    display: inline-block;
                    height: 35px;
                    padding-top: 8px;
                    background-color: #fafafa;
                    text-align: center;

                    &:hover {
                        background-color: #fafafa;
                    }
                }
            }
        }

    }

    @media screen and (min-width: 300px) {
        nav {
            .menu-container {
                .icon-wrapper {
                    display: none;
                }

                .menu {
                    position: relative;
                    border: 0;

                    li {
                        background-color: transparent;
                    }
                }
            }
        }
    }
</style>
<script>
    import CollectionView from "./components/CollectionView";
    import {mapGetters} from "vuex";
    import CalendarView from "./components/CalendarView";
    import Toaster from "./components/Toaster";
    import Inviter from "./components/inviter";
    import ConfirmationModal from "./components/modals/ConfirmationModal";

    export default {
        components: {
            Toaster, CalendarView, CollectionView, ConfirmationModal, Inviter
        },
        computed: {
            ...mapGetters(['collectionViewEnabled'])
        },
        data() {
            return {
                menu_visible: true
            }
        },
        methods: {
            logout() {
                console.log("to delete");
                this.deleteCookie('token');
                document.location.replace('/');
            },
            inviting:async function(){
                await this.$invite();
            },
            deleteCookie(cookie_name) {
                const d = new Date();
                d.setTime(d.getTime() - (24 * 60 * 60 * 1000));
                const expires = "expires=" + d.toUTCString();
                document.cookie = cookie_name + "=" + ";" + expires + ";path=/";
            }
        }
    }
</script>