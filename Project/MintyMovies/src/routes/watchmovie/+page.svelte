<script>
	import { Post, SetSessionToken, GetSessionToken, Get } from '$lib/DataFetcher';
	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	const movieID = parseInt($page.url.searchParams.get('m'));

	let ses = '';
	let loggedin = $state(false);
	let user;
	let movie = $state({});
	let movielink = $state('');
	let ready = $state(false);
	let duration = $state(0);
	let vol = $state(0.25);

	onMount(async () => {
		ses = GetSessionToken();
		if (ses) {
			user = await Get('getUserBySession', { 'session-token': ses });

			movie = await Get('getMovieByID', { 'movie-id': movieID });
			movielink = movie.movie_link;
			ready = true;
			loggedin = true;
		} else {
			loggedin = false;
		}
	});
</script>

<div class="pageContents">
	{#if ready == true}
		<div id="panel">
			<video src={movielink} bind:volume={vol} bind:duration controls>
				<track kind="captions" />
				<track kind="descriptions" />
			</video>
			<div id="movieInfo">
				<div id="infoContent">
					<p>{movie.movie_title} ({movie.release_year})</p>
					<p>{movie.movie_desc}</p>
					<p>Duration: ~{parseInt(duration / 60)} min</p>
				</div>
			</div>
		</div>
        {:else}
        <div>
            <h1>Getting the movie ready!</h1>
        </div>
	{/if}
</div>

<!-- Styleing for the page -->
<style>
	.pageContents {
		height: 85vh;
		transform: translateY(3%);
		/* align-content: center; */
	}
	#panel {
		width: 100%;
		height: 100%;
		display: flex;
		justify-content: center;
		gap: 1%;
	}
	video {
		transform: translateY(8%);
		width: 80%;
		height: 90%;
	}
	#movieInfo {
		width: 19%;
		height: 50%;
		border-radius: 25px;
		background-color: rgb(172, 172, 172);
		align-content: center;
	}
	#infoContent {
		/* background-color: bisque; */
		width: 90%;
		height: 95%;
		margin: auto;
	}
	#infoContent p {
		height: 10%;
		color: rgb(7, 7, 7);
		font-size: 20px;
	}
	#infoContent p:first-of-type {
		font-size: 24px;
		width: 100%;
		margin-bottom: 10%;
		text-wrap: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
		align-content: center;
	}
	#infoContent p:nth-of-type(2) {
		height: 70%;
	}
	#infoContent p:nth-of-type(3) {
		align-content: center;
	}
</style>
