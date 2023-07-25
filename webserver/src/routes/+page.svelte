<script>
    import GetApp from './GetApp.svelte';
    import AddButton from './AddButton.svelte';
	import HelpButton from './HelpButton.svelte';
</script>

<svelte:head>
    <title>DISTRIBUTOR</title>
    <meta name="description" content="Management distributorů" />
</svelte:head>

<section>
    <GetApp />
    <AddButton />
    <HelpButton />
</section>

<style>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        flex: 0.4;
    }
</style>