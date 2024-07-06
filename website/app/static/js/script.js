document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('kolamBaruModal');
    var successModal = document.getElementById('successSubmitModal');
    var openModalLink = document.querySelector('a[href="/new-kolam"]');
    var closeModalButton = document.querySelector('.close');
    var form = document.getElementById('kolamForm');
    var otherMenuModal = document.getElementById('otherMenuModal');
    var notificationModal = document.getElementById('notificationModal');
    var otherMenuButton = document.querySelector('.other');
    var notificationButton = document.getElementById('notification');
    var logoutButton = document.getElementById('logout');
    var closeNotificationButton = document.querySelector('.close-notification');

    // Open modal
    openModalLink.addEventListener('click', function(event) {
        event.preventDefault();
        modal.style.display = 'block';
    });

    // Close modal
    closeModalButton.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    // Close modal when clicking outside of the modal-content
    window.addEventListener('click', function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
        if (event.target == successModal) {
            successModal.style.display = 'none';
        }
    });

    // Form submit handler
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Close the current modal
        modal.style.display = 'none';

        // Show success modal
        successModal.style.display = 'block';

        // Close success modal after 1 second
        setTimeout(function() {
            successModal.style.display = 'none';
        }, 2000);
    });

    notificationModal.style.display = 'block';

    // Event untuk membuka modal lainnya
    otherMenuButton.addEventListener('click', function() {
        otherMenuModal.style.display = 'block';
    });

    // Event untuk menampilkan modal notifikasi
    notificationButton.addEventListener('click', function() {
        otherMenuModal.style.display = 'none';
        notificationModal.style.display = 'block';
    });

    // Event untuk menutup modal notifikasi
    closeNotificationButton.addEventListener('click', function() {
        notificationModal.style.display = 'none';
    });

    // Event untuk menutup modal ketika mengklik di luar modal-content
    window.addEventListener('click', function(event) {
        if (event.target == otherMenuModal) {
            otherMenuModal.style.display = 'none';
        }
        if (event.target == notificationModal) {
            notificationModal.style.display = 'none';
        }
    });

    // Event untuk tombol logout
    logoutButton.addEventListener('click', function() {
        // Tambahkan logika logout di sini
        alert("Anda telah logout.");
        otherMenuModal.style.display = 'none';
    });
});