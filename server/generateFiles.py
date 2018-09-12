import sys
import json
import io
import os

# Calls all functions to parse json object into Dockerfile and environments.yml files
def run(jsonDict, outputPath):
    dockerFileString = getDockerfile(jsonDict)
    writeDockerfile(dockerFileString, outputPath)
    return dockerFileString

# Generates a Dockerfile as a string
def getDockerfile(jsonDict):
    dockerFileString = io.StringIO()

    dockerFileString.write("FROM " + jsonDict["base_image"] + "\n\n")

    dockerFileString.write('LABEL author="' + jsonDict["author"] + '"\n')
    dockerFileString.write('LABEL email="' + jsonDict["email"] + '"\n\n')

    if(len(jsonDict["dependencies"]) > 0):
        dockerFileString.write("RUN conda install -y ")
        for package in jsonDict["dependencies"]:
            dockerFileString.write(str(package) + "==" + jsonDict["dependencies"][package] + " ")
    dockerFileString.write("\n")

    if(jsonDict["project_repo"]):
        dockerFileString.write('RUN git clone "' + jsonDict["project_repo"] + '"\n')

    osPackageStringLine = appendOSPackages(jsonDict)
    dockerFileString.write(osPackageStringLine)
    volumeStringLine = appendVolume(jsonDict)
    dockerFileString.writelines(volumeStringLine)
    dockerFileString.write('CMD ["python"]')

    return dockerFileString.getvalue()

# Writes a string to a file
def writeDockerfile(dockerFileString,outputPath):
    dockerFile = open(os.path.join(outputPath,"Dockerfile"), "w")
    dockerFile.write(dockerFileString)
    dockerFile.close()

def appendOSPackages(jsonDict):
    osPackagesDict = jsonDict["os_packages"]
    osPackageFileString = io.StringIO()

    for osPackage in osPackagesDict:
        packageVersion = osPackagesDict[osPackage]
        osPackageFileString.write(osPackage + packageVersion + " ")

    return "RUN apt-get update && apt-get install -y " + osPackageFileString.getvalue() + "\n"

def appendVolume(jsonDict):
    volumeDict = jsonDict["volumes"]

    volumeString = io.StringIO()
    for volumeName in volumeDict:
        volumeString.write("/VOLUME " + str(volumeDict[volumeName]) + "\n")

    return volumeString.getvalue()
