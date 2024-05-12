    // Get the file input element
    const fileInput = document.getElementById('fileInput');
    // Get the div where the file list will be displayed
    const fileList = document.getElementById('fileList');

    // Add event listener for file selection
    fileInput.addEventListener('change', function() {
      // Clear previous file list
      fileList.innerHTML = '';

      // Loop through selected files and display their names
      Array.from(fileInput.files).forEach(file => {
        const listItem = document.createElement('div');
        listItem.textContent = file.name;
        fileList.appendChild(listItem);
      });
    });