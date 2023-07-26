<script>
	import { json } from '@sveltejs/kit';
    import '../styles.css';
    import { onMount } from 'svelte';
    let draggedOver = false;
    let selectedFile;

    function onDragOver(event) {
        event.preventDefault();
        draggedOver = true;
    }

    function onDragLeave(event) {
        event.preventDefault();
        draggedOver = false;
    }

    async function onDrop(event) {
        event.preventDefault();
        draggedOver = false;
        if (event.dataTransfer.items && event.dataTransfer.items.length > 0) {
            selectedFile = event.dataTransfer.items[0].getAsFile();
            // Validate file type
            if (selectedFile && selectedFile.type === 'application/json') {
                await uploadFile();
            } else {
                console.error('Uploaded file is not a JSON file');
            }
        }
    }

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

    let users = [];

    async function userGET() {
        const responseUser = await fetch('http://localhost:5000/api');
        users = await responseUser.json();
    }

    async function downloadUsers() {
        await userGET();
        let json = JSON.stringify(users);
        let blob = new Blob([json], {type: "application/json"});
        let url  = URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url;
        a.download = "data.json";
        a.click();
    }

    async function uploadFile() {
        const reader = new FileReader();
        reader.onload = async () => {
            const contents = reader.result;
            try {
                const data = JSON.parse(contents);
                const response = await fetch('http://localhost:5000/api/reinitialize', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });

                // handle the response
            } catch (error) {
                console.error('The file does not contain valid JSON');
            }
        };

        reader.readAsText(selectedFile);
    }

</script>

<div class="input-wrapper">
    <button class="alert" on:click={deleteTable}>delete table</button>
    <button on:click={createTable}>create table</button>
    <button on:click={downloadUsers}>backup db</button>
    <div class="dropzone" on:dragover={onDragOver} on:dragleave={onDragLeave} on:drop={onDrop} class:dragging={draggedOver}>
        Drop JSON to restore
    </div>

</div>

<style>
    form {
        display: flex;
        flex-direction: column;
    }

    input {
        color: var(--color-theme-1);
        display: inline-block;
        outline: 0;
        border: 0;
        cursor: pointer;
        border-radius: 5px;
        height: 50px;
        font-size: 1rem;
        font-weight: 500;
        line-height: 1;
        opacity: 0.9;
        width: 11.7rem;
        margin-top: 5px;
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

    .alert {
        background: red;
        border: 3px solid red;
    }

    .dropzone {
        width: 11.8rem;
        height: 5rem;
        border: 2px dashed var(--color-theme-1);
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 5px;
        transition: background-color 0.3s ease;
    }

    .dropzone.dragging {
        background-color: lightgray;
    }
</style>

