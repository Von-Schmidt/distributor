<script>
    import './styles.css';
    import DiAptana from 'svelte-icons/di/DiAptana.svelte'
    import { goto } from '$app/navigation';
</script>

<button on:click={() => goto('/admin')}>
    <div class="icon">
        <DiAptana />
    </div>
</button>

<style>
    button {
        position: fixed;
        left: 40px;
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
        
    }

    .icon {
        color: var(--color-bg-1);
        width: 32px;
        height: 32px;
    }
</style>
