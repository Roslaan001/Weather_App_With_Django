# the base image
FROM python:3.12-slim-bookworm

#create the directory for my django app
RUN mkdir -p /my-django-app

# Set the working directory for my django app
WORKDIR /my-django-app

# Copy the current directory contents into the container at /my-django-app
COPY . /my-django-app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available outside this container
EXPOSE 8000

# Run the command to start the development server
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
