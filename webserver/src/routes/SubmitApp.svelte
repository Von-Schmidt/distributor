<script>
    import './styles.css';
    import { goto } from '$app/navigation';

    let name = "";
    let email = "";
    let username = "";
    let company = "";

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

        goto('/');
    }
    
</script>

<div class="input-wrapper">
    <input type="text" placeholder="Celé jméno" bind:value={name}>
    <input type="text" placeholder="Kontaktní email" bind:value={email}>
    <input type="text" placeholder="Username" bind:value={username}>
    <input type="text" placeholder="Společnost" bind:value={company}>
    <input type="submit" value="Přidat" on:click={userPOST}>
</div>

<style>
    input {
        margin-top: 0.1rem;
    }

    input[type=text] {
        border: 3px solid var(--color-theme-1);
        border-radius: 5px;
        height: 50px;
        line-height: normal;
        color: var(--color-theme-3);
        display: block;
        width: 100%;
        box-sizing: border-box;
        user-select: auto;
        font-size: 16px;
        padding: 0 6px;
        padding-left: 12px;
    }

    input[type="submit"] {
        background: var(--color-theme-1);
        color: var(--color-theme-4);
        display: inline-block;
        outline: 0;
        border: 0;
        cursor: pointer;
        border: 3px solid var(--color-theme-1);
        border-radius: 5px;
        height: 50px;
        font-size: 18px;
        font-weight: 700;
        line-height: 1;
        opacity: 0.9;
    }

    input:focus {
        border: 3px solid var(--color-theme-3);
        outline: none;
    }

    input[type="submit"]:hover {
        opacity:1;
    }

    .input-wrapper {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border: 3px solid var(--color-theme-1);
        border-radius: 15px;
        padding: 2rem;
        background-color: var(--color-theme-4);
        box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22);
    }
    
</style>

