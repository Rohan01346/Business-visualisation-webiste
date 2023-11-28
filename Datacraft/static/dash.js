// Get references to the side panel items and content sections
const sidePanelItems = document.querySelectorAll('.side-panel ul li a');
const contentSections = document.querySelectorAll('.content section');

// Add a click event listener to each side panel item
sidePanelItems.forEach((item, index) => {
  item.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent the default link behavior

    // Hide all content sections
    contentSections.forEach((section) => {
      section.style.display = 'none';
    });

    // Show the corresponding content section based on the index
    contentSections[index].style.display = 'block';
  });
});
