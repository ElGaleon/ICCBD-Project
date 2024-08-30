from kafka import KafkaConsumer

# Create a Kafka consumer
consumer = KafkaConsumer(
    'example-topic',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',  # Start reading from the beginning
    group_id='example-group'
)

# Consume messages
print("Consuming messages...")
for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")
