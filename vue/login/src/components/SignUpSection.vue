<template>
    <div class="sign-wrapper">
        <form action="#" v-on:submit.prevent="tryRegister">
            <label for="inv_token_field">Invitation token</label>
            <input id="inv_token_field" v-model="invitation_code" type="text">
            <label for="username_field">Username</label>
            <input id="username_field" v-model="username" type="text">
            <label for="password_field">Password</label>
            <input id="password_field" v-model="password" type="password">
            <label for="conf_password_field">confirm password</label>
            <input id="conf_password_field" v-model="confirmation" type="password">
            <label for="email_field">Email</label>
            <input id="email_field" v-model="email" type="email">
            <input type="submit" value="Submit" :disabled='invalidInput'
                   :class="{'invalid':invalidInput}"/>
        </form>
    </div>
</template>

<script>
    import {loggedSuccessfully, loginFailed} from "../assets/login_functions";

    export default {
        name: "SignUpSection",
        data: () => ({
            invitation_code: '',
            username: '',
            password: '',
            confirmation: '',
            email: '',
        }),
        methods: {
            tryRegister: async function () {
                const r_data = {
                    inv_code: this.invitation_code,
                    username: this.username,
                    password: this.password,
                    password_confirmation: this.confirmation,
                    email: this.email
                };
                const result = await fetch('/api/auth/register/', {
                    method: 'POST',
                    headers: {
                        'Content-type': 'application/json'
                    },
                    body: JSON.stringify(r_data),
                }).then(resp => resp.json()).catch(() => loginFailed());
                if (result) {
                    const t = result['token'];
                    if (t) {
                        loggedSuccessfully(t);
                        return;
                    }
                }
                loginFailed()

            }
        },
        computed: {
            invalidInput: function () {
                return this.inv_code === '' || this.username === '' || this.password === ''
                    || this.confirmation !== this.password || this.email === '';
            }
        }
    }
</script>

<style lang="scss">
</style>