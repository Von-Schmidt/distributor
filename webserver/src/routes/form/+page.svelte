<script>
    import BackButton from '../BackButton.svelte';
	import HelpButton from '../HelpButton.svelte';
    import SubmitApp from '../SubmitApp.svelte';
</script>

<svelte:head>
    <title>DISTRIBUTOR</title>
    <meta name="description" content="Management distributorů" />
</svelte:head>

<section>
    <SubmitApp />
    <BackButton />
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