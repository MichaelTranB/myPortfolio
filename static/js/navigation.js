document.addEventListener("DOMContentLoaded", function() {
    console.log("Document is ready.");

    function updateBodyPadding() {
        const navbarHeight = document.getElementById('navbar').offsetHeight;
        const isMobileView = window.innerWidth < 640;
        const additionalPadding = isMobileView ? 20 : 10;
        document.body.style.paddingTop = `${navbarHeight + additionalPadding}px`;
        console.log("Body padding updated:", document.body.style.paddingTop);
    }

    updateBodyPadding();
    window.addEventListener('resize', function() {
        updateBodyPadding();
    });

    document.querySelectorAll('a.nav-link, #mobile-menu a').forEach(link => {
        link.addEventListener('click', function(e) {
            let href = this.getAttribute('href');
            console.log("Link clicked:", href);
            if (href.startsWith('/#')) { // Correcting for full path in href
                href = href.substring(1); // Remove the leading slash
            }
            if (href.startsWith('#')) {
                e.preventDefault();
                const targetId = href.substring(1); // Get the ID without the hash
                const targetElement = document.getElementById(targetId);
                console.log("Target element:", targetElement);
                if (targetElement) {
                    console.log(`Attempting to scroll to ${targetId} at position ${targetElement.offsetTop}`);
                    // Alternative method for smooth scrolling
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    if (menuToggle && mobileMenu) {
        menuToggle.addEventListener('click', function() {
            mobileMenu.style.display = (mobileMenu.style.display === "block" ? "none" : "block");
            console.log("Mobile menu toggled:", mobileMenu.style.display);
        });
    }
});
