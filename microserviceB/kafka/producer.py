from confluent_kafka import Producer
#localhost:9094
producer = Producer({'bootstrap.servers': 'localhost:9094'})