document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.experience-card-header').forEach(header => {
        header.addEventListener('click', function() {
            const details = this.nextElementSibling;

            // Check if the details are currently visible
            const isVisible = details.style.maxHeight && details.style.maxHeight !== '0px';

            if (!isVisible) {
                details.classList.remove('hidden'); // Make sure the element is not marked as hidden
                details.style.maxHeight = '0px'; // Reset max height in case it was set to none
                setTimeout(() => {
                    details.style.maxHeight = `${details.scrollHeight}px`;
                    details.style.paddingTop = '20px'; // Restore vertical padding
                    details.style.paddingBottom = '20px'; // Restore vertical padding
                }, 10); // Short delay to ensure the transition plays
            } else {
                details.style.maxHeight = '0px';
                details.style.paddingTop = '0'; // Remove vertical padding
                details.style.paddingBottom = '0'; // Remove vertical padding
                details.addEventListener('transitionend', () => {
                    if (details.style.maxHeight === '0px') {
                        details.classList.add('hidden'); // Hide after transition completes
                    }
                }, { once: true });
            }

            const icon = this.querySelector('.toggle-experience i');
            icon.classList.toggle('fa-plus');
            icon.classList.toggle('fa-minus');
        });
    });
});
