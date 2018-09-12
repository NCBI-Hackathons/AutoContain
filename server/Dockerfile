FROM python:3.7-slim

ARG SOURCE_FOLDER="./"

COPY ${SOURCE_FOLDER} .

RUN pip install tornado==5.1
RUN apt-get install -y docker-ce

EXPOSE 8888

ENTRYPOINT ["python", "main.py"]