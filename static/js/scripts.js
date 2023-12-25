// Remove alert messages after 5 seconds
setTimeout(function() {
    var messages = document.querySelectorAll('.alert');
    messages.forEach(function(message) {
        message.remove();
    });
}, 5000); 