# base image  
FROM python:3.8   

#Set the working directory to /home
WORKDIR /home

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . /home

# run this command to install all dependencies  
RUN pip install -r requirements.txt  

# port where the Django app runs  
EXPOSE 8000  

# start server  
CMD ["python", "manage.py", "runserver"] 