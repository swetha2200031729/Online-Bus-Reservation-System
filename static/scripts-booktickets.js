document.addEventListener("DOMContentLoaded", function() {
    var form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        var numOfSeatsInput = document.getElementById("inputEmail3");
        var numOfSeats = parseInt(numOfSeatsInput.value);

        // Validate number of seats
        if (isNaN(numOfSeats) || numOfSeats <= 0) {
            alert("Please enter a valid number of seats.");
            event.preventDefault(); // Prevent form submission
        }
    });
});
