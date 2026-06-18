<script>
	import favicon from '$lib/assets/favicon.svg';
	import home from '$lib/assets/home.svg';
	import cat from '$lib/assets/category.svg';
	import profile from '$lib/assets/profile.svg';
	import sub from '$lib/assets/subscription.svg';
	import ticket from '$lib/assets/ticket.svg';
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
		<p id="sitetitle">Minty Movies</p>
		<nav>
			<a href="./"><img src={home} alt="Home">
			<p class="hoverText">
				Home
				<span class="triangle"></span>
			</p>
			</a>
			<a href="./categories"><img src={cat} alt="Categories">
			<p class="hoverText">
				Categories
				<span class="triangle"></span>
			</p></a>
			<a href="./tokenstation"><img src={ticket} alt="Token Station">
			<p class="hoverText">
				Token Station
				<span class="triangle"></span>
			</p></a>
			<a href="./subscriptions"><img src={sub} alt="Subscription"><p class="hoverText">
				Subscription
				<span class="triangle"></span>
			</p></a>
			<a href="./profile"><img src={profile} alt="Profile"><p class="hoverText">
				Profile
				<span class="triangle"></span>
			</p></a>
		</nav>
	</div>
	<div id="content">
		{@render children()}
	</div>
</section>
