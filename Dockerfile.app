# Based on your Dockerfile and the adjustments mentioned:

# Use the slim variant of Python 3.10.10.
FROM python:3.10.10-slim

# Set container's working directory.
WORKDIR /app_home

# Install conda (this is a basic example, it might need adjustments based on the Miniconda version)
RUN apt-get update && apt-get install -y wget && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    sh Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda && \
    rm Miniconda3-latest-Linux-x86_64.sh

# Add Miniconda to PATH
ENV PATH="/miniconda/bin:$PATH"

# Copy the application and install dependencies.
COPY . .
RUN conda env create -f environment.yml

# Expose port 8000 for the application.
EXPOSE 8000

# Move to the right folder
WORKDIR /app_home/src/web_service

# Run Uvicorn when the container starts using the full path to the conda environment.
CMD ["/miniconda/envs/x-hec-solution/bin/uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
