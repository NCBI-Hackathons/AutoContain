import subprocess
import traceback
import argparse

def build_docker(folderPath):
    subprocess.run(['docker', 'build', '-t', 'autocontain/image:' + folderPath, folderPath])

def push_docker(id):
    subprocess.run(['docker', 'push', 'autocontain/image:' + id])


