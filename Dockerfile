FROM golang:1.19

ENV PORT=9000
WORKDIR /app
COPY . .
RUN go get -d -v github.com/confluentinc/confluent-kafka-go/kafka \
RUN go build
CMD ["./server"]

