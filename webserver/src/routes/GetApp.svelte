<script>
    import './styles.css';
    import { onMount } from 'svelte';

    let users = "";

    async function userGET() {
        const responseUser = await fetch('http://localhost:5000/api');
        users = await responseUser.json();
    }

    onMount(() => {
        userGET();
    })
    
</script>

<h1>{users}</h1>