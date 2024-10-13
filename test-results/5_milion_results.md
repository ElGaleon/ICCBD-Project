# Producer Tests
## Message Delivery Comparison: At Most Once vs At Least Once vs Exactly Once
#### 5000000 messages sent to a topic with 16 partitions and 3 replicas
##### Tests done on 13th October 2024

### Create Topic Test
```shell
$ bin/kafka-topics.sh \
--create \
--topic test-topic\
--partitions 1 \
--replication-factor 1 \
--bootstrap-server localhost:9092
```

### At Most Once
```shell
        kafka-producer-perf-test.sh \
        --topic test-topic \
        --throughput 100000 \
        --num-records 5000000 \
        --record-size 2048 \
        --producer-props bootstrap.servers=localhost:9092 \
        --producer.config var/lib/kafka/config-properties/producer-at-most-once.properties --print-metrics 
```

#### Results
```shell
196218 records sent, 39243.6 records/sec (76.65 MB/sec), 319.5 ms avg latency, 646.0 ms max latency.
309652 records sent, 61930.4 records/sec (120.96 MB/sec), 232.7 ms avg latency, 358.0 ms max latency.
314790 records sent, 62958.0 records/sec (122.96 MB/sec), 226.7 ms avg latency, 290.0 ms max latency.
306579 records sent, 61315.8 records/sec (119.76 MB/sec), 234.1 ms avg latency, 315.0 ms max latency.
359527 records sent, 71905.4 records/sec (140.44 MB/sec), 199.2 ms avg latency, 295.0 ms max latency.
323750 records sent, 64737.1 records/sec (126.44 MB/sec), 221.5 ms avg latency, 281.0 ms max latency.
348978 records sent, 69795.6 records/sec (136.32 MB/sec), 205.7 ms avg latency, 256.0 ms max latency.
348565 records sent, 69713.0 records/sec (136.16 MB/sec), 206.2 ms avg latency, 265.0 ms max latency.
337421 records sent, 67484.2 records/sec (131.81 MB/sec), 211.3 ms avg latency, 271.0 ms max latency.
343378 records sent, 68661.9 records/sec (134.11 MB/sec), 209.7 ms avg latency, 284.0 ms max latency.
349251 records sent, 69850.2 records/sec (136.43 MB/sec), 205.6 ms avg latency, 235.0 ms max latency.
353787 records sent, 70757.4 records/sec (138.20 MB/sec), 202.5 ms avg latency, 257.0 ms max latency.
357161 records sent, 71432.2 records/sec (139.52 MB/sec), 200.7 ms avg latency, 240.0 ms max latency.
354823 records sent, 70964.6 records/sec (138.60 MB/sec), 202.0 ms avg latency, 244.0 ms max latency.
348964 records sent, [Dockerfile](Dockerfile)69792.8 records/sec (136.31 MB/sec), 205.1 ms avg latency, 251.0 ms max latency.

5000000 records sent, 66076.384300 records/sec (129.06 MB/sec), 215.22 ms avg latency, 646.00 ms max latency, 207 ms 50th, 264 ms 95th, 397 ms 99th, 604 ms 99.9th.
```

### Metrics
```shell
Metric Name                                                                          Value
app-info:commit-id:{client-id=producer-1}                                          : 839b886f9b732b15
app-info:start-time-ms:{client-id=producer-1}                                      : 1728857668786
app-info:version:{client-id=producer-1}                                            : 2.8.1
kafka-metrics-count:count:{client-id=producer-1}                                   : 102.000
producer-metrics:batch-size-avg:{client-id=producer-1}                             : 14459.991
producer-metrics:batch-size-max:{client-id=producer-1}                             : 14460.000
producer-metrics:batch-split-rate:{client-id=producer-1}                           : 0.000
producer-metrics:batch-split-total:{client-id=producer-1}                          : 0.000
producer-metrics:buffer-available-bytes:{client-id=producer-1}                     : 33554432.000
producer-metrics:buffer-exhausted-rate:{client-id=producer-1}                      : 0.000
producer-metrics:buffer-exhausted-total:{client-id=producer-1}                     : 0.000
producer-metrics:buffer-total-bytes:{client-id=producer-1}                         : 33554432.000
producer-metrics:bufferpool-wait-ratio:{client-id=producer-1}                      : 0.845
producer-metrics:bufferpool-wait-time-total:{client-id=producer-1}                 : 63590012988.000
producer-metrics:compression-rate-avg:{client-id=producer-1}                       : 1.000
producer-metrics:connection-close-rate:{client-id=producer-1}                      : 0.000
producer-metrics:connection-close-total:{client-id=producer-1}                     : 0.000
producer-metrics:connection-count:{client-id=producer-1}                           : 2.000
producer-metrics:connection-creation-rate:{client-id=producer-1}                   : 0.000
producer-metrics:connection-creation-total:{client-id=producer-1}                  : 2.000
producer-metrics:failed-authentication-rate:{client-id=producer-1}                 : 0.000
producer-metrics:failed-authentication-total:{client-id=producer-1}                : 0.000
producer-metrics:failed-reauthentication-rate:{client-id=producer-1}               : 0.000
producer-metrics:failed-reauthentication-total:{client-id=producer-1}              : 0.000
producer-metrics:incoming-byte-rate:{client-id=producer-1}                         : 0.000
producer-metrics:incoming-byte-total:{client-id=producer-1}                        : 977.000
producer-metrics:io-ratio:{client-id=producer-1}                                   : 0.138
producer-metrics:io-time-ns-avg:{client-id=producer-1}                             : 9667.027
producer-metrics:io-wait-ratio:{client-id=producer-1}                              : 0.674
producer-metrics:io-wait-time-ns-avg:{client-id=producer-1}                        : 47231.752
producer-metrics:io-waittime-total:{client-id=producer-1}                          : 49820043143.000
producer-metrics:iotime-total:{client-id=producer-1}                               : 10530278442.000
producer-metrics:metadata-age:{client-id=producer-1}                               : 75.371
producer-metrics:network-io-rate:{client-id=producer-1}                            : 9977.051
producer-metrics:network-io-total:{client-id=producer-1}                           : 714292.000
producer-metrics:outgoing-byte-rate:{client-id=producer-1}                         : 144819576.279
producer-metrics:outgoing-byte-total:{client-id=producer-1}                        : 10367143047.000
producer-metrics:produce-throttle-time-avg:{client-id=producer-1}                  : NaN
producer-metrics:produce-throttle-time-max:{client-id=producer-1}                  : NaN
producer-metrics:reauthentication-latency-avg:{client-id=producer-1}               : NaN
producer-metrics:reauthentication-latency-max:{client-id=producer-1}               : NaN
producer-metrics:record-error-rate:{client-id=producer-1}                          : 0.000
producer-metrics:record-error-total:{client-id=producer-1}                         : 0.000
producer-metrics:record-queue-time-avg:{client-id=producer-1}                      : 205.007
producer-metrics:record-queue-time-max:{client-id=producer-1}                      : 284.000
producer-metrics:record-retry-rate:{client-id=producer-1}                          : 0.000
producer-metrics:record-retry-total:{client-id=producer-1}                         : 0.000
producer-metrics:record-send-rate:{client-id=producer-1}                           : 69843.027
producer-metrics:record-send-total:{client-id=producer-1}                          : 5000000.000
producer-metrics:record-size-avg:{client-id=producer-1}                            : 2134.000
producer-metrics:record-size-max:{client-id=producer-1}                            : 2134.000
producer-metrics:records-per-request-avg:{client-id=producer-1}                    : 7.000
producer-metrics:request-latency-avg:{client-id=producer-1}                        : NaN
producer-metrics:request-latency-max:{client-id=producer-1}                        : NaN
producer-metrics:request-rate:{client-id=producer-1}                               : 9977.271
producer-metrics:request-size-avg:{client-id=producer-1}                           : 14513.991
producer-metrics:request-size-max:{client-id=producer-1}                           : 14514.000
producer-metrics:request-total:{client-id=producer-1}                              : 714289.000
producer-metrics:requests-in-flight:{client-id=producer-1}                         : 0.000
producer-metrics:response-rate:{client-id=producer-1}                              : 0.000
producer-metrics:response-total:{client-id=producer-1}                             : 3.000
producer-metrics:select-rate:{client-id=producer-1}                                : 14270.509
producer-metrics:select-total:{client-id=producer-1}                               : 1011603.000
producer-metrics:successful-authentication-no-reauth-total:{client-id=producer-1}  : 0.000
producer-metrics:successful-authentication-rate:{client-id=producer-1}             : 0.000
producer-metrics:successful-authentication-total:{client-id=producer-1}            : 0.000
producer-metrics:successful-reauthentication-rate:{client-id=producer-1}           : 0.000
producer-metrics:successful-reauthentication-total:{client-id=producer-1}          : 0.000
producer-metrics:waiting-threads:{client-id=producer-1}                            : 0.000
producer-node-metrics:incoming-byte-rate:{client-id=producer-1, node-id=node--1}   : 0.000
producer-node-metrics:incoming-byte-rate:{client-id=producer-1, node-id=node-1}    : 0.000
producer-node-metrics:incoming-byte-total:{client-id=producer-1, node-id=node--1}  : 559.000
producer-node-metrics:incoming-byte-total:{client-id=producer-1, node-id=node-1}   : 418.000
producer-node-metrics:outgoing-byte-rate:{client-id=producer-1, node-id=node--1}   : 0.000
producer-node-metrics:outgoing-byte-rate:{client-id=producer-1, node-id=node-1}    : 144830358.359
producer-node-metrics:outgoing-byte-total:{client-id=producer-1, node-id=node--1}  : 107.000
producer-node-metrics:outgoing-byte-total:{client-id=producer-1, node-id=node-1}   : 10367142940.000
producer-node-metrics:request-latency-avg:{client-id=producer-1, node-id=node--1}  : NaN
producer-node-metrics:request-latency-avg:{client-id=producer-1, node-id=node-1}   : NaN
producer-node-metrics:request-latency-max:{client-id=producer-1, node-id=node--1}  : NaN
producer-node-metrics:request-latency-max:{client-id=producer-1, node-id=node-1}   : NaN
producer-node-metrics:request-rate:{client-id=producer-1, node-id=node--1}         : 0.000
producer-node-metrics:request-rate:{client-id=producer-1, node-id=node-1}          : 9978.452
producer-node-metrics:request-size-avg:{client-id=producer-1, node-id=node--1}     : NaN
producer-node-metrics:request-size-avg:{client-id=producer-1, node-id=node-1}      : 14513.991
producer-node-metrics:request-size-max:{client-id=producer-1, node-id=node--1}     : NaN
producer-node-metrics:request-size-max:{client-id=producer-1, node-id=node-1}      : 14514.000
producer-node-metrics:request-total:{client-id=producer-1, node-id=node--1}        : 2.000
producer-node-metrics:request-total:{client-id=producer-1, node-id=node-1}         : 714287.000
producer-node-metrics:response-rate:{client-id=producer-1, node-id=node--1}        : 0.000
producer-node-metrics:response-rate:{client-id=producer-1, node-id=node-1}         : 0.000
producer-node-metrics:response-total:{client-id=producer-1, node-id=node--1}       : 2.000
producer-node-metrics:response-total:{client-id=producer-1, node-id=node-1}        : 1.000
producer-topic-metrics:byte-rate:{client-id=producer-1, topic=test-topic}          : 144276037.381
producer-topic-metrics:byte-total:{client-id=producer-1, topic=test-topic}         : 10328571446.000
producer-topic-metrics:compression-rate:{client-id=producer-1, topic=test-topic}   : 1.000
producer-topic-metrics:record-error-rate:{client-id=producer-1, topic=test-topic}  : 0.000
producer-topic-metrics:record-error-total:{client-id=producer-1, topic=test-topic} : 0.000
producer-topic-metrics:record-retry-rate:{client-id=producer-1, topic=test-topic}  : 0.000
producer-topic-metrics:record-retry-total:{client-id=producer-1, topic=test-topic} : 0.000
producer-topic-metrics:record-send-rate:{client-id=producer-1, topic=test-topic}   : 69844.713
producer-topic-metrics:record-send-total:{client-id=producer-1, topic=test-topic}  : 5000000.000

```
---
### At Least Once
```shell
        kafka-producer-perf-test.sh \
        --topic test-topic \
        --throughput 100000 \
        --num-records 5000000 \
        --record-size 2048 \
        --producer-props bootstrap.servers=localhost:9092 \
        --producer.config var/lib/kafka/config-properties/producer-at-least-once.properties --print-metrics 
```

#### Results
```shell
182911 records sent, 36582.2 records/sec (71.45 MB/sec), 347.8 ms avg latency, 634.0 ms max latency.
243481 records sent, 48696.2 records/sec (95.11 MB/sec), 295.4 ms avg latency, 452.0 ms max latency.
288239 records sent, 57647.8 records/sec (112.59 MB/sec), 250.4 ms avg latency, 298.0 ms max latency.
283913 records sent, 56782.6 records/sec (110.90 MB/sec), 250.9 ms avg latency, 312.0 ms max latency.
280476 records sent, 56095.2 records/sec (109.56 MB/sec), 256.3 ms avg latency, 325.0 ms max latency.
281029 records sent, 56205.8 records/sec (109.78 MB/sec), 253.0 ms avg latency, 302.0 ms max latency.
275835 records sent, 55167.0 records/sec (107.75 MB/sec), 262.2 ms avg latency, 336.0 ms max latency.
277557 records sent, 55511.4 records/sec (108.42 MB/sec), 256.7 ms avg latency, 317.0 ms max latency.
278026 records sent, 55605.2 records/sec (108.60 MB/sec), 259.1 ms avg latency, 345.0 ms max latency.
270060 records sent, 54012.0 records/sec (105.49 MB/sec), 264.8 ms avg latency, 347.0 ms max latency.
287672 records sent, 57534.4 records/sec (112.37 MB/sec), 249.6 ms avg latency, 295.0 ms max latency.
273399 records sent, 54679.8 records/sec (106.80 MB/sec), 261.9 ms avg latency, 320.0 ms max latency.
279699 records sent, 55939.8 records/sec (109.26 MB/sec), 255.7 ms avg latency, 345.0 ms max latency.
294098 records sent, 58819.6 records/sec (114.88 MB/sec), 245.1 ms avg latency, 365.0 ms max latency.
287364 records sent, 57472.8 records/sec (112.25 MB/sec), 249.8 ms avg latency, 298.0 ms max latency.
274617 records sent, 54923.4 records/sec (107.27 MB/sec), 259.1 ms avg latency, 330.0 ms max latency.
266700 records sent, 53222.9 records/sec (103.95 MB/sec), 269.3 ms avg latency, 348.0 ms max latency.
275856 records sent, 55171.2 records/sec (107.76 MB/sec), 260.6 ms avg latency, 317.0 ms max latency.

5000000 records sent, 54450.809139 records/sec (106.35 MB/sec), 261.66 ms avg latency, 634.00 ms max latency, 257 ms 50th, 318 ms 95th, 411 ms 99th, 561 ms 99.9th.
```

### Metrics
```shell
Metric Name                                                                          Value
app-info:commit-id:{client-id=producer-1}                                          : 839b886f9b732b15
app-info:start-time-ms:{client-id=producer-1}                                      : 1728857834195
app-info:version:{client-id=producer-1}                                            : 2.8.1
kafka-metrics-count:count:{client-id=producer-1}                                   : 102.000
producer-metrics:batch-size-avg:{client-id=producer-1}                             : 14459.984
producer-metrics:batch-size-max:{client-id=producer-1}                             : 14460.000
producer-metrics:batch-split-rate:{client-id=producer-1}                           : 0.000
producer-metrics:batch-split-total:{client-id=producer-1}                          : 0.000
producer-metrics:buffer-available-bytes:{client-id=producer-1}                     : 33554432.000
producer-metrics:buffer-exhausted-rate:{client-id=producer-1}                      : 0.000
producer-metrics:buffer-exhausted-total:{client-id=producer-1}                     : 0.000
producer-metrics:buffer-total-bytes:{client-id=producer-1}                         : 33554432.000
producer-metrics:bufferpool-wait-ratio:{client-id=producer-1}                      : 0.855
producer-metrics:bufferpool-wait-time-total:{client-id=producer-1}                 : 78536568665.000
producer-metrics:compression-rate-avg:{client-id=producer-1}                       : 1.000
producer-metrics:connection-close-rate:{client-id=producer-1}                      : 0.000
producer-metrics:connection-close-total:{client-id=producer-1}                     : 0.000
producer-metrics:connection-count:{client-id=producer-1}                           : 2.000
producer-metrics:connection-creation-rate:{client-id=producer-1}                   : 0.000
producer-metrics:connection-creation-total:{client-id=producer-1}                  : 2.000
producer-metrics:failed-authentication-rate:{client-id=producer-1}                 : 0.000
producer-metrics:failed-authentication-total:{client-id=producer-1}                : 0.000
producer-metrics:failed-reauthentication-rate:{client-id=producer-1}               : 0.000
producer-metrics:failed-reauthentication-total:{client-id=producer-1}              : 0.000
producer-metrics:incoming-byte-rate:{client-id=producer-1}                         : 486427.149
producer-metrics:incoming-byte-total:{client-id=producer-1}                        : 43572423.000
producer-metrics:io-ratio:{client-id=producer-1}                                   : 0.258
producer-metrics:io-time-ns-avg:{client-id=producer-1}                             : 10939.336
producer-metrics:io-wait-ratio:{client-id=producer-1}                              : 0.526
producer-metrics:io-wait-time-ns-avg:{client-id=producer-1}                        : 22272.806
producer-metrics:io-waittime-total:{client-id=producer-1}                          : 45945706189.000
producer-metrics:iotime-total:{client-id=producer-1}                               : 24430603556.000
producer-metrics:metadata-age:{client-id=producer-1}                               : 91.593
producer-metrics:network-io-rate:{client-id=producer-1}                            : 15947.837
producer-metrics:network-io-total:{client-id=producer-1}                           : 1428578.000
producer-metrics:outgoing-byte-rate:{client-id=producer-1}                         : 115743149.836
producer-metrics:outgoing-byte-total:{client-id=producer-1}                        : 10367143047.000
producer-metrics:produce-throttle-time-avg:{client-id=producer-1}                  : 0.000
producer-metrics:produce-throttle-time-max:{client-id=producer-1}                  : 0.000
producer-metrics:reauthentication-latency-avg:{client-id=producer-1}               : NaN
producer-metrics:reauthentication-latency-max:{client-id=producer-1}               : NaN
producer-metrics:record-error-rate:{client-id=producer-1}                          : 0.000
producer-metrics:record-error-total:{client-id=producer-1}                         : 0.000
producer-metrics:record-queue-time-avg:{client-id=producer-1}                      : 255.788
producer-metrics:record-queue-time-max:{client-id=producer-1}                      : 364.000
producer-metrics:record-retry-rate:{client-id=producer-1}                          : 0.000
producer-metrics:record-retry-total:{client-id=producer-1}                         : 0.000
producer-metrics:record-send-rate:{client-id=producer-1}                           : 55805.998
producer-metrics:record-send-total:{client-id=producer-1}                          : 5000000.000
producer-metrics:record-size-avg:{client-id=producer-1}                            : 2134.000
producer-metrics:record-size-max:{client-id=producer-1}                            : 2134.000
producer-metrics:records-per-request-avg:{client-id=producer-1}                    : 7.000
producer-metrics:request-latency-avg:{client-id=producer-1}                        : 0.618
producer-metrics:request-latency-max:{client-id=producer-1}                        : 28.000
producer-metrics:request-rate:{client-id=producer-1}                               : 7973.840
producer-metrics:request-size-avg:{client-id=producer-1}                           : 14513.984
producer-metrics:request-size-max:{client-id=producer-1}                           : 14514.000
producer-metrics:request-total:{client-id=producer-1}                              : 714289.000
producer-metrics:requests-in-flight:{client-id=producer-1}                         : 0.000
producer-metrics:response-rate:{client-id=producer-1}                              : 7974.216
producer-metrics:response-total:{client-id=producer-1}                             : 714289.000
producer-metrics:select-rate:{client-id=producer-1}                                : 23602.053
producer-metrics:select-total:{client-id=producer-1}                               : 2054140.000
producer-metrics:successful-authentication-no-reauth-total:{client-id=producer-1}  : 0.000
producer-metrics:successful-authentication-rate:{client-id=producer-1}             : 0.000
producer-metrics:successful-authentication-total:{client-id=producer-1}            : 0.000
producer-metrics:successful-reauthentication-rate:{client-id=producer-1}           : 0.000
producer-metrics:successful-reauthentication-total:{client-id=producer-1}          : 0.000
producer-metrics:waiting-threads:{client-id=producer-1}                            : 0.000
producer-node-metrics:incoming-byte-rate:{client-id=producer-1, node-id=node--1}   : 0.000
producer-node-metrics:incoming-byte-rate:{client-id=producer-1, node-id=node-1}    : 486325.748
producer-node-metrics:incoming-byte-total:{client-id=producer-1, node-id=node--1}  : 559.000
producer-node-metrics:incoming-byte-total:{client-id=producer-1, node-id=node-1}   : 43571864.000
producer-node-metrics:outgoing-byte-rate:{client-id=producer-1, node-id=node--1}   : 0.000
producer-node-metrics:outgoing-byte-rate:{client-id=producer-1, node-id=node-1}    : 115716727.434
producer-node-metrics:outgoing-byte-total:{client-id=producer-1, node-id=node--1}  : 107.000
producer-node-metrics:outgoing-byte-total:{client-id=producer-1, node-id=node-1}   : 10367142940.000
producer-node-metrics:request-latency-avg:{client-id=producer-1, node-id=node--1}  : NaN
producer-node-metrics:request-latency-avg:{client-id=producer-1, node-id=node-1}   : 0.618
producer-node-metrics:request-latency-max:{client-id=producer-1, node-id=node--1}  : NaN
producer-node-metrics:request-latency-max:{client-id=producer-1, node-id=node-1}   : 28.000
producer-node-metrics:request-rate:{client-id=producer-1, node-id=node--1}         : 0.000
producer-node-metrics:request-rate:{client-id=producer-1, node-id=node-1}          : 7972.522
producer-node-metrics:request-size-avg:{client-id=producer-1, node-id=node--1}     : NaN
producer-node-metrics:request-size-avg:{client-id=producer-1, node-id=node-1}      : 14513.984
producer-node-metrics:request-size-max:{client-id=producer-1, node-id=node--1}     : NaN
producer-node-metrics:request-size-max:{client-id=producer-1, node-id=node-1}      : 14514.000
producer-node-metrics:request-total:{client-id=producer-1, node-id=node--1}        : 2.000
producer-node-metrics:request-total:{client-id=producer-1, node-id=node-1}         : 714287.000
producer-node-metrics:response-rate:{client-id=producer-1, node-id=node--1}        : 0.000
producer-node-metrics:response-rate:{client-id=producer-1, node-id=node-1}         : 7972.553
producer-node-metrics:response-total:{client-id=producer-1, node-id=node--1}       : 2.000
producer-node-metrics:response-total:{client-id=producer-1, node-id=node-1}        : 714287.000
producer-topic-metrics:byte-rate:{client-id=producer-1, topic=test-topic}          : 115270983.230
producer-topic-metrics:byte-total:{client-id=producer-1, topic=test-topic}         : 10328571446.000
producer-topic-metrics:compression-rate:{client-id=producer-1, topic=test-topic}   : 1.000
producer-topic-metrics:record-error-rate:{client-id=producer-1, topic=test-topic}  : 0.000
producer-topic-metrics:record-error-total:{client-id=producer-1, topic=test-topic} : 0.000
producer-topic-metrics:record-retry-rate:{client-id=producer-1, topic=test-topic}  : 0.000
producer-topic-metrics:record-retry-total:{client-id=producer-1, topic=test-topic} : 0.000
producer-topic-metrics:record-send-rate:{client-id=producer-1, topic=test-topic}   : 55803.766
producer-topic-metrics:record-send-total:{client-id=producer-1, topic=test-topic}  : 5000000.000
```



### Exactly Once
```shell
        kafka-producer-perf-test.sh \
        --topic test-topic \
        --throughput 100000 \
        --num-records 5000000 \
        --record-size 2048 \
        --producer-props bootstrap.servers=localhost:9092 \
        --producer.config var/lib/kafka/config-properties/producer-exactly-once.properties --print-metrics 
```

#### Results
```shell
176065 records sent, 35213.0 records/sec (68.78 MB/sec), 362.4 ms avg latency, 699.0 ms max latency.
267386 records sent, 53477.2 records/sec (104.45 MB/sec), 266.3 ms avg latency, 315.0 ms max latency.
251902 records sent, 50380.4 records/sec (98.40 MB/sec), 286.8 ms avg latency, 342.0 ms max latency.
267323 records sent, 53464.6 records/sec (104.42 MB/sec), 268.2 ms avg latency, 327.0 ms max latency.
266196 records sent, 53239.2 records/sec (103.98 MB/sec), 267.9 ms avg latency, 318.0 ms max latency.
279986 records sent, 55997.2 records/sec (109.37 MB/sec), 256.2 ms avg latency, 314.0 ms max latency.
256207 records sent, 51241.4 records/sec (100.08 MB/sec), 280.4 ms avg latency, 319.0 ms max latency.
272482 records sent, 54496.4 records/sec (106.44 MB/sec), 264.2 ms avg latency, 323.0 ms max latency.
262955 records sent, 52591.0 records/sec (102.72 MB/sec), 271.5 ms avg latency, 366.0 ms max latency.
277718 records sent, 55543.6 records/sec (108.48 MB/sec), 258.1 ms avg latency, 332.0 ms max latency.
266679 records sent, 53335.8 records/sec (104.17 MB/sec), 268.2 ms avg latency, 348.0 ms max latency.
272237 records sent, 54447.4 records/sec (106.34 MB/sec), 263.7 ms avg latency, 326.0 ms max latency.
264901 records sent, 52980.2 records/sec (103.48 MB/sec), 269.7 ms avg latency, 318.0 ms max latency.
268723 records sent, 53744.6 records/sec (104.97 MB/sec), 266.8 ms avg latency, 347.0 ms max latency.
255507 records sent, 51101.4 records/sec (99.81 MB/sec), 282.0 ms avg latency, 341.0 ms max latency.
269507 records sent, 53901.4 records/sec (105.28 MB/sec), 265.8 ms avg latency, 322.0 ms max latency.
251412 records sent, 50282.4 records/sec (98.21 MB/sec), 285.5 ms avg latency, 350.0 ms max latency.
268114 records sent, 53622.8 records/sec (104.73 MB/sec), 266.1 ms avg latency, 352.0 ms max latency.
265979 records sent, 53195.8 records/sec (103.90 MB/sec), 270.9 ms avg latency, 314.0 ms max latency.

5000000 records sent, 52206.780617 records/sec (101.97 MB/sec), 272.98 ms avg latency, 699.00 ms max latency, 270 ms 50th, 317 ms 95th, 433 ms 99th, 607 ms 99.9th.
```

### Metrics
```shell
Metric Name                                                                          Value
app-info:commit-id:{client-id=producer-1}                                          : 839b886f9b732b15
app-info:start-time-ms:{client-id=producer-1}                                      : 1728858005076
app-info:version:{client-id=producer-1}                                            : 2.8.1
kafka-metrics-count:count:{client-id=producer-1}                                   : 102.000
producer-metrics:batch-size-avg:{client-id=producer-1}                             : 14459.985
producer-metrics:batch-size-max:{client-id=producer-1}                             : 14460.000
producer-metrics:batch-split-rate:{client-id=producer-1}                           : 0.000
producer-metrics:batch-split-total:{client-id=producer-1}                          : 0.000
producer-metrics:buffer-available-bytes:{client-id=producer-1}                     : 33554432.000
producer-metrics:buffer-exhausted-rate:{client-id=producer-1}                      : 0.000
producer-metrics:buffer-exhausted-total:{client-id=producer-1}                     : 0.000
producer-metrics:buffer-total-bytes:{client-id=producer-1}                         : 33554432.000
producer-metrics:bufferpool-wait-ratio:{client-id=producer-1}                      : 0.854
producer-metrics:bufferpool-wait-time-total:{client-id=producer-1}                 : 81704066328.000
producer-metrics:compression-rate-avg:{client-id=producer-1}                       : 1.000
producer-metrics:connection-close-rate:{client-id=producer-1}                      : 0.000
producer-metrics:connection-close-total:{client-id=producer-1}                     : 0.000
producer-metrics:connection-count:{client-id=producer-1}                           : 2.000
producer-metrics:connection-creation-rate:{client-id=producer-1}                   : 0.000
producer-metrics:connection-creation-total:{client-id=producer-1}                  : 2.000
producer-metrics:failed-authentication-rate:{client-id=producer-1}                 : 0.000
producer-metrics:failed-authentication-total:{client-id=producer-1}                : 0.000
producer-metrics:failed-reauthentication-rate:{client-id=producer-1}               : 0.000
producer-metrics:failed-reauthentication-total:{client-id=producer-1}              : 0.000
producer-metrics:incoming-byte-rate:{client-id=producer-1}                         : 458037.283
producer-metrics:incoming-byte-total:{client-id=producer-1}                        : 43572449.000
producer-metrics:io-ratio:{client-id=producer-1}                                   : 0.251
producer-metrics:io-time-ns-avg:{client-id=producer-1}                             : 11889.653
producer-metrics:io-wait-ratio:{client-id=producer-1}                              : 0.513
producer-metrics:io-wait-time-ns-avg:{client-id=producer-1}                        : 24255.487
producer-metrics:io-waittime-total:{client-id=producer-1}                          : 47717767444.000
producer-metrics:iotime-total:{client-id=producer-1}                               : 24212219746.000
producer-metrics:metadata-age:{client-id=producer-1}                               : 95.524
producer-metrics:network-io-rate:{client-id=producer-1}                            : 15016.940
producer-metrics:network-io-total:{client-id=producer-1}                           : 1428580.000
producer-metrics:outgoing-byte-rate:{client-id=producer-1}                         : 108982922.740
producer-metrics:outgoing-byte-total:{client-id=producer-1}                        : 10367143088.000
producer-metrics:produce-throttle-time-avg:{client-id=producer-1}                  : 0.000
producer-metrics:produce-throttle-time-max:{client-id=producer-1}                  : 0.000
producer-metrics:reauthentication-latency-avg:{client-id=producer-1}               : NaN
producer-metrics:reauthentication-latency-max:{client-id=producer-1}               : NaN
producer-metrics:record-error-rate:{client-id=producer-1}                          : 0.000
producer-metrics:record-error-total:{client-id=producer-1}                         : 0.000
producer-metrics:record-queue-time-avg:{client-id=producer-1}                      : 271.821
producer-metrics:record-queue-time-max:{client-id=producer-1}                      : 352.000
producer-metrics:record-retry-rate:{client-id=producer-1}                          : 0.000
producer-metrics:record-retry-total:{client-id=producer-1}                         : 0.000
producer-metrics:record-send-rate:{client-id=producer-1}                           : 52554.879
producer-metrics:record-send-total:{client-id=producer-1}                          : 5000000.000
producer-metrics:record-size-avg:{client-id=producer-1}                            : 2134.000
producer-metrics:record-size-max:{client-id=producer-1}                            : 2134.000
producer-metrics:records-per-request-avg:{client-id=producer-1}                    : 7.000
producer-metrics:request-latency-avg:{client-id=producer-1}                        : 0.656
producer-metrics:request-latency-max:{client-id=producer-1}                        : 19.000
producer-metrics:request-rate:{client-id=producer-1}                               : 7508.400
producer-metrics:request-size-avg:{client-id=producer-1}                           : 14513.985
producer-metrics:request-size-max:{client-id=producer-1}                           : 14514.000
producer-metrics:request-total:{client-id=producer-1}                              : 714290.000
producer-metrics:requests-in-flight:{client-id=producer-1}                         : 0.000
producer-metrics:response-rate:{client-id=producer-1}                              : 7508.808
producer-metrics:response-total:{client-id=producer-1}                             : 714290.000
producer-metrics:select-rate:{client-id=producer-1}                                : 21131.507
producer-metrics:select-total:{client-id=producer-1}                               : 1992717.000
producer-metrics:successful-authentication-no-reauth-total:{client-id=producer-1}  : 0.000
producer-metrics:successful-authentication-rate:{client-id=producer-1}             : 0.000
producer-metrics:successful-authentication-total:{client-id=producer-1}            : 0.000
producer-metrics:successful-reauthentication-rate:{client-id=producer-1}           : 0.000
producer-metrics:successful-reauthentication-total:{client-id=producer-1}          : 0.000
producer-metrics:waiting-threads:{client-id=producer-1}                            : 0.000
producer-node-metrics:incoming-byte-rate:{client-id=producer-1, node-id=node--1}   : 0.000
producer-node-metrics:incoming-byte-rate:{client-id=producer-1, node-id=node-1}    : 457980.335
producer-node-metrics:incoming-byte-total:{client-id=producer-1, node-id=node--1}  : 585.000
producer-node-metrics:incoming-byte-total:{client-id=producer-1, node-id=node-1}   : 43571864.000
producer-node-metrics:outgoing-byte-rate:{client-id=producer-1, node-id=node--1}   : 0.000
producer-node-metrics:outgoing-byte-rate:{client-id=producer-1, node-id=node-1}    : 108971009.184
producer-node-metrics:outgoing-byte-total:{client-id=producer-1, node-id=node--1}  : 148.000
producer-node-metrics:outgoing-byte-total:{client-id=producer-1, node-id=node-1}   : 10367142940.000
producer-node-metrics:request-latency-avg:{client-id=producer-1, node-id=node--1}  : NaN
producer-node-metrics:request-latency-avg:{client-id=producer-1, node-id=node-1}   : 0.656
producer-node-metrics:request-latency-max:{client-id=producer-1, node-id=node--1}  : NaN
producer-node-metrics:request-latency-max:{client-id=producer-1, node-id=node-1}   : 19.000
producer-node-metrics:request-rate:{client-id=producer-1, node-id=node--1}         : 0.000
producer-node-metrics:request-rate:{client-id=producer-1, node-id=node-1}          : 7507.789
producer-node-metrics:request-size-avg:{client-id=producer-1, node-id=node--1}     : NaN
producer-node-metrics:request-size-avg:{client-id=producer-1, node-id=node-1}      : 14513.985
producer-node-metrics:request-size-max:{client-id=producer-1, node-id=node--1}     : NaN
producer-node-metrics:request-size-max:{client-id=producer-1, node-id=node-1}      : 14514.000
producer-node-metrics:request-total:{client-id=producer-1, node-id=node--1}        : 3.000
producer-node-metrics:request-total:{client-id=producer-1, node-id=node-1}         : 714287.000
producer-node-metrics:response-rate:{client-id=producer-1, node-id=node--1}        : 0.000
producer-node-metrics:response-rate:{client-id=producer-1, node-id=node-1}         : 7507.874
producer-node-metrics:response-total:{client-id=producer-1, node-id=node--1}       : 3.000
producer-node-metrics:response-total:{client-id=producer-1, node-id=node-1}        : 714287.000
producer-topic-metrics:byte-rate:{client-id=producer-1, topic=test-topic}          : 108565001.719
producer-topic-metrics:byte-total:{client-id=producer-1, topic=test-topic}         : 10328571446.000
producer-topic-metrics:compression-rate:{client-id=producer-1, topic=test-topic}   : 1.000
producer-topic-metrics:record-error-rate:{client-id=producer-1, topic=test-topic}  : 0.000
producer-topic-metrics:record-error-total:{client-id=producer-1, topic=test-topic} : 0.000
producer-topic-metrics:record-retry-rate:{client-id=producer-1, topic=test-topic}  : 0.000
producer-topic-metrics:record-retry-total:{client-id=producer-1, topic=test-topic} : 0.000
producer-topic-metrics:record-send-rate:{client-id=producer-1, topic=test-topic}   : 52555.671
producer-topic-metrics:record-send-total:{client-id=producer-1, topic=test-topic}  : 5000000.000
```


