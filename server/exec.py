from subprocess import call

def buildDocker(imageName, filePath):
    call(["docker", "build", "-t", "autocontain/" + imageName, filePath])
