<script>
	import favicon from '$lib/assets/favicon.svg';
	import '../lib/css/style.css';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />

	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
	<link
		href="https://fonts.googleapis.com/css2?family=Pangolin&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<section>
	<div id="topbar">
		<p id="sitetitle">MintyMovies</p>
		<nav>
			<a href="./">Ho</a>
			<a href="./categories">Ca</a>
			<a href="./tokenstation">TS</a>
			<a href="./subscriptions">Su</a>
			<a href="./profile">Pr</a>
		</nav>
	</div>
	<div id="content">
		{@render children()}
	</div>
</section>
