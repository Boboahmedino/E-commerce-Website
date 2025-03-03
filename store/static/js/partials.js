document.addEventListener('DOMContentLoaded', function() {
    // Get all close buttons
    const closeButtons = document.querySelectorAll('.close-btn');
    
    // Add click event to each close button
    closeButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Find the parent alert and hide it
            const alert = this.parentElement;
            alert.style.opacity = '0'; // Fade out the alert
            setTimeout(function() {
                alert.style.display = 'none'; // Remove the alert after fade out
            }, 300); // Adjust time to match the fade-out duration
        });
    });

    // Remove duplicate alerts if any
    const alerts = document.querySelectorAll('.alert');
    const seenMessages = new Set();
    
    alerts.forEach(function(alert) {
        const messageText = alert.querySelector('.message-text').textContent;
        if (seenMessages.has(messageText)) {
            alert.remove();
        } else {
            seenMessages.add(messageText);
        }
    });
});
