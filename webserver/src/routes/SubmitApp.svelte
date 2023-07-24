<script>
    import './styles.css';
    import { onMount } from 'svelte';

    let name = "";
    let email = "";
    let username = "";
    let company = "";
    let yesno = 1;

    async function userPOST() {
        const response = await fetch('http://localhost:5000/api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            string_input1: name,
            string_input2: email,
            string_input3: username,
            string_input4: company
        })
        });
    }

</script>

<input type="text" placeholder="Jméno" bind:value={name}>
<input type="text" placeholder="email" bind:value={email}>
<input type="text" placeholder="username" bind:value={username}>
<input type="text" placeholder="company" bind:value={company}>

<input type="submit" value="submit" on:click={userPOST}>
