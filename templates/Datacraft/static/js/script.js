// Get references to elements
const signupForm = document.getElementById("signup-form");
const loginForm = document.getElementById("login-form");
const showSignupButton = document.getElementById("show-signup-button");
const showLoginButton = document.getElementById("show-login-button");

// Function to show the signup form and hide the login form
function showSignup() {
    signupForm.style.display = "block";
    loginForm.style.display = "none";
    showSignupButton.style.display = "none";
    showLoginButton.style.display = "block";
}

// Function to show the login form and hide the signup form
function showLogin() {
    signupForm.style.display = "none";
    loginForm.style.display = "block";
    showSignupButton.style.display = "block";
    showLoginButton.style.display = "none";
}

// Add event listeners to buttons
showSignupButton.addEventListener("click", showSignup);
showLoginButton.addEventListener("click", showLogin);
