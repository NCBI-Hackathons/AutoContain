function loadPackages(filePath) {
  let xhr = new XMLHttpRequest();

  xhr.open('GET', 'http://localhost:8888/packages/' + filePath, true);
  xhr.send();

  xhr.onreadystatechange = function () {
    return xhr.responseText;
  };
}

let items = [
  {
    name: 'test',
    versions: ['1', '2']
  },
  {
    name: 'test2',
    versions: ['4', '5']
  }
];

// Dynamically generates table of packages
let results = '<tr class="header"><th style="width:20%;">Package</th><th style="width:20%;">Versions</th></tr>';
for(key in items) {
  var item = items[key];
  results += `<tr><td><div class="custom-control custom-checkbox"><input class="custom-control-input" type="checkbox" name="${item.name}" value="${item.name}" id="package-${item.name}"><label class="custom-control-label" for="package-${item.name}">${item.name}</label></div></td><td><select class="custom-select" id="version-${item.name}">`;
  for(x in items[key].versions) {
    results += '<option value="' + items[key].versions[x] + '">' + items[key].versions[x] + '</option>';
  }
  results += '</select></td></tr>';
}
document.getElementById('packageTable').innerHTML = results;

// Triggered on form submit. Retrieves elements.
let selectedPackages = {};
$('#submit').click(function () {
  $('input:checkbox:checked').each((key, item) => {
    selectedPackages[item.name] = $('#version-' + item.name + ' option:selected').text();
  });
});

function search () {
  var input, filter, table, tr, td, i;
  input = document.getElementById("PackageSelection");
  filter = input.value.toUpperCase();
  table = document.getElementById("packageTable");
  tr = table.getElementsByTagName("tr");
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