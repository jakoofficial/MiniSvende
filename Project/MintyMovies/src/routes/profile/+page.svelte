<script>
	import { Post, SetSessionToken, GetSessionToken, Get } from '$lib/DataFetcher';
	import { onMount } from 'svelte';

	let username = '';
	let password = '';

	// Use the props from `load`
	let ses = '';
	let loggedin = $state(false);
	let user;
	let subtype = "tbd";

	onMount(async () => {
		ses = GetSessionToken();
		if (ses) {
			user = await Get('getUserBySession', { 'session-token': ses });
			loggedin = true;

		} else {
			loggedin = false;
		}
	});
	async function Signin() {
		const data = await Post('signin', {
			username: username,
			password: password
		});
		SetSessionToken(data[1].session_key);
		loggedin = true;
		window.location.reload(true);
	}
	async function Signup() {
		const data = await Post('createUser', {
			username: username,
			password: password
		});
	}
</script>

<div class=" {!loggedin ? 'pageContentsSignIn' : 'pageContentsSignedIn'}">
	{#if loggedin}
		<div id="profile">
			<div class="panel">
				<p>{user.username}</p>
				<hr>
				<p>Subscription: {user.sub ? "Premium" : "Free user"}</p>
			</div>
		</div>
	{/if}
	<div class={loggedin ? 'signedout' : ''} id="signinArea">
		<div id="form">
			<p id="formTitle">Sign in</p>
			<input bind:value={username} type="text" placeholder="Username" />
			<input bind:value={password} type="password" placeholder="Password" />
			<div id="formButtons">
				<button onclick={Signup}> Register </button>
				<button onclick={Signin}> Sign in </button>
			</div>
		</div>
	</div>
</div>

<!-- Styleing for the page -->
<style>
	.pageContentsSignIn {
		display: block;
		height: 90vh;
		align-content: center;
	}
	.pageContentsSignedIn {
		display: block;
		height: 90vh;
	}
	#profile {
		height: 50%;
		width: 50%;
		margin: auto;
		/* transform: translateY(40%); */
		align-content: center;
	}
	#profile .panel {
		display: block;
		background-color: #afafaf;
		width: 100%;
		height: 50%;
		border-radius: 25px;
	}
	.panel hr {
		transform: translateX(-5px) translateY(15px);
		width: 95%;
		margin:auto;
		margin-bottom:15px;
	}
	.panel p{
		color: #272727;
		font-weight: bold;
		transform: translateX(30px) translateY(10px);
		font-size: 18px;
	}
	.panel p:first-of-type {
		font-size: 26px;
		text-transform: capitalize;
	}
	
	#signinArea {
		background-color: #444444;
		width: 35%;
		height: 35%;
		margin: auto;
		transform: translateY(-25%);
		border-radius: 35px;
		align-content: center;
	}
	.signedout {
		visibility: collapse;
	}
	#signinArea #form {
		width: 90%;
		height: 90%;
		margin: auto;
	}
	#signinArea #form #formTitle {
		font-size: 24px;
		margin-bottom: 25px;
	}
	#signinArea #form input {
		display: block;
		width: 75%;
		height: 20%;
		font-size: 20px;
		border: none;
		text-indent: 10px;
		border-radius: 10px;
		margin: 0 auto 10px auto;
		background-color: #181818;
	}
	#signinArea #form #formButtons {
		height: 25%;
		width: 75%;
		margin: auto;
		display: flex;
	}
	#signinArea #form #formButtons button {
		border: none;
		border-radius: 10px;
		margin: 0 10px;
		background-color: rgb(97, 97, 97);
		color: #afafaf;
		font-size: 18px;
		width: 50%;
		height: 70%;
		transform: translateY(30%);
		cursor: pointer;
	}
	#signinArea #form #formButtons button:hover {
		border-bottom: var(--HoverColor) 4px solid;
	}
</style>
