<script>
	import { goto } from '$app/navigation';
	let { movieID, movieTitle, movieDesc, premium, releaseYear } = $props();

	async function gotomovies() {
		goto(`./watchmovie?m=${movieID}`);
	}
</script>

<button onclick={gotomovies} class="movieItem">
	<div id="itemContent">
        {#if premium}
        <div id="banner"></div>
        {/if}
        <p>{movieTitle} <span style="font-size: 18px;">({releaseYear})</span></p>
		<p>{movieDesc}</p>
		<p>{premium}</p>
	</div>
</button>

<style>
	.movieItem {
		background-color: rgb(92, 92, 92);
		border-radius: 50px;
		height: 250px; /* Optional: Fixed height */
		align-content: center;
		border: none;
		cursor: pointer;
	}
	.movieItem:hover {
		border-bottom: var(--HoverColor) 6px solid;
	}
	#itemContent {
		margin: auto;
		width: 90%;
		height: 90%;
	}
	p {
		font-size: 20px;
		color: black;
	}
	p span {
		color: black;
	}
	p:first-of-type {
		font-size: 26px;
		margin-bottom: 10px;
	}
	#banner {
		background-color: rgb(129, 73, 69);
		position: absolute;
        transform: translateY(-15px);
		/* clip-path: polygon(17% 0, 22% 0, 22% 15%, 17% 22%); */
		clip-path: polygon(15% 0, 75% 0, 75% 35%, 15% 25%);
		width: 100px; /* Adjust as needed */
		height: 150px; /* Adjust as needed */
		z-index: 10;
	}
</style>
