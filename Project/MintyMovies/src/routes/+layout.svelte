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
	<nav>
		<a href="./">Home</a>
		<a href="./categories">Categories</a>
		<a href="./tokenstation">Token Station</a>
		<a href="./subscriptions">Subscriptions</a>
		<a href="./profile">Profile</a>
	</nav>
	<div id="content">
		{@render children()}
	</div>
</section>
