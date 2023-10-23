# Use the slim variant of Python 3.10.10.
FROM python:3.10.10-slim

# Set container's working directory.
WORKDIR /app_home

# Copying requirements
COPY ./requirements.txt /app_home/requirements.txt

# Install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app_home/requirements.txt

# Copy the application 
COPY /src/web_service /app_home/web_service
WORKDIR /app_home/web_service

# Expose port 8001 for the application.
EXPOSE 8001

# Run the app on a container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
