document.addEventListener("DOMContentLoaded", function() {
    const detailsSections = document.querySelectorAll('.experience-details');
    const firstDetails = detailsSections[0]; 

    // Initialize each details section to ensure no white space is present initially
    document.querySelectorAll('.experience-details').forEach(details => {
        details.style.maxHeight = '0';
        details.style.paddingTop = '0';
        details.style.paddingBottom = '0';
        details.style.visibility = 'hidden';
        details.style.marginTop = '0px'; // Ensure margins don't add extra space initially
        details.style.marginBottom = '0px';
    });

     // Immediately expand the first details section upon page load
     if (firstDetails) {
        firstDetails.style.visibility = 'visible';
        firstDetails.style.maxHeight = firstDetails.scrollHeight + 50 + "px"; // Adding 50px buffer
        firstDetails.style.paddingTop = '20px';
        firstDetails.style.paddingBottom = '20px';
        firstDetails.style.marginTop = '4px';
        firstDetails.style.marginBottom = '1px';
        // Update the icon of the first header
        const firstIcon = firstDetails.previousElementSibling.querySelector('.toggle-experience i');
        if (firstIcon) {
            firstIcon.classList.remove('fa-plus');
            firstIcon.classList.add('fa-minus');
        }
    }

    document.querySelectorAll('.experience-card-header').forEach(header => {
        header.addEventListener('click', function() {
            const clickedDetails = this.nextElementSibling;

            // Collapse any other expanded details
            detailsSections.forEach(details => {
                if (details !== clickedDetails && details.style.maxHeight !== '0px') {
                    details.style.maxHeight = '0px';
                    details.style.paddingTop = '0';
                    details.style.paddingBottom = '0';
                    details.addEventListener('transitionend', () => {
                        if (details.style.maxHeight === '0px') {
                            details.style.visibility = 'hidden';
                            details.style.marginTop = '0px';
                            details.style.marginBottom = '0px';
                        }
                    }, { once: true });

                    // Update the icon of any other expanded headers
                    const icon = details.previousElementSibling.querySelector('.toggle-experience i');
                    if (icon) {
                        icon.classList.remove('fa-minus');
                        icon.classList.add('fa-plus');
                    }
                }
            });

            // Then proceed to toggle the clicked details visibility
            const isCollapsed = clickedDetails.style.maxHeight === '0px' || clickedDetails.style.maxHeight === '';

            if (isCollapsed) {
                this.style.backgroundColor = '#740cdc';
                clickedDetails.style.visibility = 'visible';
                clickedDetails.style.maxHeight = 'none';
                const fullHeight = clickedDetails.scrollHeight + 50 + "px"; // Adding buffer
                clickedDetails.style.maxHeight = '0px';

                requestAnimationFrame(() => {
                    clickedDetails.style.maxHeight = fullHeight;
                    clickedDetails.style.paddingTop = '20px';
                    clickedDetails.style.paddingBottom = '20px';
                    clickedDetails.style.marginTop = '4px';
                    clickedDetails.style.marginBottom = '1px';
                });
            } else {
                this.style.backgroundColor = '#6d28d9';
                clickedDetails.style.maxHeight = '0px';
                clickedDetails.style.paddingTop = '0';
                clickedDetails.style.paddingBottom = '0';
                clickedDetails.addEventListener('transitionend', () => {
                    if (clickedDetails.style.maxHeight === '0px') {
                        clickedDetails.style.visibility = 'hidden';
                        clickedDetails.style.marginTop = '0px';
                        clickedDetails.style.marginBottom = '0px';
                    }
                }, { once: true });
            }

            // Toggle the icon for the clicked header
            const icon = this.querySelector('.toggle-experience i');
            icon.classList.toggle('fa-plus');
            icon.classList.toggle('fa-minus');
        });
    });
});
