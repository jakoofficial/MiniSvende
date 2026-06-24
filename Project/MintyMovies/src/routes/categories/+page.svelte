<script>
	import { Post, SetSessionToken, GetSessionToken, Get } from '$lib/DataFetcher';
	import { onMount } from 'svelte';
	import MovieItems from '$lib/components/movieItems.svelte';

	let ses = '';
	let loggedin = $state(false);
	let user;
	let movies = [];
	let ready = $state(false);

	onMount(async () => {
		ses = GetSessionToken();
		if (ses) {
			user = await Get('getUserBySession', { 'session-token': ses });
            
			let movieList = await Get('getAllMovies');
			movies = movieList;
            console.log(movies);
			ready = true;
			loggedin = true;
		} else {
			loggedin = false;
		}
	});
</script>

<div class="pageContents">
	<h1>Categories</h1>
	<div id="panel">
		{#if ready == true}
			{#each movies as item}
				<MovieItems
					movieID={item.movie_id}
					movieTitle={item.movie_title}
					movieDesc={item.movie_desc}
					premium={item.premium}
				></MovieItems>
			{/each}
        {:else}
            <p>hello</p>
		{/if}
	</div>
</div>

<!-- Styleing for the page -->
<style>
	.pageContents {
		height: 85vh;
		transform: translateY(3%);
		/* align-content: center; */
	}

	#panel {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 10px;
		align-items: start;
		padding: 10px; /* Optional: Adds padding inside the panel */
	}
</style>
