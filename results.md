# Producer Tests
## Message Delivery Comparison: At Most Once vs At Least Once vs Exactly Once

### At Most Once
```python
    kafka-producer-perf-test.sh --topic my_topic \
    --num-records 500 --throughput 10 --producer-props bootstrap.servers=localhost:9092 \
    key.serializer=org.apache.kafka.common.serialization.StringSerializer value.serializer=org.apache.kafka.common.serialization.StringSerializer \
    --record-size 1 --producer.config var/lib/kafka/config-properties/producer-at-most-once.properties --print-metrics 
```

```python
    kafka-producer-perf-test.sh \
    --topic your_topic \
    --throughput -1 \
    --num-records 3000000 \
    --record-size 1024 \
    --producer-props acks=all bootstrap.servers=localhost:9092 \
    --producer.config var/lib/kafka/config-properties/producer-at-most-once.properties
```


#### Results
```shell
52 records sent, 10.2 records/sec (0.00 MB/sec), 16.4 ms avg latency, 455.0 ms max latency.
51 records sent, 10.1 records/sec (0.00 MB/sec), 2.7 ms avg latency, 13.0 ms max latency.
51 records sent, 10.1 records/sec (0.00 MB/sec), 4.4 ms avg latency, 35.0 ms max latency.
50 records sent, 9.9 records/sec (0.00 MB/sec), 2.5 ms avg latency, 18.0 ms max latency.
51 records sent, 10.2 records/sec (0.00 MB/sec), 2.3 ms avg latency, 21.0 ms max latency.
51 records sent, 10.0 records/sec (0.00 MB/sec), 2.1 ms avg latency, 9.0 ms max latency.
51 records sent, 10.0 records/sec (0.00 MB/sec), 2.6 ms avg latency, 24.0 ms max latency.
50 records sent, 9.9 records/sec (0.00 MB/sec), 2.0 ms avg latency, 5.0 ms max latency.
50 records sent, 10.0 records/sec (0.00 MB/sec), 1.8 ms avg latency, 5.0 ms max latency.
500 records sent, 10.004402 records/sec (0.00 MB/sec), 3.96 ms avg latency, 455.00 ms max latency, 2 ms 50th, 5 ms 95th, 63 ms 99th, 455 ms 99.9th.
```

### Metrics
```shell
Metric Name                                                                         Value
app-info:commit-id:{client-id=producer-1}                                         : 839b886f9b732b15
app-info:start-time-ms:{client-id=producer-1}                                     : 1728777761565
app-info:version:{client-id=producer-1}                                           : 2.8.1
kafka-metrics-count:count:{client-id=producer-1}                                  : 102.000
producer-metrics:batch-size-avg:{client-id=producer-1}                            : 69.230
producer-metrics:batch-size-max:{client-id=producer-1}                            : 101.000
producer-metrics:batch-split-rate:{client-id=producer-1}                          : 0.000
producer-metrics:batch-split-total:{client-id=producer-1}                         : 0.000
producer-metrics:buffer-available-bytes:{client-id=producer-1}                    : 33554432.000
producer-metrics:buffer-exhausted-rate:{client-id=producer-1}                     : 0.000
producer-metrics:buffer-exhausted-total:{client-id=producer-1}                    : 0.000
producer-metrics:buffer-total-bytes:{client-id=producer-1}                        : 33554432.000
producer-metrics:bufferpool-wait-ratio:{client-id=producer-1}                     : 0.000
producer-metrics:bufferpool-wait-time-total:{client-id=producer-1}                : 0.000
producer-metrics:compression-rate-avg:{client-id=producer-1}                      : 1.000
producer-metrics:connection-close-rate:{client-id=producer-1}                     : 0.000
producer-metrics:connection-close-total:{client-id=producer-1}                    : 0.000
producer-metrics:connection-count:{client-id=producer-1}                          : 2.000
producer-metrics:connection-creation-rate:{client-id=producer-1}                  : 0.040
producer-metrics:connection-creation-total:{client-id=producer-1}                 : 2.000
producer-metrics:failed-authentication-rate:{client-id=producer-1}                : 0.000
producer-metrics:failed-authentication-total:{client-id=producer-1}               : 0.000
producer-metrics:failed-reauthentication-rate:{client-id=producer-1}              : 0.000
producer-metrics:failed-reauthentication-total:{client-id=producer-1}             : 0.000
producer-metrics:incoming-byte-rate:{client-id=producer-1}                        : 19.968
producer-metrics:incoming-byte-total:{client-id=producer-1}                       : 993.000
producer-metrics:io-ratio:{client-id=producer-1}                                  : 0.006
producer-metrics:io-time-ns-avg:{client-id=producer-1}                            : 295115.191
producer-metrics:io-wait-ratio:{client-id=producer-1}                             : 0.972
producer-metrics:io-wait-time-ns-avg:{client-id=producer-1}                       : 49548726.753
producer-metrics:io-waittime-total:{client-id=producer-1}                         : 48607300945.000
producer-metrics:iotime-total:{client-id=producer-1}                              : 289508002.000
producer-metrics:metadata-age:{client-id=producer-1}                              : 49.639
producer-metrics:network-io-rate:{client-id=producer-1}                           : 9.891
producer-metrics:network-io-total:{client-id=producer-1}                          : 492.000
producer-metrics:outgoing-byte-rate:{client-id=producer-1}                        : 1177.912
producer-metrics:outgoing-byte-total:{client-id=producer-1}                       : 58587.000
producer-metrics:produce-throttle-time-avg:{client-id=producer-1}                 : 0.000
producer-metrics:produce-throttle-time-max:{client-id=producer-1}                 : 0.000
producer-metrics:reauthentication-latency-avg:{client-id=producer-1}              : NaN
producer-metrics:reauthentication-latency-max:{client-id=producer-1}              : NaN
producer-metrics:record-error-rate:{client-id=producer-1}                         : 0.000
producer-metrics:record-error-total:{client-id=producer-1}                        : 0.000
producer-metrics:record-queue-time-avg:{client-id=producer-1}                     : 0.652
producer-metrics:record-queue-time-max:{client-id=producer-1}                     : 62.000
producer-metrics:record-retry-rate:{client-id=producer-1}                         : 0.000
producer-metrics:record-retry-total:{client-id=producer-1}                        : 0.000
producer-metrics:record-send-rate:{client-id=producer-1}                          : 10.093
producer-metrics:record-send-total:{client-id=producer-1}                         : 500.000
producer-metrics:record-size-avg:{client-id=producer-1}                           : 86.000
producer-metrics:record-size-max:{client-id=producer-1}                           : 86.000
producer-metrics:records-per-request-avg:{client-id=producer-1}                   : 1.029
producer-metrics:request-latency-avg:{client-id=producer-1}                       : NaN
producer-metrics:request-latency-max:{client-id=producer-1}                       : NaN
producer-metrics:request-rate:{client-id=producer-1}                              : 9.830
producer-metrics:request-size-avg:{client-id=producer-1}                          : 119.810
producer-metrics:request-size-max:{client-id=producer-1}                          : 152.000
producer-metrics:request-total:{client-id=producer-1}                             : 489.000
producer-metrics:requests-in-flight:{client-id=producer-1}                        : 0.000
producer-metrics:response-rate:{client-id=producer-1}                             : 0.060
producer-metrics:response-total:{client-id=producer-1}                            : 3.000
producer-metrics:select-rate:{client-id=producer-1}                               : 19.626
producer-metrics:select-total:{client-id=producer-1}                              : 981.000
producer-metrics:successful-authentication-no-reauth-total:{client-id=producer-1} : 0.000
producer-metrics:successful-authentication-rate:{client-id=producer-1}            : 0.000
producer-metrics:successful-authentication-total:{client-id=producer-1}           : 0.000
producer-metrics:successful-reauthentication-rate:{client-id=producer-1}          : 0.000
producer-metrics:successful-reauthentication-total:{client-id=producer-1}         : 0.000
producer-metrics:waiting-threads:{client-id=producer-1}                           : 0.000
producer-node-metrics:incoming-byte-rate:{client-id=producer-1, node-id=node--1}  : 11.562
producer-node-metrics:incoming-byte-rate:{client-id=producer-1, node-id=node-1}   : 8.437
producer-node-metrics:incoming-byte-total:{client-id=producer-1, node-id=node--1} : 575.000
producer-node-metrics:incoming-byte-total:{client-id=producer-1, node-id=node-1}  : 418.000
producer-node-metrics:outgoing-byte-rate:{client-id=producer-1, node-id=node--1}  : 2.111
producer-node-metrics:outgoing-byte-rate:{client-id=producer-1, node-id=node-1}   : 1179.715
producer-node-metrics:outgoing-byte-total:{client-id=producer-1, node-id=node--1} : 105.000
producer-node-metrics:outgoing-byte-total:{client-id=producer-1, node-id=node-1}  : 58482.000
producer-node-metrics:request-latency-avg:{client-id=producer-1, node-id=node--1} : NaN
producer-node-metrics:request-latency-avg:{client-id=producer-1, node-id=node-1}  : NaN
producer-node-metrics:request-latency-max:{client-id=producer-1, node-id=node--1} : NaN
producer-node-metrics:request-latency-max:{client-id=producer-1, node-id=node-1}  : NaN
producer-node-metrics:request-rate:{client-id=producer-1, node-id=node--1}        : 0.040
producer-node-metrics:request-rate:{client-id=producer-1, node-id=node-1}         : 9.823
producer-node-metrics:request-size-avg:{client-id=producer-1, node-id=node--1}    : 52.500
producer-node-metrics:request-size-avg:{client-id=producer-1, node-id=node-1}     : 120.086
producer-node-metrics:request-size-max:{client-id=producer-1, node-id=node--1}    : 55.000
producer-node-metrics:request-size-max:{client-id=producer-1, node-id=node-1}     : 152.000
producer-node-metrics:request-total:{client-id=producer-1, node-id=node--1}       : 2.000
producer-node-metrics:request-total:{client-id=producer-1, node-id=node-1}        : 487.000
producer-node-metrics:response-rate:{client-id=producer-1, node-id=node--1}       : 0.040
producer-node-metrics:response-rate:{client-id=producer-1, node-id=node-1}        : 0.020
producer-node-metrics:response-total:{client-id=producer-1, node-id=node--1}      : 2.000
producer-node-metrics:response-total:{client-id=producer-1, node-id=node-1}       : 1.000
producer-topic-metrics:byte-rate:{client-id=producer-1, topic=my_topic}           : 679.168
producer-topic-metrics:byte-total:{client-id=producer-1, topic=my_topic}          : 33646.000
producer-topic-metrics:compression-rate:{client-id=producer-1, topic=my_topic}    : 1.000
producer-topic-metrics:record-error-rate:{client-id=producer-1, topic=my_topic}   : 0.000
producer-topic-metrics:record-error-total:{client-id=producer-1, topic=my_topic}  : 0.000
producer-topic-metrics:record-retry-rate:{client-id=producer-1, topic=my_topic}   : 0.000
producer-topic-metrics:record-retry-total:{client-id=producer-1, topic=my_topic}  : 0.000
producer-topic-metrics:record-send-rate:{client-id=producer-1, topic=my_topic}    : 10.093
producer-topic-metrics:record-send-total:{client-id=producer-1, topic=my_topic}   : 500.000
```
---
### At Least Once
```python
    kafka-producer-perf-test.sh --topic my_topic \
    --num-records 500 --throughput 10 --producer-props bootstrap.servers=localhost:9092 \
    key.serializer=org.apache.kafka.common.serialization.StringSerializer value.serializer=org.apache.kafka.common.serialization.StringSerializer \
    --record-size 1 --producer.config var/lib/kafka/config-properties/producer-at-least-once.properties --print-metrics 
```

#### Results
```shell
52 records sent, 10.3 records/sec (0.00 MB/sec), 15.6 ms avg latency, 384.0 ms max latency.
51 records sent, 10.0 records/sec (0.00 MB/sec), 5.5 ms avg latency, 19.0 ms max latency.
50 records sent, 10.0 records/sec (0.00 MB/sec), 6.2 ms avg latency, 14.0 ms max latency.
51 records sent, 10.0 records/sec (0.00 MB/sec), 6.1 ms avg latency, 29.0 ms max latency.
51 records sent, 10.0 records/sec (0.00 MB/sec), 5.5 ms avg latency, 27.0 ms max latency.
51 records sent, 10.0 records/sec (0.00 MB/sec), 4.6 ms avg latency, 8.0 ms max latency.
51 records sent, 10.0 records/sec (0.00 MB/sec), 5.2 ms avg latency, 27.0 ms max latency.
51 records sent, 10.0 records/sec (0.00 MB/sec), 5.7 ms avg latency, 31.0 ms max latency.
51 records sent, 10.0 records/sec (0.00 MB/sec), 4.7 ms avg latency, 11.0 ms max latency.
500 records sent, 10.017832 records/sec (0.00 MB/sec), 6.44 ms avg latency, 384.00 ms max latency, 5 ms 50th, 9 ms 95th, 36 ms 99th, 384 ms 99.9th.
```

### Metrics
```shell
Metric Name                                                                         Value
app-info:commit-id:{client-id=producer-1}                                         : 839b886f9b732b15
app-info:start-time-ms:{client-id=producer-1}                                     : 1728777590564
app-info:version:{client-id=producer-1}                                           : 2.8.1
kafka-metrics-count:count:{client-id=producer-1}                                  : 102.000
producer-metrics:batch-size-avg:{client-id=producer-1}                            : 69.230
producer-metrics:batch-size-max:{client-id=producer-1}                            : 101.000
producer-metrics:batch-split-rate:{client-id=producer-1}                          : 0.000
producer-metrics:batch-split-total:{client-id=producer-1}                         : 0.000
producer-metrics:buffer-available-bytes:{client-id=producer-1}                    : 33554432.000
producer-metrics:buffer-exhausted-rate:{client-id=producer-1}                     : 0.000
producer-metrics:buffer-exhausted-total:{client-id=producer-1}                    : 0.000
producer-metrics:buffer-total-bytes:{client-id=producer-1}                        : 33554432.000
producer-metrics:bufferpool-wait-ratio:{client-id=producer-1}                     : 0.000
producer-metrics:bufferpool-wait-time-total:{client-id=producer-1}                : 0.000
producer-metrics:compression-rate-avg:{client-id=producer-1}                      : 1.000
producer-metrics:connection-close-rate:{client-id=producer-1}                     : 0.000
producer-metrics:connection-close-total:{client-id=producer-1}                    : 0.000
producer-metrics:connection-count:{client-id=producer-1}                          : 2.000
producer-metrics:connection-creation-rate:{client-id=producer-1}                  : 0.040
producer-metrics:connection-creation-total:{client-id=producer-1}                 : 2.000
producer-metrics:failed-authentication-rate:{client-id=producer-1}                : 0.000
producer-metrics:failed-authentication-total:{client-id=producer-1}               : 0.000
producer-metrics:failed-reauthentication-rate:{client-id=producer-1}              : 0.000
producer-metrics:failed-reauthentication-total:{client-id=producer-1}             : 0.000
producer-metrics:incoming-byte-rate:{client-id=producer-1}                        : 597.102
producer-metrics:incoming-byte-total:{client-id=producer-1}                       : 29667.000
producer-metrics:io-ratio:{client-id=producer-1}                                  : 0.008
producer-metrics:io-time-ns-avg:{client-id=producer-1}                            : 268418.879
producer-metrics:io-wait-ratio:{client-id=producer-1}                             : 0.967
producer-metrics:io-wait-time-ns-avg:{client-id=producer-1}                       : 32918934.573
producer-metrics:io-waittime-total:{client-id=producer-1}                         : 48292077018.000
producer-metrics:iotime-total:{client-id=producer-1}                              : 393770495.000
producer-metrics:metadata-age:{client-id=producer-1}                              : 49.618
producer-metrics:network-io-rate:{client-id=producer-1}                           : 19.676
producer-metrics:network-io-total:{client-id=producer-1}                          : 978.000
producer-metrics:outgoing-byte-rate:{client-id=producer-1}                        : 1178.884
producer-metrics:outgoing-byte-total:{client-id=producer-1}                       : 58587.000
producer-metrics:produce-throttle-time-avg:{client-id=producer-1}                 : 0.000
producer-metrics:produce-throttle-time-max:{client-id=producer-1}                 : 0.000
producer-metrics:reauthentication-latency-avg:{client-id=producer-1}              : NaN
producer-metrics:reauthentication-latency-max:{client-id=producer-1}              : NaN
producer-metrics:record-error-rate:{client-id=producer-1}                         : 0.000
producer-metrics:record-error-total:{client-id=producer-1}                        : 0.000
producer-metrics:record-queue-time-avg:{client-id=producer-1}                     : 0.621
producer-metrics:record-queue-time-max:{client-id=producer-1}                     : 25.000
producer-metrics:record-retry-rate:{client-id=producer-1}                         : 0.000
producer-metrics:record-retry-total:{client-id=producer-1}                        : 0.000
producer-metrics:record-send-rate:{client-id=producer-1}                          : 10.088
producer-metrics:record-send-total:{client-id=producer-1}                         : 500.000
producer-metrics:record-size-avg:{client-id=producer-1}                           : 86.000
producer-metrics:record-size-max:{client-id=producer-1}                           : 86.000
producer-metrics:records-per-request-avg:{client-id=producer-1}                   : 1.029
producer-metrics:request-latency-avg:{client-id=producer-1}                       : 4.156
producer-metrics:request-latency-max:{client-id=producer-1}                       : 28.000
producer-metrics:request-rate:{client-id=producer-1}                              : 9.838
producer-metrics:request-size-avg:{client-id=producer-1}                          : 119.810
producer-metrics:request-size-max:{client-id=producer-1}                          : 152.000
producer-metrics:request-total:{client-id=producer-1}                             : 489.000
producer-metrics:requests-in-flight:{client-id=producer-1}                        : 0.000
producer-metrics:response-rate:{client-id=producer-1}                             : 9.842
producer-metrics:response-total:{client-id=producer-1}                            : 489.000
producer-metrics:select-rate:{client-id=producer-1}                               : 29.383
producer-metrics:select-total:{client-id=producer-1}                              : 1467.000
producer-metrics:successful-authentication-no-reauth-total:{client-id=producer-1} : 0.000
producer-metrics:successful-authentication-rate:{client-id=producer-1}            : 0.000
producer-metrics:successful-authentication-total:{client-id=producer-1}           : 0.000
producer-metrics:successful-reauthentication-rate:{client-id=producer-1}          : 0.000
producer-metrics:successful-reauthentication-total:{client-id=producer-1}         : 0.000
producer-metrics:waiting-threads:{client-id=producer-1}                           : 0.000
producer-node-metrics:incoming-byte-rate:{client-id=producer-1, node-id=node--1}  : 11.572
producer-node-metrics:incoming-byte-rate:{client-id=producer-1, node-id=node-1}   : 586.911
producer-node-metrics:incoming-byte-total:{client-id=producer-1, node-id=node--1} : 575.000
producer-node-metrics:incoming-byte-total:{client-id=producer-1, node-id=node-1}  : 29092.000
producer-node-metrics:outgoing-byte-rate:{client-id=producer-1, node-id=node--1}  : 2.113
producer-node-metrics:outgoing-byte-rate:{client-id=producer-1, node-id=node-1}   : 1179.596
producer-node-metrics:outgoing-byte-total:{client-id=producer-1, node-id=node--1} : 105.000
producer-node-metrics:outgoing-byte-total:{client-id=producer-1, node-id=node-1}  : 58482.000
producer-node-metrics:request-latency-avg:{client-id=producer-1, node-id=node--1} : NaN
producer-node-metrics:request-latency-avg:{client-id=producer-1, node-id=node-1}  : 4.156
producer-node-metrics:request-latency-max:{client-id=producer-1, node-id=node--1} : NaN
producer-node-metrics:request-latency-max:{client-id=producer-1, node-id=node-1}  : 28.000
producer-node-metrics:request-rate:{client-id=producer-1, node-id=node--1}        : 0.040
producer-node-metrics:request-rate:{client-id=producer-1, node-id=node-1}         : 9.823
producer-node-metrics:request-size-avg:{client-id=producer-1, node-id=node--1}    : 52.500
producer-node-metrics:request-size-avg:{client-id=producer-1, node-id=node-1}     : 120.086
producer-node-metrics:request-size-max:{client-id=producer-1, node-id=node--1}    : 55.000
producer-node-metrics:request-size-max:{client-id=producer-1, node-id=node-1}     : 152.000
producer-node-metrics:request-total:{client-id=producer-1, node-id=node--1}       : 2.000
producer-node-metrics:request-total:{client-id=producer-1, node-id=node-1}        : 487.000
producer-node-metrics:response-rate:{client-id=producer-1, node-id=node--1}       : 0.040
producer-node-metrics:response-rate:{client-id=producer-1, node-id=node-1}        : 9.825
producer-node-metrics:response-total:{client-id=producer-1, node-id=node--1}      : 2.000
producer-node-metrics:response-total:{client-id=producer-1, node-id=node-1}       : 487.000
producer-topic-metrics:byte-rate:{client-id=producer-1, topic=my_topic}           : 678.853
producer-topic-metrics:byte-total:{client-id=producer-1, topic=my_topic}          : 33646.000
producer-topic-metrics:compression-rate:{client-id=producer-1, topic=my_topic}    : 1.000
producer-topic-metrics:record-error-rate:{client-id=producer-1, topic=my_topic}   : 0.000
producer-topic-metrics:record-error-total:{client-id=producer-1, topic=my_topic}  : 0.000
producer-topic-metrics:record-retry-rate:{client-id=producer-1, topic=my_topic}   : 0.000
producer-topic-metrics:record-retry-total:{client-id=producer-1, topic=my_topic}  : 0.000
producer-topic-metrics:record-send-rate:{client-id=producer-1, topic=my_topic}    : 10.088
producer-topic-metrics:record-send-total:{client-id=producer-1, topic=my_topic}   : 500.000
```



### Exactly Once
```python
    kafka-producer-perf-test.sh --topic my_topic \
    --num-records 500 --throughput 10 --producer-props bootstrap.servers=localhost:9092 \
    key.serializer=org.apache.kafka.common.serialization.StringSerializer value.serializer=org.apache.kafka.common.serialization.StringSerializer \
    --record-size 1 --producer.config var/lib/kafka/config-properties/producer-exactly-once.properties 
```

#### Results
```shell
52 records sent, 10.2 records/sec (0.00 MB/sec), 12.9 ms avg latency, 293.0 ms max latency.
51 records sent, 10.1 records/sec (0.00 MB/sec), 5.7 ms avg latency, 22.0 ms max latency.
51 records sent, 10.0 records/sec (0.00 MB/sec), 6.1 ms avg latency, 22.0 ms max latency.
50 records sent, 9.9 records/sec (0.00 MB/sec), 6.9 ms avg latency, 32.0 ms max latency.
51 records sent, 10.1 records/sec (0.00 MB/sec), 6.0 ms avg latency, 11.0 ms max latency.
51 records sent, 10.0 records/sec (0.00 MB/sec), 4.8 ms avg latency, 8.0 ms max latency.
51 records sent, 10.0 records/sec (0.00 MB/sec), 6.2 ms avg latency, 28.0 ms max latency.
51 records sent, 10.0 records/sec (0.00 MB/sec), 5.3 ms avg latency, 13.0 ms max latency.
50 records sent, 9.8 records/sec (0.00 MB/sec), 4.6 ms avg latency, 7.0 ms max latency.
500 records sent, 10.003601 records/sec (0.00 MB/sec), 6.43 ms avg latency, 293.00 ms max latency, 6 ms 50th, 9 ms 95th, 26 ms 99th, 293 ms 99.9th.
```

### Metrics
```shell
Metric Name                                                                         Value
app-info:commit-id:{client-id=producer-1}                                         : 839b886f9b732b15
app-info:start-time-ms:{client-id=producer-1}                                     : 1728777982027
app-info:version:{client-id=producer-1}                                           : 2.8.1
kafka-metrics-count:count:{client-id=producer-1}                                  : 102.000
producer-metrics:batch-size-avg:{client-id=producer-1}                            : 69.197
producer-metrics:batch-size-max:{client-id=producer-1}                            : 93.000
producer-metrics:batch-split-rate:{client-id=producer-1}                          : 0.000
producer-metrics:batch-split-total:{client-id=producer-1}                         : 0.000
producer-metrics:buffer-available-bytes:{client-id=producer-1}                    : 33554432.000
producer-metrics:buffer-exhausted-rate:{client-id=producer-1}                     : 0.000
producer-metrics:buffer-exhausted-total:{client-id=producer-1}                    : 0.000
producer-metrics:buffer-total-bytes:{client-id=producer-1}                        : 33554432.000
producer-metrics:bufferpool-wait-ratio:{client-id=producer-1}                     : 0.000
producer-metrics:bufferpool-wait-time-total:{client-id=producer-1}                : 0.000
producer-metrics:compression-rate-avg:{client-id=producer-1}                      : 1.000
producer-metrics:connection-close-rate:{client-id=producer-1}                     : 0.000
producer-metrics:connection-close-total:{client-id=producer-1}                    : 0.000
producer-metrics:connection-count:{client-id=producer-1}                          : 2.000
producer-metrics:connection-creation-rate:{client-id=producer-1}                  : 0.040
producer-metrics:connection-creation-total:{client-id=producer-1}                 : 2.000
producer-metrics:failed-authentication-rate:{client-id=producer-1}                : 0.000
producer-metrics:failed-authentication-total:{client-id=producer-1}               : 0.000
producer-metrics:failed-reauthentication-rate:{client-id=producer-1}              : 0.000
producer-metrics:failed-reauthentication-total:{client-id=producer-1}             : 0.000
producer-metrics:incoming-byte-rate:{client-id=producer-1}                        : 598.446
producer-metrics:incoming-byte-total:{client-id=producer-1}                       : 29811.000
producer-metrics:io-ratio:{client-id=producer-1}                                  : 0.008
producer-metrics:io-time-ns-avg:{client-id=producer-1}                            : 272171.727
producer-metrics:io-wait-ratio:{client-id=producer-1}                             : 0.971
producer-metrics:io-wait-time-ns-avg:{client-id=producer-1}                       : 32807473.128
producer-metrics:io-waittime-total:{client-id=producer-1}                         : 48391022864.000
producer-metrics:iotime-total:{client-id=producer-1}                              : 401453297.000
producer-metrics:metadata-age:{client-id=producer-1}                              : 49.758
producer-metrics:network-io-rate:{client-id=producer-1}                           : 19.751
producer-metrics:network-io-total:{client-id=producer-1}                          : 984.000
producer-metrics:outgoing-byte-rate:{client-id=producer-1}                        : 1181.388
producer-metrics:outgoing-byte-total:{client-id=producer-1}                       : 58852.000
producer-metrics:produce-throttle-time-avg:{client-id=producer-1}                 : 0.000
producer-metrics:produce-throttle-time-max:{client-id=producer-1}                 : 0.000
producer-metrics:reauthentication-latency-avg:{client-id=producer-1}              : NaN
producer-metrics:reauthentication-latency-max:{client-id=producer-1}              : NaN
producer-metrics:record-error-rate:{client-id=producer-1}                         : 0.000
producer-metrics:record-error-total:{client-id=producer-1}                        : 0.000
producer-metrics:record-queue-time-avg:{client-id=producer-1}                     : 0.621
producer-metrics:record-queue-time-max:{client-id=producer-1}                     : 13.000
producer-metrics:record-retry-rate:{client-id=producer-1}                         : 0.000
producer-metrics:record-retry-total:{client-id=producer-1}                        : 0.000
producer-metrics:record-send-rate:{client-id=producer-1}                          : 10.055
producer-metrics:record-send-total:{client-id=producer-1}                         : 500.000
producer-metrics:record-size-avg:{client-id=producer-1}                           : 86.000
producer-metrics:record-size-max:{client-id=producer-1}                           : 86.000
producer-metrics:records-per-request-avg:{client-id=producer-1}                   : 1.025
producer-metrics:request-latency-avg:{client-id=producer-1}                       : 4.422
producer-metrics:request-latency-max:{client-id=producer-1}                       : 30.000
producer-metrics:request-rate:{client-id=producer-1}                              : 9.875
producer-metrics:request-size-avg:{client-id=producer-1}                          : 119.618
producer-metrics:request-size-max:{client-id=producer-1}                          : 144.000
producer-metrics:request-total:{client-id=producer-1}                             : 492.000
producer-metrics:requests-in-flight:{client-id=producer-1}                        : 0.000
producer-metrics:response-rate:{client-id=producer-1}                             : 9.877
producer-metrics:response-total:{client-id=producer-1}                            : 492.000
producer-metrics:select-rate:{client-id=producer-1}                               : 29.591
producer-metrics:select-total:{client-id=producer-1}                              : 1475.000
producer-metrics:successful-authentication-no-reauth-total:{client-id=producer-1} : 0.000
producer-metrics:successful-authentication-rate:{client-id=producer-1}            : 0.000
producer-metrics:successful-authentication-total:{client-id=producer-1}           : 0.000
producer-metrics:successful-reauthentication-rate:{client-id=producer-1}          : 0.000
producer-metrics:successful-reauthentication-total:{client-id=producer-1}         : 0.000
producer-metrics:waiting-threads:{client-id=producer-1}                           : 0.000
producer-node-metrics:incoming-byte-rate:{client-id=producer-1, node-id=node--1}  : 12.065
producer-node-metrics:incoming-byte-rate:{client-id=producer-1, node-id=node-1}   : 587.336
producer-node-metrics:incoming-byte-total:{client-id=producer-1, node-id=node--1} : 601.000
producer-node-metrics:incoming-byte-total:{client-id=producer-1, node-id=node-1}  : 29210.000
producer-node-metrics:outgoing-byte-rate:{client-id=producer-1, node-id=node--1}  : 2.931
producer-node-metrics:outgoing-byte-rate:{client-id=producer-1, node-id=node-1}   : 1180.400
producer-node-metrics:outgoing-byte-total:{client-id=producer-1, node-id=node--1} : 146.000
producer-node-metrics:outgoing-byte-total:{client-id=producer-1, node-id=node-1}  : 58706.000
producer-node-metrics:request-latency-avg:{client-id=producer-1, node-id=node--1} : NaN
producer-node-metrics:request-latency-avg:{client-id=producer-1, node-id=node-1}  : 4.422
producer-node-metrics:request-latency-max:{client-id=producer-1, node-id=node--1} : NaN
producer-node-metrics:request-latency-max:{client-id=producer-1, node-id=node-1}  : 30.000
producer-node-metrics:request-rate:{client-id=producer-1, node-id=node--1}        : 0.060
producer-node-metrics:request-rate:{client-id=producer-1, node-id=node-1}         : 9.832
producer-node-metrics:request-size-avg:{client-id=producer-1, node-id=node--1}    : 48.667
producer-node-metrics:request-size-avg:{client-id=producer-1, node-id=node-1}     : 120.053
producer-node-metrics:request-size-max:{client-id=producer-1, node-id=node--1}    : 55.000
producer-node-metrics:request-size-max:{client-id=producer-1, node-id=node-1}     : 144.000
producer-node-metrics:request-total:{client-id=producer-1, node-id=node--1}       : 3.000
producer-node-metrics:request-total:{client-id=producer-1, node-id=node-1}        : 489.000
producer-node-metrics:response-rate:{client-id=producer-1, node-id=node--1}       : 0.060
producer-node-metrics:response-rate:{client-id=producer-1, node-id=node-1}        : 9.833
producer-node-metrics:response-total:{client-id=producer-1, node-id=node--1}      : 3.000
producer-node-metrics:response-total:{client-id=producer-1, node-id=node-1}       : 489.000
producer-topic-metrics:byte-rate:{client-id=producer-1, topic=my_topic}           : 679.068
producer-topic-metrics:byte-total:{client-id=producer-1, topic=my_topic}          : 33768.000
producer-topic-metrics:compression-rate:{client-id=producer-1, topic=my_topic}    : 1.000
producer-topic-metrics:record-error-rate:{client-id=producer-1, topic=my_topic}   : 0.000
producer-topic-metrics:record-error-total:{client-id=producer-1, topic=my_topic}  : 0.000
producer-topic-metrics:record-retry-rate:{client-id=producer-1, topic=my_topic}   : 0.000
producer-topic-metrics:record-retry-total:{client-id=producer-1, topic=my_topic}  : 0.000
producer-topic-metrics:record-send-rate:{client-id=producer-1, topic=my_topic}    : 10.055
producer-topic-metrics:record-send-total:{client-id=producer-1, topic=my_topic}   : 500.000
```


