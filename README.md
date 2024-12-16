# OpenCV Face Detection in Docker
## OTPRO Lab 2 VCS, CI

This repository contains a Python application to detect faces in an image using OpenCV, packaged into a Docker container.

## Usage

1. Clone the repository:
```bash
   git clone https://github.com/RyogaGrey/Lab2.git
   cd Lab2
```

2. Build and run the Docker container:
<image-path> — Path to the image file you want to process.
```bash
docker build -t face-detect .
docker run -v $(pwd):/app -it face-detect <image-path>
```
Example with default image:

```bash
docker run -it face-detect
```
---
Ensure that Docker is installed and running before you execute these commands.
The project uses OpenCV to detect faces; ensure the required dependencies are included in the Dockerfile.
