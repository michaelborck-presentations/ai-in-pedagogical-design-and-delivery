// Inject header and footer components into pages
document.addEventListener('DOMContentLoaded', function() {
    // Inject header
    const headerDiv = document.getElementById('header');
    if (headerDiv) {
        fetch('header.html')
            .then(response => response.text())
            .then(html => {
                headerDiv.innerHTML = html;
                setActiveNavLink();
            })
            .catch(error => console.error('Error loading header:', error));
    }

    // Inject footer
    const footerDiv = document.getElementById('footer');
    if (footerDiv) {
        fetch('footer.html')
            .then(response => response.text())
            .then(html => {
                footerDiv.innerHTML = html;
            })
            .catch(error => console.error('Error loading footer:', error));
    }
});

// Set active navigation link based on current page
function setActiveNavLink() {
    const currentPath = window.location.pathname;
    const currentPage = currentPath.substring(currentPath.lastIndexOf('/') + 1) || 'index.html';

    // Remove active class from all nav links
    document.querySelectorAll('nav a').forEach(link => {
        link.classList.remove('active');
    });

    // Add active class to current page link
    document.querySelectorAll('nav a').forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPage || (currentPage === '' && href === 'index.html')) {
            link.classList.add('active');
        }
    });
}
