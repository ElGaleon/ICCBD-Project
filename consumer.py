# kafka-pocs/kafka-dev-with-docker/part-04/consumer.py
import os
import time
import logging

from kafka import KafkaConsumer
from kafka.errors import KafkaError

logging.basicConfig(level=logging.INFO)


def print_info(msg: dict):
    for t, v in msg.items():
        for r in v:
            logging.info(
                f"key={r.key}, value={r.value}, topic={t.topic}, partition={t.partition}, offset={r.offset}, ts={r.timestamp}"
            )


class Consumer:
    def __init__(self, bootstrap_servers: list, topics: list, group_id: str) -> None:
        self.bootstrap_servers = bootstrap_servers
        self.topics = topics
        self.group_id = group_id
        self.consumer = self.create()

    def create(self):
        return KafkaConsumer(
            *self.topics,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id=self.group_id,
            # key_deserializer=lambda v: v.decode("utf-8"),
            # value_deserializer=lambda v: v.decode("utf-8"),
        )

    def process(self):
        try:
            while True:
                msg = self.consumer.poll(timeout_ms=1000)
                if msg is None:
                    continue
                print_info(msg)
                time.sleep(1)
        except KafkaError as error:
            logging.error(error)


if __name__ == "__main__":
    consumer = Consumer(
        bootstrap_servers=os.getenv("BOOTSTRAP_SERVERS", "kafka-0:9092").split(","),
        topics=os.getenv("TOPIC_NAME", "orders").split(","),
        group_id=os.getenv("GROUP_ID", "orders-group"),
    )
    consumer.process()
