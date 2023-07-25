<script>
    import './styles.css';
    import { goto } from '$app/navigation';
</script>

<button on:click={() => goto('/form')}>Přidat distributora</button>

<style>
    button {
        position: fixed;
        right: 40px;
        bottom: 40px;
        background: var(--color-theme-1);
        color: var(--color-bg-1);
        display: inline-block;
        outline: 0;
        border: 0;
        cursor: pointer;
        border: 3px solid var(--color-theme-1);
        border-radius: 20px;
        font-size: 1.4rem;
        padding: 20px;
        font-weight: 700;
        line-height: 1;
        opacity: 0.9;
        z-index: 100;
        width: 18rem;
    }
</style>
