
function previewImage(input) {
    var preview = document.getElementById('picturePreview');
    var file = input.files[0];
    var reader = new FileReader();

    reader.onload = function (e) {
        preview.src = e.target.result;
        preview.style.display = 'block';
    };

    if (file) {
        reader.readAsDataURL(file);
    }
}

function flipText(element) {
    element.style.transform = 'rotateY(180deg)';
  }
  
  function resetText(element) {
    element.style.transform = 'rotateY(0deg)';
  }
  