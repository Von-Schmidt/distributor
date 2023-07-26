<script>
    import AdminTable from "./AdminTable.svelte";
    import AdminPanel from "./AdminPanel.svelte";
</script>

<svelte:head>
    <title>DISTRIBUTOR</title>
    <meta name="description" content="Management distributorů" />
</svelte:head>

<section>
    <AdminPanel />
    <AdminTable />
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