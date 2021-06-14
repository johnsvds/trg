FROM python:3.6

RUN mkdir /microserviceB
WORKDIR /microserviceB
ADD . /microserviceB
EXPOSE 9094
RUN pip install -r requirements.txt

CMD ["python","main.py"]
