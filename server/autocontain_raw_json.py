import sys
import json
import io

def main():
    if len(sys.argv) > 1:
        print("length of argument is: " + str(len(sys.argv)))
        print(sys.argv[1])
        jsonFile = open(sys.argv[1])
        jsonDict = readFileAsJsonString(jsonFile)

        dockerFileString = dockerFileStringFromDict(jsonDict)

        writeDockerFile(dockerFileString)

        generateEnvironmentEnv(jsonDict)

    else:
        print("No arguments")


def readFileAsJsonString(jsonFile):
    jsonString = jsonFile.read()
    jsonDict = loadJson(jsonString)

    return jsonDict


def loadJson(jsonString):
    #load json into json string
    data = json.loads(jsonString)
    print(type(data))

    for entry in data:
        print(entry + "Value: " + str(data[entry]))

    return data

def dockerFileStringFromDict(jsonDict):
    print ("Create file from jsonDict")

    dockerFileString = io.StringIO()

    # 1. Write base image date
    baseImageDict = jsonDict["base_image"]
    baseImageStringLine = appendBaseImageName(baseImageDict)
    dockerFileString.write(baseImageStringLine)

    dockerFileString.write("\n")

    dockerFileString.write("RUN conda create -f environment.yml\n")


    osPackageStringLine = appendOSPackages(jsonDict)
    dockerFileString.write(osPackageStringLine)

    volumeStringLine = appendVolume(jsonDict)
    dockerFileString.writelines(volumeStringLine)

    dockerFileString.write("EXPOSE 80\n")
    dockerFileString.write("CMD [\"python\", \"app.py\"]\n")

    return dockerFileString.getvalue()

def writeDockerFile(dockerFileString):
    dockerFile = open("DOCKERFILE", "w")
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


def generateEnvironmentEnv(jsonDict):
    environmentYmlString = io.StringIO()
    environmentDependenciesYmlString = io.StringIO()

    repositoryDict = jsonDict["repository"]
    condaChannelsDict = repositoryDict["conda"]

    environmentYmlString.write("name: " + jsonDict["name"] + "\n")
    environmentYmlString.write("channels:\n")
    environmentDependenciesYmlString.write("dependencies:" + "\n")

    if condaChannelsDict is not None:

        for condaChannel in condaChannelsDict:
            environmentYmlString.write("    - " + str(condaChannel) + "\n")

            channelDependencies = condaChannelsDict[condaChannel]
            if channelDependencies is not None:

                for dependency in channelDependencies:
                    environmentDependenciesYmlString.write("    - " + str(dependency) + "=" + channelDependencies[dependency])
                    environmentDependenciesYmlString.write("\n")

    environmentYmlFile = open("environment.yml","w")
    environmentYmlFile.write(environmentYmlString.getvalue())
    environmentYmlFile.write(environmentDependenciesYmlString.getvalue())

    environmentYmlFile.close()


main()