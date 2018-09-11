# AutoContain - Automated-containerized-bioinformatics-workflows
![License](LICENSE)
## Summary
AutoContain is a web-based application for generating Dockerfiles and Docker images for scientific applications. Container technologies provide a valuable resource for bioinformaticians and data analysts within the scientific community. By bundling and packaging a complete toolchain or workflow, a container can provide portability, automation, and reproducibility.

This web application is meant for scientists who want a reproducible Docker image for their scientific projects and applications, but who do not have much experience in writing Dockerfiles or have trouble managing the dependencies that their project may rely on. The user-friendly web based GUI guides a user through all the steps to generate an appropriate Docker image.
## Table of Contents
1. [Features](#Features)
2. [Future Development](#Future-Development)
3. [Installation](#Installation)
4. [Usage](#Usage)
5. [Citing `AutoContain`](#citing-AutoContain)
6. [Troubleshooting](#troubleshooting)

## Features
* A selection of various base languages (eg. Python, R, Perl, Java, etc...)
* Curation of relevant packages from popular language-specific package managers for easy accessibility
* Option to utilize existing projects from GitHub repositories
* Option to include data files in Docker image or mount an existing data volume
* Hosting of generated Docker images in public Docker Hub repository
* Generation of raw Dockerfile 
* User-friendly instructions for using Docker images
* Easy deployment instructions for the AutContain application

## Future-Development
* Support for multiple programming languages and package managers
* Support for third-party tools and binaries
* Automated deployment of Jupyter Notebook environment
* GUI based pipeline generation and management
* Container based scalability through third-party tools
* Other deployment options (eg. desktop application)


## Installation
* Prerequisites: 
  1. System Requirements : Unix/Linux OS Variants 
  2. [Docker Installation]:(https://docs.docker.com/install/) 
  3. Internet Browser (Chrome/Firefox)
## Usage
1. [Open a web-GUI]:(put link here)
2. Select a Base Programming Language from a dropdown menu
3. Select packages and appropriate versions from a list of available packages table (Type name in a search-box for quick lookup) 

## Citing-AutoContain
Until `AutoContain` is published, please cite using its [github_repo](https://github.com/NCBI-Hackathons/AutoContain).

## Troubleshooting
As issues arise and common problems are identified, we will list them here.
1. Currently this tool is built to provide libraries from Anaconda and only supports Python packages.
