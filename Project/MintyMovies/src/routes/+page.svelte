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
			<h1>Category</h1>
			<span></span>
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
		height: 50%;
        align-content: center;
	}
    #carosel {
        height: 45%;
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
		min-height: 50%;
	}
	#categories #catTitle {
		width: 100%;
		display: flex;
		align-content: center;
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
</style>
