# OpenCV Face Detection in Docker
## OTPRO Lab 2 VCS, CI

This repository contains a Python application to detect faces in an image using OpenCV, packaged into a Docker container.

## Usage

1. Clone the repository:
```bash
   https://github.com/RyogaGrey/Lab2.git
   cd LAB2
```

2. Build and run the Docker container:

```bash
docker build -t face-detect .
docker run -v $(pwd):/app -it face-detect <image-path>
```
Example with default image:

```bash
docker run -it face-detect
```
