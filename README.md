# AutoContain: Automated Containerization of Bioinformatics Pipelines
[MIT License](LICENSE)
## Summary
AutoContain is a web-based application for generating Dockerfiles and Docker images for scientific applications. Container technologies provide a valuable resource for bioinformaticians and data analysts within the scientific community. By bundling and packaging a complete toolchain or workflow, a container can provide portability, automation, and reproducibility.

This web application is meant for scientists who want a reproducible Docker image for their scientific projects and applications, but who do not have much experience in writing Dockerfiles or have trouble managing the dependencies that their project may rely on. The user-friendly web based GUI guides a user through all the steps to generate an appropriate Docker image.

## Features
* Support for Python 3.7
* Curation of relevant packages (eg. Bioconda) from the Anaconda package manager for easy accessibility
* Option to utilize existing projects from GitHub repositories
* Hosting of generated Docker images in public [Docker Hub repository](https://hub.docker.com/r/autocontain/image)
* Generation and download of raw Dockerfile 
* User-friendly instructions for using Docker images
* Easy deployment instructions for the AutContain application

## Usage
1. Go to provided web url. If AutoContain is not yet deployed, see installation instructions below.
1. Select a `Base Programming Language` from the dropdown menu.
1. Select packages and appropriate versions from a list of available packages (use the autocomplete search box).
1. After submission, AutoContain will build a Dockerfile automatically from user selected tools.
1. The composed Dockerfile will automatically download from the browser.
1. The Docker image will also be built and pushed to the [AutoContain Docker Hub](https://hub.docker.com/r/autocontain/image/).
1. Instructions for using your Docker image will be displayed in a popup window.
 
* For more information about Docker Hub repositories or how to use pre-built repositories available please visit (https://hub.docker.com/explore/).

## Installation
* Prerequisites: 
  1. [Docker](https://docs.docker.com/install/)
  1. [Docker Compose](https://docs.docker.com/compose/install/)

1. Copy the [docker-compose.yml](docker-compose.yml) from the [AutoContain GitHub repository](https://github.com/NCBI-Hackathons/AutoContain).
1. Check that your Docker daemon is running and that you have the docker-compose CLI installed.
1. Change your working directory to location where the docker-compose.yml file is located.
1. Run `docker-compose up -d`.

### Workflow Diagram
![workflow](https://github.com/NCBI-Hackathons/AutoContain/blob/master/ui/BasicWorkflow.png)
  #### Example
  ![example workflow](https://github.com/NCBI-Hackathons/AutoContain/blob/master/ui/Web_Interface.png)

## Future Development
* Support for multiple programming languages and package managers (eg. R, Perl, Java, etc...)
* Support for multiple package managers
* Support for third-party tools and binaries
* Option to wrap data in image or mount a volume of data to the Docker image
* Automated deployment of Jupyter Notebook environment
* GUI based pipeline generation and management
* Container based scalability through third-party tools
* Other deployment options (eg. desktop application)

## Citing-AutoContain
Until `AutoContain` is published, please cite using its [GitHub_repository](https://github.com/NCBI-Hackathons/AutoContain).

## Troubleshooting
Please feel free to utilize the Issue submission and tracking system provided via GitHub. We will try to address issues to the best of our ability.

## Contributing
Please feel free to submit pull requests for any bugs or new features you like to add. Pre-planned features, as well as their current statuses, will be populated in the Issues tab.
