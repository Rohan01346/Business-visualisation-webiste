function submitForm() {
    var email = document.getElementById("forgot-email").value;
   
    setTimeout(function () {
        var success = Math.random() < 0.8; 
        showMessage(success);
    }, 2000); 

   
    document.getElementById("message").innerText = "Sending reset link...";
    document.getElementById("form-heading").innerText = "Please wait";


    document.getElementById("forgot-button").disabled = true;
}

function showMessage(success) {
    var messageElement = document.getElementById("message");
    var formHeading = document.getElementById("form-heading");

    if (success) {
        messageElement.innerText = "Password reset link has been sent to your email.";
        messageElement.style.color = "green";
    } else {
        messageElement.innerText = "Failed to send reset link. Please try again.";
        messageElement.style.color = "red";
        formHeading.innerText = "Forgot Password";
    }

    // Enable the button again
    document.getElementById("forgot-button").disabled = false;

    // Display the message
    messageElement.classList.remove("hidden");

    // Optionally, reset the form or redirect the user
    // document.getElementById("forgotPasswordForm").reset();
}