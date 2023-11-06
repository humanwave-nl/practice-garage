<template>
    <modal
        title="New garage"
        @close="$emit('close')"
    >
        <new-garage></new-garage>
</modal>
</template>

<script>
    import Modal from './modal'
    import NewGarage from "./new-garage";
    export default {
        name: "new-garage-dialog",
        components: {
            NewGarage,
            Modal
        }
    }
</script>

<style scoped>

</style>