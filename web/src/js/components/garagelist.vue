<template>
	<div class="grid-container">
		<div class="title">
			<h1>Garages</h1>
			<button type="button" class="btn" @click="garageDialog = true;">Add garage</button>
			<new-garage-dialog
				v-if="garageDialog"
				@update="updateList"
				@close="garageDialog = false;"
			/>
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
	import NewGarageDialog from "./new-garage-dialog"

	export default {
		name: 'garage-list',
		components: {NewGarage, GarageListItem, GarageForm, NewGarageDialog},
		data() {
			return {
				garageList: [],
                garageDialog: false,
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
			updateList(data) {
				this.garageList.push(data)
			}
		},
		created: function() {
			this.load();
		}
	}

</script>

<style scoped>
	.grid-container {
		display: grid;
        grid-template-columns: 1fr;
        grid-template-rows: 60px 1fr;
		grid-gap: 8px;
		grid-template-areas:
			"title"
			"garage-list";
	}

	.list-group {
        grid-area: garage-list;
    }
    .add-garage {
        margin: 4px;
    }

	.title {
        grid-area: title;
		display: flex;
		align-items: center; /* Vertical align the elements to the center */
	}

	h1 {
		margin: 0;
	}

	button {
		margin-left: auto; /* Push this element to the right */
	}

</style>
