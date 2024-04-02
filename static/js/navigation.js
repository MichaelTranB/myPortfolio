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
    window.addEventListener('resize', debounce(updateBodyPadding, 100)); // Using debounce here

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
        }, { passive: true }); // Added passive here
    }

    // Smooth scrolling for all navigation links
    document.querySelectorAll('a.nav-link, #mobile-menu a').forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href').split('#')[1];
            
            if (window.location.pathname === '/' || window.location.pathname.endsWith('main_page.html')) {
                e.preventDefault();
                
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    document.getElementById('mobile-menu').style.display = 'none';
                    const navbarHeight = document.getElementById('navbar').offsetHeight;
                    const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navbarHeight;
                    window.scrollTo({ top: targetPosition, behavior: 'smooth' });
                }
            } else {
                window.location.href = '/' + '#' + targetId; // No change needed here
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
