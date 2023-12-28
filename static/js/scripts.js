/**
 * Remove alert messages after a delay of 5 seconds.
 * Automatically removes alert elements with the '.alert' class from the DOM.
 */
setTimeout(() => {
    const messages = document.querySelectorAll('.alert');
    messages.forEach((message) => {
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
  
    const debounce = (func, delay) => {
      let timeoutId;
      return (...args) => {
        if (timeoutId) {
          clearTimeout(timeoutId);
        }
        timeoutId = setTimeout(() => {
          func(null, ...args);
        }, delay);
      };
    };
  
    const delayedSubmit = debounce(() => {
      if (searchInput.value === '') {
        searchForm.submit();
      }
    }, 300);
  
    if (searchButton) {
      searchButton.addEventListener('click', () => {
        searchForm.submit();
      });
  
      searchInput.addEventListener('input', delayedSubmit);
    }
  });
  
  /**
   * Triggers a click event on the delete link.
   */
  function deleteItem() {
    document.getElementById('deleteLink').click();
  }
  
  let deleteConfirmed = false;
  
  /**
   * Resets the UI buttons to their default state after delete confirmation.
   */
  function resetButtons() {
    const cancelButton = document.querySelector('#cancelButton');
    const deleteButton = document.getElementById('deleteButton');
    const editButton = document.querySelector('#editButton');
  
    deleteButton.innerHTML = `
          <i class="fa-solid fa-trash-can me-1"></i>
          Delete
      `;
    cancelButton.classList.add('d-none');
    deleteButton.classList.remove('btn-danger');
    deleteButton.classList.add('btn-outline-danger');
    editButton.classList.remove('d-none');
    deleteConfirmed = false;
  }
  
  /**
   * Toggles the delete confirmation in the user interface.
   * @returns {void}
   */
  function toggleDeleteConfirmation() {
    const cancelButton = document.querySelector('#cancelButton');
    const deleteButton = document.getElementById('deleteButton');
    const editButton = document.querySelector('#editButton');
  
    if (!deleteConfirmed) {
      deleteButton.innerHTML = `
              <i class="fa-solid fa-exclamation-circle me-1"></i>
              Confirm Delete
          `;
      cancelButton.classList.remove('d-none');
      deleteButton.classList.remove('btn-outline-danger');
      deleteButton.classList.add('btn-danger');
      editButton.classList.add('d-none');
      deleteConfirmed = true;
    } else {
      deleteItem();
      resetButtons();
    }
  }