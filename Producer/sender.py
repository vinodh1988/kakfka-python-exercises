from kafka import KafkaProducer


brokers=["localhost:9092"]
topic="messages"

producer=KafkaProducer(bootstrap_servers=brokers)

def messageSender(message):
    producer.send('messages',message)
