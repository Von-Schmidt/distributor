<script>
    import { goto } from '$app/navigation';
    import './styles.css';
    import { onMount } from 'svelte';
    import IoIosPaperPlane from 'svelte-icons/io/IoIosPaperPlane.svelte'
    import IoIosCloseCircleOutline from 'svelte-icons/io/IoIosCloseCircleOutline.svelte'

    let users = [];

    async function userGET() {
        const responseUser = await fetch('http://localhost:5000/api');
        users = await responseUser.json();
    }

    async function deleteUser(username) {
        const response = await fetch(`http://localhost:5000/api/${username}`, {
            method: 'DELETE',
        });
        const data = await response.json();
        console.log(data.result);
        await userGET();
    }


    onMount(() => {
        userGET();
    })
    
</script>


<table>
    <thead>
    <tr>
        <th>Company</th>
        <th>Email</th>
        <th>Name</th>
        <th>Username</th>
        <th>Delete</th>
        <th>Reset</th>
    </tr>
    </thead>
    <tbody>
    {#each users as row (row.email)}
        <tr>
        <td>{row.company}</td>
        <td>{row.email}</td>
        <td>{row.name}</td>
        <td>{row.username}</td>
        <td><button on:click={() => deleteUser(row.username)}>
            <div class="icon">
                <IoIosCloseCircleOutline />
            </div>
        </button></td>
        <td><button on:click={() => goto('/admin')}>
            <div class="icon">
                <IoIosPaperPlane />
            </div>
        </button></td>
        </tr>
    {/each}
    </tbody>
</table>
  
<style>
    table {
        border-collapse: collapse;
        width: 80%;
        color: #333;
        font-family: Arial, sans-serif;
        font-size: 14px;
        text-align: left;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22);
        margin: auto;
        margin-top: 50px;
        margin-bottom: 50px;
    }

    table th {
        background-color: var(--color-theme-1);
        color: #fff;
        font-weight: bold;
        padding: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    table tr:nth-child(even) td {
        background-color: var(--color-theme-4);
    }

    table tr:hover td {
        background-color: var(--color-theme-2);
    }

    table td {
        background-color: var(--color-bg-1);
        padding: 10px;
        border-bottom: 1px solid #ccc;
        font-weight: bold;
    }

    table button {
        background: transparent;
        display: inline-block;
        outline: 0;
        border: 0;
        cursor: pointer;
        border-radius: 5px;
        font-size: 1.4rem;
        padding: 5px;
        font-weight: 700;
        line-height: 1;
        opacity: 0.9;
    }

    table button:hover {
        opacity: 1;
    }

    .icon {
        color: var(--color-theme-1);
        width: 32px;
        height: 32px;
    }
    
</style>