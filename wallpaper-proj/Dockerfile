FROM python:3.10.8


WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt 

COPY ./myproj ./myproj


CMD ["python3.10", "./myproj/manage.py", "runserver", "0.0.0.0:8000"]

