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
    return getPackages('bioconda.json').then((conda) => {
      return Object.assign(JSON.parse(main), JSON.parse(conda));
    });
  });
}



// Triggered on form submit, retrieves values from form
$('#submit').click(function () {
  // Request data object
  let body = {
    id: '',
    project_repo: '',
    base_image: '',
    dependencies: {},
    volumes: {},
    os_packages: {}
  };

  body.project_repo = $('#github').val();
  body.base_image = $('#base').val();
  $('input:checkbox:checked').each((key, item) => {
    body.dependencies[item.name] = $('#version-' + item.name + ' option:selected').text();
  });
  body.id = new Date().valueOf();
  submit(body);
});

// Submit request to /submit API
function submit(item) {
  $.ajax({
    method: 'POST',
    url: 'http://localhost:8888/submit',
    data: JSON.stringify(item)
  });
}

// Initialization
initPackages().then((data) => {
  loadTable(data);
});