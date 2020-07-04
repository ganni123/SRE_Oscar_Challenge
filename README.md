In this challenge I have created Hello World! python application and python script for capturing the error codes from ErrorLog.txt file. Finally created docker file for running the docker contianer. In the docker file I mentined aobut ubuntu as the base image. copied the sample1.py and log_responses.log to /home/app directory. Given the command as running log_responses.py python script with hardcoded start time and end time for capturing the log from error.log file

Steps:

1. Create python application
2. Create python script to grep the errors codes from the log file
3. Create docker file-> docker image-> docker container
4. Run the docker container with the application and store the logs in /home/app location

Docker commands used:

docker build .

docker run [contianerID]
