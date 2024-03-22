document.addEventListener("DOMContentLoaded", function() {
    const detailsSections = document.querySelectorAll('.experience-details');
    const firstDetails = detailsSections[0]; 

    // Initialize each details section to ensure no white space is present initially
    detailsSections.forEach(details => {
        details.style.maxHeight = '0';
        details.style.paddingTop = '0';
        details.style.paddingBottom = '0';
        details.style.visibility = 'hidden';
        details.style.marginTop = '0px'; // Ensure margins don't add extra space initially
        details.style.marginBottom = '0px';
    });

    // Immediately expand the first details section upon page load
    if (firstDetails) {
        expandSection(firstDetails, true);
    }

    document.querySelectorAll('.experience-card-header').forEach(header => {
        header.addEventListener('click', function() {
            const clickedDetails = this.nextElementSibling;
            toggleSection(clickedDetails);
        });
    });

    function expandSection(section, expand) {
        const icon = section.previousElementSibling.querySelector('.toggle-experience i');
        if (expand) {
            section.style.visibility = 'visible';
            section.style.maxHeight = section.scrollHeight + 50 + "px";
            section.style.paddingTop = '20px';
            section.style.paddingBottom = '20px';
            section.style.marginTop = '4px';
            section.style.marginBottom = '1px';
            icon.classList.replace('fa-plus', 'fa-minus');
            adjustHeaderColor(section.previousElementSibling, true);
        }
    }

    function toggleSection(section) {
        const isCollapsed = section.style.maxHeight === '0px';
        const icon = section.previousElementSibling.querySelector('.toggle-experience i');

        // Collapse any other expanded details
        detailsSections.forEach(details => {
            if (details !== section && details.style.maxHeight !== '0px') {
                details.style.maxHeight = '0px';
                details.style.paddingTop = '0';
                details.style.paddingBottom = '0';
                details.addEventListener('transitionend', function handleTransitionEnd() {
                    details.style.visibility = 'hidden';
                    details.style.marginTop = '0px';
                    details.style.marginBottom = '0px';
                    details.removeEventListener('transitionend', handleTransitionEnd);
                }, { once: true });
                adjustHeaderColor(details.previousElementSibling, false);
                const otherIcon = details.previousElementSibling.querySelector('.toggle-experience i');
                otherIcon.classList.replace('fa-minus', 'fa-plus');
            }
        });

        // Expand the clicked section if it was collapsed
        if (isCollapsed) {
            section.style.visibility = 'visible';
            section.style.maxHeight = section.scrollHeight + 50 + "px";
            section.style.paddingTop = '20px';
            section.style.paddingBottom = '20px';
            section.style.marginTop = '4px';
            section.style.marginBottom = '1px';
            icon.classList.replace('fa-plus', 'fa-minus');
        } else {
            section.style.maxHeight = '0';
            section.style.paddingTop = '0';
            section.style.paddingBottom = '0';
            section.addEventListener('transitionend', function handleTransitionEnd() {
                section.style.visibility = 'hidden';
                section.style.marginTop = '0px';
                section.style.marginBottom = '0px';
                section.removeEventListener('transitionend', handleTransitionEnd);
            }, { once: true });
            icon.classList.replace('fa-minus', 'fa-plus');
        }
        adjustHeaderColor(section.previousElementSibling, isCollapsed);
    }

    function adjustHeaderColor(header, expanded) {
        const isDarkMode = document.body.classList.contains('dark-mode');
        header.style.backgroundColor = expanded ? (isDarkMode ? '#740cdc' : '#740cdc') : (isDarkMode ? '#430d79' : '#430d79');
    }
});
