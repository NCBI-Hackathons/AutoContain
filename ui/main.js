function loadPackages(filePath) {
  let xhr = new XMLHttpRequest();

  xhr.open('GET', 'http://localhost:8888/packages/' + filePath, true);
  xhr.send();

  xhr.onreadystatechange = function () {
    return xhr.responseText;
  };
}

function submit() {

}