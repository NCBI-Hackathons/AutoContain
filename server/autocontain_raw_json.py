import sys
import json
import io
import os

def Wrapper(jsonDict,outputPath):
    dockerFileString = dockerFileStringFromDict(jsonDict)
    writeDockerFile(dockerFileString,outputPath)
    generateEnvironmentEnv(jsonDict,outputPath)

def dockerFileStringFromDict(jsonDict):
    print ("Created file from jsonDict")
    dockerFileString = io.StringIO()
    # 1. Write base image date
    dockerFileString.write("FROM " + jsonDict["base_image"]+"\n")
    # dockerFileString.write("\n")
    dockerFileString.write("RUN conda env update -f environment.yml\n")
    osPackageStringLine = appendOSPackages(jsonDict)
    dockerFileString.write(osPackageStringLine)
    volumeStringLine = appendVolume(jsonDict)
    dockerFileString.writelines(volumeStringLine)
    dockerFileString.write("CMD /bin/bash\n")

    return dockerFileString.getvalue()

def writeDockerFile(dockerFileString,outputPath):
    dockerFile = open(os.path.join(outputPath,"DOCKERFILE"), "w")
    dockerFile.write(dockerFileString)
    dockerFile.close()

def appendBaseImageName(jsonDict):

    # only 1 base image so read directly from dict
    baseImageNameList = list(jsonDict.keys())
    baseImageName = baseImageNameList[0]
    baseImageVersion = jsonDict[baseImageName]

    return "FROM " + baseImageName + ":" + baseImageVersion + "\n"

def appendOSPackages(jsonDict):
    osPackagesDict = jsonDict["os_packages"]
    osPackageFileString =io.StringIO()

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

def generateEnvironmentEnv(jsonDict,outputPath):
    environmentYmlString = io.StringIO()
    environmentDependenciesYmlString = io.StringIO()
    environmentDependenciesYmlString.write("name: " + jsonDict['id']+"\n")
    environmentDependenciesYmlString.write("dependencies:" + "\n")
    dependencies = jsonDict['dependencies']
    for dependency in dependencies:
        environmentDependenciesYmlString.write("    - " + str(dependency) + "=" + dependencies[dependency])
        environmentDependenciesYmlString.write("\n")
    environmentYmlFile = open(os.path.join(outputPath,"environment.yml"),"w")
    environmentYmlFile.write(environmentYmlString.getvalue())
    environmentYmlFile.write(environmentDependenciesYmlString.getvalue())
    environmentYmlFile.close()
