document.addEventListener("DOMContentLoaded", function() {
    function debounce(func, wait) {
        let timeout;
        return function() {
            const context = this, args = arguments;
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(context, args), wait);
        };
    }

    function updateBodyPadding() {
        const navbarHeight = document.getElementById('navbar').offsetHeight;
        const isMobileView = window.innerWidth < 640;
        const additionalPadding = isMobileView ? 20 : 10;
        document.body.style.paddingTop = `${navbarHeight + additionalPadding}px`;
    }

    updateBodyPadding();
    window.addEventListener('resize', debounce(updateBodyPadding, 100));

    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    // Smooth scrolling for all navigation links
    document.querySelectorAll('a.nav-link, #mobile-menu a').forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href.startsWith('#')) {
                e.preventDefault();
                const targetId = href.split('#')[1];
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    // Force visibility and position adjustments if necessary
                    targetElement.classList.add('active'); // Ensure it is visible
                    window.scrollTo({
                        top: targetElement.offsetTop - document.getElementById('navbar').offsetHeight,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // Toggle the mobile menu
    document.getElementById('menu-toggle').addEventListener('click', function() {
        var mobileMenu = document.getElementById('mobile-menu');
        if (mobileMenu.style.display === "block") {
            mobileMenu.style.display = "none";
        } else {
            mobileMenu.style.display = "block";
        }
    });

    // Checks animations and makes sure they are triggered as expected
    function checkAnimations() {
        document.querySelectorAll('.fade-in, .slide-in-left, .slide-in-right').forEach(element => {
            if (isElementInViewport(element)) {
                element.classList.add('active', 'animated');
            } else if (!element.classList.contains('animated')) {
                element.classList.remove('active');
            }
        });
    }

    window.addEventListener('scroll', checkAnimations, { passive: true });
    checkAnimations();

    // Home Link Smooth Scroll to Top
    const homeLink = document.getElementById('home-link');
    if (homeLink) {
        homeLink.addEventListener('click', function(e) {
            e.preventDefault();
            if (window.location.pathname !== '/') {
                window.location.href = '/';
            } else {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            }
        });
    }
});
