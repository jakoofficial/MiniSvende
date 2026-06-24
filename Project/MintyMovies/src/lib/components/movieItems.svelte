<script>
    import {goto} from '$app/navigation'
	let { movieID, movieTitle, movieDesc, premium} = $props();

    async function gotomovies() {
        goto(`./watchmovie?m=${movieID}`);
    }

</script>

<button onclick={gotomovies} class="movieItem">
	<div id="itemContent">
			<p>{movieID}</p>
			<p>{movieTitle}</p>
			<p>{movieDesc}</p>
			<p>{premium}</p>
	</div>
</button>

<style>
	.movieItem {
        background-color: rgb(78, 78, 78);
		border-radius: 50px;
		height: 250px; /* Optional: Fixed height */
		align-content: center;
        border: none;
        cursor: pointer;
	}
    .movieItem:hover{
        border-bottom: var(--HoverColor) 6px solid;
    }
	#itemContent {
		margin: auto;
		width: 90%;
		height: 90%;
	}
    /* button{
        width: 100%;
        height: 100%;
        border: none;
        background-color: transparent;
        cursor: pointer;
    } */
	p {
		font-size: 20px;
		color: black;
	}
</style>
