FROM python:3.11
RUN mkdir /fastapi_app
WORKDIR /fastapi_app
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .
RUN chmod a+x docker/*.sh
#WORKDIR src
#
#CMD gunicorn main:app --bind=0.0.0.0:8000
