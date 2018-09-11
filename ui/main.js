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

let results = '<tr class="header"><th style="width:20%;">SelectPackage</th><th style="width:20%;">Version</th></tr>';
for(key in items) {
  var item = items[key];
  results += '<tr><td><input type="checkbox" value="' + item.name + '">' + item.name + '</td><td><select>';
  for(x in items[key].versions) {
    results += '<option value="' + items[key].versions[x] + '">' + items[key].versions[x] + '</option>';
  }
  results += '</select></td></tr>';
}
document.getElementById('PackageTable').innerHTML = results;