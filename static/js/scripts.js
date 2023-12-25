// Remove alert messages after 5 seconds
setTimeout(function() {
    let messages = document.querySelectorAll('.alert');
    messages.forEach(function(message) {
        message.remove();
    });
}, 5000); 

// Reset search 
document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.querySelector('#searchForm');
    const searchInput = document.querySelector('input[name="search"]');

    searchInput.addEventListener('input', () => {
        searchForm.submit();
    });
});