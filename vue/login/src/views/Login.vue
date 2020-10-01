<template>
    <div class="card auth-container">
        <div class="section-container" :class="{'section-container-reverse':loginSectionSelected}">
            <SignInSection v-if="loginSectionSelected"/>
            <SignUpSection v-else/>
        </div>
        <div class="section-control" :class="{'section-control-reverse':loginSectionSelected}">
            <h1>{{login_indicator}}</h1>
            <button v-on:click="toggleAuthSections">{{btnValue}}</button>
        </div>
    </div>
</template>

<script>
    import SignInSection from "../components/SignInSection";


    export default {
        name: "Login",
        components: {
            SignInSection,
            SignUpSection: () => import( '../components/SignUpSection'),
        },
        data: () => ({
            loginSectionSelected: true
        }),
        computed: {
            btnValue: function () {
                return this.loginSectionSelected ? "Sign up" : "Sign in"
            },
            login_indicator: function () {
                return this.loginSectionSelected ? "Sign in" : "Sign up"
            }
        },
        methods: {
            toggleAuthSections: function () {
                this.loginSectionSelected = !this.loginSectionSelected;
            }
        }
    }
</script>

<style lang="scss">
    @import "../styles/default";

    $parent_width: 900px;
    $small_width: 300px;
    $small_time: 1.2s;
    $big_time: 1.5s;

    .auth-container {
        width: 90%;
        height: 90%;
        display: flex;


        .section-control {
            background-color: $primary_color;
            color: white;
            height: 100%;
            width: 30%;

            display: flex;
            justify-content: space-around;
            align-items: center;
            flex-direction: column;

            h1 {
                color: white;
            }

            button {
                background-color: white;
                color: $primary_color;
            }

            transition: left $small_time;
        }

        .section-container {
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: auto;
            width: 70%;
        }


        .section-container-reverse {

        }

        .section-control-reverse {

        }
    }

    @media screen and (max-width: 650px) {
        .auth-container {
            display: flex;
            flex-direction: column-reverse;

            .section-container {
                flex: 1;
                width: 100%;
                overflow: auto;
                padding-top: 150px;
            }

            .section-control {
                flex-basis: 100px;
                flex-direction: row;
                width: 100%;
            }
        }
    }
</style>