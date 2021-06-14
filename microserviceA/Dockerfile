FROM python:3.6

RUN mkdir /microserviceA
WORKDIR /microserviceA
ADD . /microserviceA
EXPOSE 8000
RUN pip install -r requirements.txt

CMD ["python","main.py"]
