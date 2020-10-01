<template>
    <div id="confirmationModal" class="modal-container flex-container" v-on:click="hideModal">
        <div class="modal-card" v-on:click="do_nothing">
            <div class="modal-content">
                <h2>Confirmation</h2>
                <h3 id="confirmationText">Are you sure you want to perform following actions ? </h3>
                <div class="conf-buttons">
                    <button id="yes">Yes</button>
                    <button id="no" v-on:click="hideModal">No</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Vue from "vue";

    let callback = null;

    Vue.prototype.$showDialog = (text, newCallback) => {
        const confirmationModal = document.getElementById("confirmationModal");
        if (confirmationModal) {
            confirmationModal.querySelector('#confirmationText').innerText = text || "";
            const yesBtn = confirmationModal.querySelector('#yes');
            if (callback) {
                //delete old confirmation callback
                yesBtn.removeEventListener("click", callback);
            }
            callback = function () {
                newCallback();
                confirmationModal.style.display = 'none';
            };
            yesBtn.addEventListener("click", callback);
            confirmationModal.style.display = 'flex';
        } else {
            console.error("cannot find confirmation modal placeholder")
        }
    };
    export default {
        name: "DeleteConfirmationModal",
        methods: {
            do_nothing: (e) => {
                e.stopPropagation();
            },
            hideModal: function () {
                const confirmationModal = document.getElementById("confirmationModal");
                confirmationModal.style.display = 'none';
            }
        }
    }
</script>

<style lang="scss" scoped>
    .modal-card {
        flex-direction: column;

        .modal-content {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            text-align: center;
            grid-row-gap: 20px;

            h2 {
                flex-basis: 100%;
            }

            h3 {
                flex-basis: 100%;
            }
        }
    }

    .conf-buttons {
        height: 40px;
        flex-basis: 100%;
        align-self: flex-end;
        display: flex;
        justify-content: space-between;

        #yes {
            flex-basis: 100%;
            height: 40px;
            background-color: red;
        }

        #no {
            flex-basis: 100%;
            height: 40px;
        }
    }

    #confirmationModal {
        display: none;
    }

    @media screen and (max-width: 610px) {
        .conf-buttons {
            flex-wrap: wrap;
            width: 100%;
            justify-content: center;

            button {
                flex-basis: 100%;
            }
        }
    }
</style>