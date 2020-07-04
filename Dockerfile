# Use Matthewfeickert image as a parent image.
FROM matthewfeickert/docker-python3-ubuntu

#Install flask dependencies using pip
RUN pip install flask

#Copy Sample python code  
COPY sample1.py /home/app/logs_responses.py

#Copy ErrorLog text file
COPY ErrorLog.txt /home/app/error.log

#Becoming root user and change the permissins
USER root

RUN chown -R $USER:$USER /home/app/error.log

SHELL ["/bin/bash", "-c"] 

CMD ["python", "/home/app/logs_responses.py", "17/May/2015:18:05:23 +0000", "17/May/2015:18:05:59 +0000", "/home/app/error.log"]





