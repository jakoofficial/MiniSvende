<script>
</script>

<div class="pageContents">
	<div id="recommended">
		<div id="carosel">
			<div class="movieCapsule"></div>
			<div class="movieCapsule"></div>
			<div class="movieCapsule"></div>
			<div class="movieCapsule"></div>
		</div>
	</div>
	<div id="categories">
		<div id="catTitle">
			<h1>Categories</h1>
			<span></span>
		</div>
		<div id="CatCapsules">
			<div class="capsule"></div>
			<div class="capsule"></div>
			<div class="capsule"></div>
			<div class="capsule"></div>
			<div class="capsule"></div>
			<div class="capsule"></div>
			<div class="capsule"></div>
			<div class="capsule"></div>
		</div>
	</div>
</div>

<!-- Styleing for the page -->
<style>
	.pageContents {
		display: block;
		height: 90vh;
	}

	/* Recommendations */
	#recommended {
		width: 100%;
		height: 45%;
		align-content: center;
	}
	#carosel {
		height: 55%;
		margin: auto;
		width: 100%;
		justify-content: center;
		display: flex;
	}
	.movieCapsule {
		background-color: rgb(185, 185, 185);
		width: 20%;
		height: 100%;
		border-radius: 40px;
		margin: 0px 0.5%;
	}

	/* Categories */

    #categories {
    display: flex;
    flex-direction: column;
    height: 50vh; /* Optional: Set a max height if needed */
    width: 100%;
}

#categories #catTitle {
    width: 100%;
    display: flex;
    align-items: center; /* Vertically centers title and line */
}

#categories #catTitle h1 {
    min-width: 5%;
    margin-right: 10px;
}

#categories #catTitle span {
    margin: auto 0px;
    width: 90%;
    background-color: aliceblue;
    height: 2px;
}

#categories #CatCapsules {
    width: 100%;
    margin: auto;
    gap: 3%;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    flex-grow: 1; /* Takes remaining space */
}

#categories #CatCapsules .capsule {
    background-color: rgb(185, 185, 185);
    width: 18%;
    border-radius: 40px;
    margin: 0 0 25px 0;
    /* Remove height: 100%; to allow natural sizing */
    aspect-ratio: 2;
}
</style>
