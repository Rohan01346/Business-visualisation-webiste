// Get references to the login and signup form elements
const loginForm = document.getElementById('login-form');
const signupForm = document.getElementById('signup-form');

// Get references to the show buttons
const showLoginButton = document.getElementById('show-login-button');
const showSignupButton = document.getElementById('show-signup-button');

// Add click event listeners to the show buttons
showLoginButton.addEventListener('click', () => {
    loginForm.style.display = 'block'; // Display the login form
    signupForm.style.display = 'none'; // Hide the signup form
    showLoginButton.style.display = 'none'; // Hide the show login button
    showSignupButton.style.display = 'block'; // Display the show signup button
});

showSignupButton.addEventListener('click', () => {
    loginForm.style.display = 'none'; // Hide the login form
    signupForm.style.display = 'block'; // Display the signup form
    showLoginButton.style.display = 'block'; // Display the show login button
    showSignupButton.style.display = 'none'; // Hide the show signup button
});

// Initially, show the login form and hide the signup form
loginForm.style.display = 'block';
signupForm.style.display = 'none';
showLoginButton.style.display = 'none';
showSignupButton.style.display = 'block';
