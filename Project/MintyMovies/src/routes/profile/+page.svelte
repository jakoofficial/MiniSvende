<script>
</script>

<div class="pageContents">
	<div id="signinArea">
		<div id="form">
			<p id="formTitle">Sign in</p>
			<input type="text" placeholder="Username" />
			<input type="password" placeholder="Password" />
			<div id="formButtons">
				<button> Register </button>
				<button> Sign in </button>
			</div>
		</div>
	</div>
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
