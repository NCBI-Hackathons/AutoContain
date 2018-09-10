# Autocontain

AutoContain is a web-based application for generating Dockerfiles and images for scientific applications. Initially it is focused on the Anaconda Python repositories.

The application will allow users to select various components of a Docker image including a base Docker image, programming language packages and dependencies, operating system applications, imported data, and volume mapping.

This web application is meant for scientists who want a reproducible Docker image for their scientific projects and applications, but who don't have much experience in writing Dockerfiles or who don't want to track down specific version numbers for all of the dependencies that their project require.

To speed up development, users can point to an existing git repository to be imported into the image.

The application will initially be hosted on an AWS instance that can build images to be automatically uploaded to DockerHub. The goal of the project is to eventually allow the project to be deployed and managed on organization's internal servers.