function loadAnacondaPackages(filePath) {
  let condaPackages = {},
    re = /^([0-9]|[1-9][0-9]*)\.([0-9]|[1-9][0-9]*)\.([0-9]|[1-9][0-9]*)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+[0-9A-Za-z-]+)?$/;

  return $.getJSON(filePath, (data) => {
    for (package in data.packages) {
      let name = data.packages[package].name,
        version = data.packages[package].version;

      if (condaPackages[name] && condaPackages[name].versions) {
        if (condaPackages[name].versions.indexOf(version) === -1 && re.test(version)) {
          condaPackages[name].versions.push(version);
        }
      } else {
        if (name !== 'constructor') {
          condaPackages[name] = {
            versions: [
              version
            ]
          };
        }
      }
    }
    return condaPackages;
  });
}

function loadPackages() {
  let mainChannel = loadAnacondaPackages('./anacondaPackages.json'),
    biocondaChannel = loadAnacondaPackages('./biocondaPackages.json');

  return {main: mainChannel, bioconda: biocondaChannel};
}

function submit() {

}