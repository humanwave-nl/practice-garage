<template>
	<div class="grid-container">
		<div class="title">
			<h1>Garages</h1>
			<new-garage @change="garageList=$event"></new-garage>

		</div>
		<ul class="list-group">
		    <li v-for="g in garageList" class="list-group-item">
				<!-- when a garage item is deleted it will raise change event and return the new list -->
				<garage-list-item :garage="g" @change="garageList=$event">hello</garage-list-item>
			</li>
		</ul>
	</div>
</template>

<script>
    import GarageListItem from "./garage-list-item";
    import GarageForm from "./garage-form";
	import NewGarage from "./new-garage";

	export default {
		name: 'garage-list',
		components: {NewGarage, GarageListItem, GarageForm},
		data: function () {
			return {
				garageList: [],
                garageDialog: true,
			}
		},
		methods: {
			load() {
				$.ajax({
					type: 'GET',
					url: `/garages/`,
					contentType: 'application/json',
					timeout: 60000
				}).then((data) => {
					console.log(data)
					this.garageList = data
				}).always(() => {
					// this.loading = false
				})
			},
		},
		created: function() {
			this.load();
		}
	}

</script>

<style scoped>
	.grid-container {
		display: grid;
		grid-template-columns: 2fr 6fr;
		grid-gap: 10px;
		grid-auto-rows: min-content;
		grid-template-areas:
			"title garage-list ";
	}

	.title {
        grid-area: title;
		margin-right: 20px;
    }
	.list-group {
        grid-area: garage-list;
    }
    .add-garage {
        margin: 4px;
    }

</style>
