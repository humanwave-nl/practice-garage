<template xmlns:background-image="http://www.w3.org/1999/xhtml">
    <transition name="modal">
        <div class="modal-mask">
            <div class="modal-wrapper">
                <div class="modal-container">
                    <div class="modal-header">
                        <slot name="header">
                            <h3>
                                {{ title }}
                                <button
                                    type="button"
                                    class="btn btn-option"
                                    @click="$emit('close');"
                                    style="display: flex; justify-content: center;"
                                >
                                    <i class="fas fa-times fa-lg" style="margin: auto;"></i>
                                </button>
                            </h3>
                        </slot>
                    </div>
                    <div class="modal-body">
                        <slot />
                    </div>
                    <div class="modal-footer">
                        <slot name="footer" />
                    </div>
                </div>
            </div>
        </div>
    </transition>
</template>

<script>
    export default {
        name: 'Dialog',
        props: {
            title: {
                type: String,
                default: undefined,
            },
        },
    };
</script>

<style lang="css" scoped>
    .modal-mask {
        position: fixed;
        z-index: 9998;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        display: table;
        transition: opacity 0.3s ease;
    }

    .modal-wrapper {
        display: table-cell;
        vertical-align: middle;
    }

    .modal-container {
        width: 600px;
        margin: 0px auto;
        padding: 20px 30px;
        background-color: #fff;
        border-radius: 2px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
        transition: all 0.3s ease;
        font-family: Helvetica, Arial, sans-serif;
    }

    .modal-header h3 {
    margin-top: 0;
    color: #42b983;
    }

    .modal-body {
    margin: 20px 0;
    }

    .modal-default-button {
    float: right;
    }

    /*
    * The following styles are auto-applied to elements with
    * transition="modal" when their visibility is toggled
    * by Vue.js.
    *
    * You can easily play with the modal transition by editing
    * these styles.
    */

    .modal-enter-from, .modal-leave-to {
    opacity: 0;
    }

    .modal-enter-active .modal-container,
    .modal-leave-active .modal-container {
    -webkit-transform: scale(1.1);
    transform: scale(1.1);
    }

    h3 {
        display: grid;
        grid-template-columns: 1fr 22px;
    }

</style>
