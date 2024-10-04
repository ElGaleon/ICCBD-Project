package ICCBD_Project

import (
	"fmt"
	"log"
	"time"

	"github.com/confluentinc/confluent-kafka-go/kafka"
)

func main() {
	producer, err := kafka.NewProducer(&kafka.ConfigMap{
		"bootstrap.servers": "kafka:9092",
		"acks":              "all", // Ensure all brokers confirm message delivery
	})
	if err != nil {
		log.Fatal("Failed to create producer:", err)
	}
	defer producer.Close()

	topic := "test-topic"

	for i := 0; i < 10; i++ {
		message := fmt.Sprintf("Message %d", i)
		err := producer.Produce(&kafka.Message{
			TopicPartition: kafka.TopicPartition{Topic: &topic, Partition: kafka.PartitionAny},
			Value:          []byte(message),
		}, nil)

		if err != nil {
			log.Println("Failed to produce message:", err)
		}
		time.Sleep(1 * time.Second) // Add delay between messages
	}

	producer.Flush(15000) // Wait for message delivery
}
