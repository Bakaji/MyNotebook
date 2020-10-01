<template>
    <div class="sign-wrapper">
        <form action="#" v-on:submit.prevent="attemptLogin">
            <label for="username_field">User name</label>
            <input type="text" autocomplete="off" required id="username_field" v-model="username">
            <label for="password_field">Password</label>
            <input type="password" autocomplete="off" required id="password_field"
                   v-model="password">
            <input type="submit" value="Submit" :disabled='invalidInput'
                   :class="{'invalid':invalidInput}"/>
        </form>
    </div>
</template>

<script>
    import {loggedSuccessfully, loginFailed} from "../assets/login_functions";

    export default {
        name: "loginSection",
        data: () => ({
            username: '',
            password: ''
        }),
        methods: {
            attemptLogin: async function () {
                const r_data = {
                    username: this.username,
                    password: this.password
                };

                const result = await fetch('/api/auth/login/', {
                    method: 'POST',
                    headers: {
                        'Content-type': 'application/json'
                    },
                    body: JSON.stringify(r_data),
                }).then(resp => resp.json()).catch(() => loginFailed());
                console.log(result);

                if (result) {
                    const t = result['token'];
                    if (t) {
                        loggedSuccessfully(t);
                        return;
                    }
                }
                loginFailed()

            },
        },
        computed: {
            invalidInput: function () {
                return this.username === "" || this.password === "";
            }
        }
    }
</script>

<style lang="scss">

</style>