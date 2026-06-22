<script>
	import {Post, SetSessionToken, GetSessionToken} from "$lib/DataFetcher";
	import { onMount } from 'svelte';

    let username = "";
    let password = "";

    // Use the props from `load`
    let ses = "";
    let loggedin = $state(false);
	// $: if (loggedin != false){console.log("asd")}

	onMount(async () => {
		ses = GetSessionToken()
		if (ses) {
			
			console.log(ses)
			loggedin = true
		}
		else {
			loggedin = false
		}
	})
	async function Signin() {
		const data = await Post('signin',{
			'username': username,
			'password': password
		});
		console.log(data)
		SetSessionToken(data[1].session_key)
		loggedin = true
		window.location.reload(true)
	}
	async function Signup() {
		const data = await Post('createUser',{
			'username': username,
			'password': password
		});
		console.log(data)
	}

</script>

<div class="pageContents">
	{#if loggedin}
		<div id="profile"></div>
	{:else}
		<div id="signinArea">
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
	{/if}
</div>

<!-- Styleing for the page -->
<style>
	.pageContents {
		display: block;
		height: 90vh;
		align-content: center;
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

