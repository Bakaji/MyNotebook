<template>
    <div id="inviteUsersModal" class="flex-container modal-container" v-on:click="hideThis">
        <div class="modal-card" v-on:click="doNothing">
            <div class="modal-content">
                <h1>Invite people to join this notebook</h1>
                <h3>link</h3>
                <p>{{this.link}}</p>
                <h3>invitation token</h3>
                <p><span id="tokenHolder"></span></p>
            </div>
        </div>
    </div>
</template>

<script>
    import Vue from "vue";
    import axios from "axios";

    Vue.prototype.$invite = async () => {
        const result = await axios.get('/api/auth/request_token/');
        if (result.status === 200) {
            document.getElementById("tokenHolder").innerText = result.data.token;
            document.getElementById("inviteUsersModal").style.display = "flex";

        }
    };
    export default {
        name: "inviter",
        computed: {
            link: () => {
                const getUrl = window.location;
                return getUrl.protocol + "//" + getUrl.host + "/" +
                    getUrl.pathname.split('/')[1];
            },
        },
        methods:{
            hideThis(){
                document.getElementById("inviteUsersModal").style.display = "none";
            },
            doNothing(e){
                e.stopPropagation();
            }
        }
    }
</script>

<style lang="scss">
    @import "src/styles/default";

    #inviteUsersModal {
        display: none;
        p {
            color: $primary_color;
            font-family: $secondary_font;
            font-weight: bold;
            font-size: 18px;
        }

        .modal-content {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }
        h1{
            flex-basis: 100%;
        }
        h3{
            flex-basis: 100%;
        }
        p{
            flex-basis: 100%;
        }

    }
    @media screen and (min-width: 400px){
        #inviteUsersModal{
            h3 {
                flex-basis: 30%;
            }

            p {
                flex-basis: 60%;
            }
        }
    }
</style>