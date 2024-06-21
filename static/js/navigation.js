document.addEventListener("DOMContentLoaded", function() {

    const menuToggle = document.getElementById('menu-toggle'); // This should be the ID of your hamburger menu button
    const mobileMenu = document.getElementById('mobile-menu'); // This should be the ID of your mobile menu

    if (menuToggle && mobileMenu) {
        menuToggle.addEventListener('click', function() {
            // Toggle the display property
            mobileMenu.style.display = (mobileMenu.style.display === "block" ? "none" : "block");
        });
    }
    
    function updateBodyPadding() {
        const navbarHeight = document.getElementById('navbar').offsetHeight;
        const isMobileView = window.innerWidth < 640;
        const additionalPadding = isMobileView ? 20 : 10;
        document.body.style.paddingTop = `${navbarHeight + additionalPadding}px`;
    }

    updateBodyPadding();
    window.addEventListener('resize', updateBodyPadding);

    document.querySelectorAll('a.nav-link, #mobile-menu a').forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            console.log("Link clicked:", href);
            if (href.startsWith('#')) {
                e.preventDefault(); // prevent default anchor behavior
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        });
    });

    // Ensure smooth scrolling on page load if a hash is present
    if (window.location.hash) {
        setTimeout(() => {
            const targetElement = document.getElementById(window.location.hash.substring(1));
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }, 100); // Delay to ensure all page elements are loaded
    }
});
