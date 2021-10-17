$(document).ready(function() {
    $('.post-modal').click(function(e) {
        var id = e.target.getAttribute('value')
        var myModal = new bootstrap.Modal(document.getElementById(id))
        myModal.show();
    })
})