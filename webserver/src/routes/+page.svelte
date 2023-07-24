<script>
    import SubmitApp from './SubmitApp.svelte';
    import GetApp from './GetApp.svelte';
</script>

<svelte:head>
    <title>DISTRIBUTOR</title>
    <meta name="description" content="Management distributorů" />
</svelte:head>

<section>
    <SubmitApp />
    <GetApp />
</section>

<style>
    section {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        flex: 0.4;
    }
</style>