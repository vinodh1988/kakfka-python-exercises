from kafka import KafkaProducer


brokers=["localhost:9092"]
topic="messages"

producer=KafkaProducer(bootstrap_servers=brokers)

def keySender(key,message):
    producer.send(topic,key=key.encode('utf-8'),value=message.encode('utf-8'))
