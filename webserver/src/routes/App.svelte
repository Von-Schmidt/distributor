<script>
    import './styles.css';

    let name = "";
    let email = "";
    let yesno;

    async function callAPI() {
        const response = await fetch('http://localhost:5000/api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            string_input1: name,
            string_input2: email,
            string_input3: yesno
        })
        });
    }
</script>

<input type="text" placeholder="username" bind:value={name}>
<input type="text" placeholder="email" bind:value={email}>
<input type="text" placeholder="yesno" bind:value={yesno}>

<input type="submit" value="submit" on:click={callAPI}>