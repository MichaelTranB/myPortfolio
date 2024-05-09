//Typing Animation
document.addEventListener("DOMContentLoaded", function() {
    // Delay the start of the typing effect by 1000 milliseconds (1 second)
    setTimeout(function() {
        const lines = document.querySelectorAll(".typing-effect .line");
        let delay = 0;
        const typingDuration = 40; // Adjust for typing speed
        const cursorClass = 'active-cursor'; // Cursor class to toggle

        function typeLine(line, content, index) {
            let i = 0;
            function type() {
                if (i < content.length) {
                    line.textContent += content.charAt(i);
                    i++;
                    setTimeout(type, typingDuration);
                } else {
                    // Remove cursor from the current line
                    line.classList.remove(cursorClass);
                    // Only add cursor to the next line if not the last line; otherwise, re-add the cursor to the last line
                    if (index < lines.length - 1) {
                        lines[index + 1].classList.add(cursorClass);
                    } else {
                        // This ensures the cursor remains on the last line
                        line.classList.add(cursorClass);
                    }
                }
            }
            setTimeout(type, delay);
            delay += content.length * typingDuration + 500; // Adjust delay for the next line
        }

        // Initially add the cursor class to the first line
        if (lines.length > 0) {
            lines[0].classList.add(cursorClass);
        }

        lines.forEach((line, index) => {
            const content = line.getAttribute('data-content');
            line.textContent = ""; // Clear the line before typing
            typeLine(line, content, index);
        });
    }, 1000); // Delay before starting the typing effect
});



document.addEventListener("DOMContentLoaded", function() {
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top < window.innerHeight && rect.bottom >= 0 &&
            rect.right >= 0 && rect.left < window.innerWidth
        );
    }

    function activateAnimations() {
        document.querySelectorAll('.fade-in, .slide-in-left, .slide-in-right').forEach(element => {
            if (isElementInViewport(element) && !element.classList.contains('active')) {
                element.classList.add('active');
            }
        });
    }

    // Check animations on scroll, resize, and periodically to catch all changes
    window.addEventListener('scroll', activateAnimations);
    window.addEventListener('resize', activateAnimations);
    setInterval(activateAnimations, 1000); // Periodically ensure animations are triggered
    activateAnimations(); // Initial activation
});


document.addEventListener("DOMContentLoaded", function() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // Stop observing the element after it becomes active
            }
        });
    }, {
        rootMargin: '0px',
        threshold: 0.1  // Modify if needed to trigger animations sooner or later as elements come into view
    });

    // Add all elements that require the animation to the observer
    document.querySelectorAll('.fade-in, .slide-in-left, .slide-in-right').forEach(element => {
        observer.observe(element);
    });
});

