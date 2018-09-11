# AutoContain

## Introduction
AutoContain is a web-based application for generating Dockerfiles and Docker images for scientific applications. Container technologies provide a valuable resource for bioinformaticians and data analysts within the scientific community. By bundling and packaging a complete toolchain or workflow, a container can provide portability, automation, and reproducibility.    

This web application is meant for scientists who want a reproducible Docker image for their scientific projects and applications, but who do not have much experience in writing Dockerfiles or have trouble managing the dependencies that their project may rely on. The user-friendly web based GUI guides a user through all the steps to generate an appropriate Docker image.

## Features
* A selection of various base languages (eg. Python, R, Perl, Java, etc...)
* Curation of relevant packages from popular language-specific package managers for easy accessibility
* Option to utilize existing projects from GitHub repositories
* Option to include data files in Docker image or mount an existing data volume
* Hosting of generated Docker images in public Docker Hub repository
* Generation of raw Dockerfile 
* User-friendly instructions for using Docker images
* Easy deployment instructions for the AutContain application

### Future Development
* Support for multiple programming languages and package managers
* Support for third-party tools and binaries
* Automated deployment of Jupyter Notebook environment
* GUI based pipeline generation and management
* Container based scalability through third-party tools
* Other deployment options (eg. desktop application)

-----

## Installation
* Prerequisites: Docker

1. 
