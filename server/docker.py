import subprocess
import traceback
import argparse

def build_docker(image_path):
    # Still not working, need to change to the directory of the docker file
    # then initiate build process
    p = subprocess.run(['docker', 'build', '-t', 'autocontain/', image_path])
    p.stdin.write(str(content))
    p.stdin.flush()
    if sp.returncode != 0:
        raise Exception('Build failed')
    print('Build succeeded')

def push_docker(image_id):
    # This function will need to take the image_id and push
    # the completed image to Dockerhub. Will most likely need
    # to use docker-py to do that
    # https://github.com/docker/docker-py
    return(None)

