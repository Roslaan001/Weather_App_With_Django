Created this django app where users can check the weather of any city/country in the world, it was created when I was learning backend with django, but now that I am currently learning Devops and Cloud Engineering, I created a Dockerfile for the app, where I built the docker image of the app 


The Dockerfile is as follows:
```dockerfile
# the base image
FROM python:3.9.21-alpine3.21

# Set the working directory
WORKDIR /my-django-app

# Copy the current directory contents into the container at /app
COPY . /my-django-app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside the docker container
EXPOSE 8000

# Run the command to start the development server
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]

