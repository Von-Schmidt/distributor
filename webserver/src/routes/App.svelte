<script>
    import './styles.css';

    let name = "";
    let email = "";
    let username = "";
    let company = "";
    let yesno = 1;


    async function callAPI() {
        const response = await fetch('http://localhost:5000/api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            string_input1: username,
            string_input2: email,
            string_input3: yesno
        })
        });

        let user = {
            name,
            username,
            email,
            company
        };
        
        fetch('http://localhost:5173/api/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(user),
        })
        .then(response => response.json())
        .then(data => console.log(data));
    }

    async function test() {
        fetch('http://localhost:5173/api/users', {
            method: 'GET',
        })
    .then(response => response.json())
    .then(data => console.log(data.users));
    }
</script>

<input type="text" placeholder="Jméno" bind:value={name}>
<input type="text" placeholder="email" bind:value={email}>
<input type="text" placeholder="username" bind:value={username}>
<input type="text" placeholder="company" bind:value={company}>

<input type="submit" value="submit" on:click={callAPI}>
<button on:click={test}>test</button>