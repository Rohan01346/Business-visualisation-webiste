 // JavaScript for smooth scrolling
 document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

window.onscroll = function() {
    var header = document.querySelector("header");

    // Add 'sticky' class when scrolling down
    if (window.pageYOffset > 0) {
        header.classList.add("sticky");
    } else {
        header.classList.remove("sticky");
    }

    // Change background color based on scroll position
    if (window.pageYOffset === 0) {
        header.style.backgroundColor = 'transparent';
    } else {
        header.style.backgroundColor = 'white';
    }
};


// Add this to your existing JavaScript
const gmailIcon = document.getElementById('popgmail');
const gmailPopup = document.getElementById('gmail-popup');

gmailIcon.addEventListener('mouseover', () => {
    gmailPopup.style.display = 'block';
});

gmailIcon.addEventListener('mouseout', () => {
    gmailPopup.style.display = 'none';
});

