<script>
    import '../styles.css';

    async function deleteTable() {
        const response = await fetch(`http://localhost:5000/api/table`, {
            method: 'DELETE',
        });
        const data = await response.json();
        console.log(data.result);
    }

    async function createTable() {
        const response = await fetch(`http://localhost:5000/api/table`, {
            method: 'POST',
        });
        const data = await response.json();
        console.log(data.result);
    }

</script>

<div class="input-wrapper">
    <button on:click={deleteTable}>delete table</button>
    <button on:click={createTable}>create table</button>
</div>

<style>
    input {
        margin-top: 0.1rem;
    }

    button {
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
        width: 12rem;
        margin-top: 5px;
    }

    button:hover {
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

