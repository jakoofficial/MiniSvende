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
			if (user.sub == true) {
				premium = true;
			}
            else {
				premium = false;
            }
		} else {
			loggedin = false;
		}
	});
</script>

<div class="pageContents">
	<div id="subOptions">
		<div class="panel">
			{#if loggedin && premium == false}
				<div id="banner">
					<p>Owned</p>
				</div>
			{/if}
			<div>
				<p class="subTitle">Free tier</p>
				<hr />
				<div id="info">
					<p id="desc">
						Enjoy movies from our free selection and get absorbed into the movie of your choice.
					</p>
                    <div id="benefits">
                        <p>Benefits</p>
                        <p>Unlimited watchings<br>
                            Free movies with #tag<br>
                            No ads</p>
                    </div>
					<p id="price">Free</p>
				</div>
			</div>
            {#if loggedin}
			<button id="{premium == true ? '' : 'inactive'}">{premium == true ? "Downgrade tier" : 'Active'}</button>
            {/if}
		</div>
		<div class="panel">
			{#if loggedin && premium == true}
				<div id="banner">
					<p>Owned</p>
				</div>
			{/if}
			<div>
				<p class="subTitle">Premium</p>
				<hr />
				<div id="info">
					<p id="desc">
						Enjoy movies from our large selection and let yourself get absorbed into the movie of
						your choice.
					</p>
                    <div id="benefits">
                        <p>Benefits</p>
                        <p>Unlimited watchings.<br>
                        All movies in our selection.<br>
                        No ads.</p>
                    </div>
					<p id="price">9.99€ <span>/mo</span></p>
				</div>
			</div>
            {#if loggedin}
    			<button id="{premium == false ? '' : 'inactive'}">{premium == false ? "Upgrade tier" : 'Active'}</button>
            {/if}
		</div>
	</div>
</div>

<!-- Styleing for the page -->
<style>
    
	#banner {
		background-color: rgb(129, 73, 69);
		position: absolute;
		top: 0;
		right: 0; /* Stick to the top-right corner of the panel */
		/* clip-path: polygon(17% 0, 22% 0, 22% 15%, 17% 22%); */
		clip-path: polygon(77% 0, 95% 0, 95% 30%, 77% 20%);
		width: 100%; /* Adjust as needed */
		height: 50%; /* Adjust as needed */
		z-index: 10;
	}
	#banner p {
		z-index: inherit;
		float: inline-end;
		transform: translateX(-30%) translateY(50%);
		color: rgb(194, 194, 194);
		font-weight: bold;
		text-decoration: underline;
	}
	.pageContents {
		height: 85vh;
		transform: translateY(3%);
		/* align-content: center; */
	}
	#subOptions {
		height: 65%;
		width: 75%;
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
		position: relative; /* Add this */
	}

	.panel div {
		display: block;
		border-radius: 25px 25px 0 0;
		width: 100%;
		height: 90%;
		padding: 0px 15px 0px 15px;
	}

	.panel div .subTitle {
		font-size: 26px;
		padding-left: 0px;
        margin-top: 10px;
        color: black;
		transform: translateX(10px);
	}
    .panel div #info {
        padding: 0%;
    }
    .panel div #info #desc {
        font-size: 18px;
        color: black;
        height: 35%;
        margin-top: 20px;
        text-align: center;
    }
    .panel div #info #benefits{
        border-radius: 0%;
        padding: 0%;
        height: 45%;
    }
    .panel div #info #benefits p:first-of-type{
        text-align: center;
        color: black;
        font-size: 24px;
        font-weight: bold;
    }
    .panel div #info #benefits p:last-of-type{
        text-align: center;
        color: black;
        font-size: 20px;
    }
    .panel div #info #price {
        color: black;
        font-size: 24px;
        height: 15%;
        align-content: center;
        text-align: center;
        font-weight: 600;
    }
    .panel div #info #price span {
        color: black;
        font-size: 18px;
    }

    .panel #inactive{
		border-radius: 0 0 24px 24px;
		cursor: default;
		background-color: rgb(37, 37, 37);
    }
    .panel #inactive:hover{
        border:none;
    }

	.panel button {
		width: 100%;
		height: 10%;
		font-size: 18px;
		color: rgb(194, 194, 194);
		border: none;
		border-radius: 0 0 24px 24px;
		background-color: rgb(78, 78, 78);
		cursor: pointer;
	}
	.panel button:hover {
		border-bottom: var(--HoverColor) 4px solid;
	}
</style>
