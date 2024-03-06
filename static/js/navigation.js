//Navbar
document.addEventListener("DOMContentLoaded", function() {
    function updateBodyPadding() {
        const navbarHeight = document.getElementById('navbar').offsetHeight;
        const isMobileView = window.innerWidth < 640; 
        const additionalPadding = isMobileView ? 20 : 10; 
        document.body.style.paddingTop = `${navbarHeight + additionalPadding}px`;
    }

    updateBodyPadding();

    window.addEventListener('resize', updateBodyPadding);
});


//Scroll To Top
document.addEventListener("DOMContentLoaded", function() {
    const scrollToTopButton = document.getElementById('scrollToTop');
    scrollToTopButton.addEventListener('click', function(e) {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Toggle visibility of Scroll to Top button based on scroll position
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 200) {
            scrollToTopButton.style.display = 'block';
        } else {
            scrollToTopButton.style.display = 'none';
        }
    });

    // Smooth scrolling for navigation links using native JavaScript
    document.querySelectorAll('a.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault(); // Prevent the default anchor behavior

            const targetId = this.getAttribute('href').replace("/", ""); // Get the target ID
            const targetElement = document.querySelector(targetId); // Select the target element

            if (targetElement) {
                // Calculate the target position, accounting for the navbar height
                const navbarHeight = document.getElementById('navbar').offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navbarHeight - 20;

                // Smooth scroll to the target position
                window.scrollTo({ top: targetPosition, behavior: 'smooth' });
            }
        });
    });

    

    $('#menu-toggle').click(function() {
        $('#mobile-menu').toggle();
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

    window.addEventListener('scroll', checkAnimations);
    checkAnimations(); 

    document.getElementById('home-link').addEventListener('click', function(e) {
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
});