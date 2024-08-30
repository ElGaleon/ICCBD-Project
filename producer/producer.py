from kafka import KafkaProducer
import time

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers='kafka:9092')

topic = 'example-topic'

# Send messages with a key to ensure they go to the same partition
for i in range(1, 11):
    key = b'order_key'  # Key to ensure all messages go to the same partition
    value = f'Message {i}'.encode('utf-8')
    producer.send(topic, key=key, value=value)
    print(f"Sent: {value.decode('utf-8')}")
    time.sleep(1)  # Simulate some delay between messages

producer.flush()
producer.close()
