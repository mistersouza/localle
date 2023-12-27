/**
 * Remove alert messages after a delay of 5 seconds.
 * Automatically removes alert elements with the '.alert' class from the DOM.
 */
setTimeout(() => {
    let messages = document.querySelectorAll('.alert');
    messages.forEach(message => {
        message.remove();
    });
}, 5000);
/**
 * Reset search functionality for the search form.
 * Triggers search submission upon input changes and search button clicks.
 * Submits the form when the input field is cleared.
 */
document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.querySelector('#searchForm');
    const searchInput = document.querySelector('input[name="search"]');
    const searchButton = document.querySelector('#searchButton');

    searchButton.addEventListener('click', () => {
        searchForm.submit();
    });

    searchInput.addEventListener('input', () => {
        if (searchInput.value === '') {
            searchForm.submit();
        }
    });
});
