// Calls /packages API to load json object of conda packages
function getPackages(filePath) {
  return $.ajax({
    method: 'GET',
    url: 'http://localhost:8888/packages/' + filePath
  });
}

// Dynamically generates table of packages
function loadTable(items) {
  let results = '';
  for(key in items) {
    var versions = items[key].versions;
    results += `<tr><td><div class="custom-control custom-checkbox"><input class="custom-control-input" type="checkbox" name="${key}" value="${key}" id="package-${key}"><label class="custom-control-label" for="package-${key}">${key}</label></div></td><td><select class="custom-select" id="version-${key}">`;
    for(x in versions) {
      results += '<option value="' + versions[x] + '">' + versions[x] + '</option>';
    }
    results += '</select></td></tr>';
  }
  document.getElementById('tableBody').innerHTML = results;
}

// Basic search through table of packages
function search() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("search");
  filter = input.value.toUpperCase();
  table = document.getElementById("packageTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

// Loads packages from the conda main and bioconda channels as a JSON object
function initPackages() {
  return getPackages('main.json').then((main) => {
    return JSON.parse(main);
  });
}

// Triggered on form submit, retrieves values from form
$('#submit').click(function () {
  // Request data object
  let body = {
    id: '',
    author: '',
    email: '',
    project_repo: '',
    base_image: '',
    dependencies: {},
    volumes: {},
    os_packages: {}
  };

  body.author = $('#author').val();
  body.email = $('#email').val();
  body.project_repo = $('#github').val();
  body.base_image = $('#base').val();
  $('input:checkbox:checked').each((key, item) => {
    body.dependencies[item.name] = $('#version-' + item.name + ' option:selected').text();
  });
  body.id = new Date().valueOf();
  submit(body);
});

// Forces a file download in browser with hidden link attribute
function download(filename, text) {
  let element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

// Submit request to /submit API
function submit(item) {
  $('#triggerLoading').trigger('click');
  return $.ajax({
    method: 'POST',
    url: 'http://localhost:8888/submit',
    data: JSON.stringify(item)
  }).done((data) => {
    $('#close').trigger('click');
    data = JSON.parse(data);
    document.getElementById('imageID').innerText = data.id;
    $("#triggerDialog").trigger('click');
    download('Dockerfile', data.file);
  });
}

// Initialization
initPackages().then((data) => {
  loadTable(data);
});