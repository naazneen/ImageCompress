FROM python:3.10.0rc1-alpine3.13
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]