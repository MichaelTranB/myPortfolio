document.addEventListener('DOMContentLoaded', () => {
    // Set the initial mode based on localStorage or default to dark-mode
    const savedMode = localStorage.getItem('mode') || 'dark-mode';
    document.body.classList.toggle('dark-mode', savedMode === 'dark-mode');
    document.getElementById('mode-switcher').checked = savedMode === 'dark-mode';

    document.getElementById('mode-switcher').addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        localStorage.setItem('mode', document.body.classList.contains('dark-mode') ? 'dark-mode' : 'light-mode');
    });
});