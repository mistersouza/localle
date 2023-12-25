// Remove alert messages after 5 seconds
setTimeout(function() {
    var messages = document.querySelectorAll('.alert');
    messages.forEach(function(message) {
        message.remove();
    });
}, 5000); 

// Reset search 
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.querySelector('input[name="search"]');
    const searchForm = document.getElementById('searchForm');
    const searchButton = document.getElementById('searchButton');

    searchInput.addEventListener('search', () => {
        searchForm.submit();
    });

    searchButton.addEventListener('click', () => {
        const searchTerm = searchInput.value.trim();
        if (searchTerm) {
            searchForm.submit();
        } else {
            searchInput.focus();
        }
    });
});
