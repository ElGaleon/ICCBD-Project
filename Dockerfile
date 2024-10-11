FROM confluentinc/cp-kafka:latest

# Install ping
RUN apk update && apk add iputils

# Your other Kafka configurations here...
