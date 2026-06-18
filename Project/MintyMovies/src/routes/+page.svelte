<script>
</script>

<div class="pageContents">
	<div id="recommended">
		<div class="movieCapsule"></div>
		<div class="movieCapsule"></div>
		<div class="movieCapsule"></div>
		<div class="movieCapsule"></div>
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
	.movieCapsule {
		background-color: rgb(185, 185, 185);
		width: 20%;
		height: 50%;
		border-radius: 40px;
		display: inline-block;
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
