<script>
	import basic_logo_rgb from '$lib/images/basic_logo_rgb.svg';
</script>

<header>
    <div>
        <a href="/">
        <img src={basic_logo_rgb} alt="logo">
        </a>
    </div>
</header>

<style>
    header {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 10vh;
    }

    div {
        width: 40vh;
    }

    img {
        width: 25rem;
        margin-top: 5rem;
    }
    
</style>