# pull python base image
FROM python:3.10

# copy application files
ADD * /plant_api/

# specify working directory
WORKDIR /plant_api

# update pip
RUN pip install --upgrade pip

# install dependencies
RUN pip install -r requirements.txt

# expose port for application
EXPOSE 8501

# start fastapi application
CMD ["streamlit", "run", "main_app.py"]
