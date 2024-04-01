document.addEventListener("DOMContentLoaded", function() {
    function updateBodyPadding() {
        const navbarHeight = document.getElementById('navbar').offsetHeight;
        const isMobileView = window.innerWidth < 640;
        const additionalPadding = isMobileView ? 20 : 10;
        document.body.style.paddingTop = `${navbarHeight + additionalPadding}px`;
    }

    updateBodyPadding();
    window.addEventListener('resize', updateBodyPadding);

    // Scroll To Top Button Logic
    const scrollToTopButton = document.getElementById('scrollToTop');
    if (scrollToTopButton) {
        scrollToTopButton.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 200) {
                scrollToTopButton.style.display = 'block';
            } else {
                scrollToTopButton.style.display = 'none';
            }
        });
    }

    // Smooth scrolling for all navigation links
    document.querySelectorAll('a.nav-link, #mobile-menu a').forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href').split('#')[1];
            
            // Check if we're already on the main page or another page
            if (window.location.pathname === '/' || window.location.pathname.endsWith('main_page.html')) {
                // Prevent default if we are on the main page to handle smooth scroll
                e.preventDefault();
                
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    document.getElementById('mobile-menu').style.display = 'none';
                    const navbarHeight = document.getElementById('navbar').offsetHeight;
                    const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navbarHeight;
                    window.scrollTo({ top: targetPosition, behavior: 'smooth' });
                }
            } else {
                // If we're not on the main page, redirect and append the hash to URL
                // This will not prevent the default action, allowing the link to work naturally
                window.location.href = '/' + '#'+ targetId; // Adjust the path as necessary
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

    // Animation Visibility Check
    function checkAnimations() {
        document.querySelectorAll('.fade-in, .slide-in-left, .slide-in-right').forEach(element => {
            if (isElementInViewport(element)) {
                element.classList.add('active', 'animated');
            } else if (!element.classList.contains('animated')) {
                element.classList.remove('active');
            }
        });
    }

    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top <= (window.innerHeight || document.documentElement.clientHeight) + 100 &&
            rect.bottom >= 0
        );
    }

    window.addEventListener('scroll', checkAnimations);
    checkAnimations();

    // Home Link Smooth Scroll to Top
    const homeLink = document.getElementById('home-link');
    if (homeLink) {
        homeLink.addEventListener('click', function(e) {
            e.preventDefault();
            if(window.location.pathname !== '/') {
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
