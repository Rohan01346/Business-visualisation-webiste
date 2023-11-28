document.addEventListener('click', function(event) {
    var dropdownContent = document.getElementById('dropdownContent');
    var userIcon = document.getElementById('userIcon');
  
    if (!userIcon.contains(event.target) && !dropdownContent.contains(event.target)) {
        dropdownContent.classList.remove('show');
    }
  });
  
  document.getElementById('userIcon').addEventListener('click', function() {
    var dropdownContent = document.getElementById('dropdownContent');
    dropdownContent.classList.toggle('show');
  });

  