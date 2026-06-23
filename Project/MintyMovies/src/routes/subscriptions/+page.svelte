<script>
	import { Post, SetSessionToken, GetSessionToken, Get } from '$lib/DataFetcher';
	import { onMount } from 'svelte';

	let ses = '';
	let loggedin = $state(false);
	let user;
    let premium = false;

	onMount(async () => {
		ses = GetSessionToken();
		if (ses) {
			user = await Get('getUserBySession', { 'session-token': ses });
			loggedin = true;
            if (user.sub == true){premium = true}
		} else {
			loggedin = false;
		}
	});
</script>

<div class="pageContents">
	<div id="subOptions">
		<div class="panel">
        {#if loggedin && premium == false}
            <div id="banner"></div>
        {/if}
			<div>
                <p class="subTitle">Free</p>
                <hr>
                <p>hello</p>
            </div>
			<button>Choose this tier</button>
		</div>
        <div class="panel">
        {#if loggedin && premium == true}
            <div id="banner"></div>
        {/if}
			<div>
                <p class="subTitle">Premium</p>
            </div>
			<button>Choose this tier</button>
		</div>
	</div>
</div>

<!-- Styleing for the page -->
<style>

    #banner{
        background-color: aqua;
        position:fixed;
        clip-path: polygon(17% 0, 22% 0, 22% 15%, 17% 22%);
    }
	.pageContents {
		height: 85vh;
		transform: translateY(3%);
		/* align-content: center; */
	}
	#subOptions {
		height: 65%;
		width: 100%;
		margin: auto;
		justify-content: center;
		transform: translateY(10%);
		display: flex;
		gap: 2%;
	}
	.panel {
		background-color: #afafaf;
		width: 25%;
		height: 90%;
		border-radius: 25px;
		align-self: center;
		display: inline-flex;
		flex-wrap: wrap;
	}
	.panel div {
		display: block;
		border-radius: 25px 25px 0 0;
		width: 100%;
		height: 90%;
        padding: 0px 15px 0px 15px;
	}
    .panel div p {
        margin-top: 10px;
        font-size: 18px;
        color: black;
        padding-left: 10px;
        padding-right: 10px;
    }
    .panel div hr {
    }
    .panel div .subTitle {
        font-size: 26px;
        padding-left: 0px;
        transform: translateX(10px);
    }
	.panel button {
		width: 100%;
		height: 10%;
        font-size: 18px;
        color: rgb(194, 194, 194);
		border: none;
		border-radius: 0 0 25px 25px;
		background-color: rgb(78, 78, 78);
        cursor: pointer;
	}
    .panel button:hover{
        border-bottom: var(--HoverColor) 4px solid;
    }
</style>
