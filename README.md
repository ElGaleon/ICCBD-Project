##  ICCBD Project
@Author: Christian Galeone

Setup of kafka Cluster via Docker and importing of metrics on Grafana by the use of Prometheus and JMX-Exporter

# Setting up Kafka monitoring using Prometheus and Grafana on Docker

Kafka is a distributed streaming platform that is used publish and subscribe to streams of records. Kafka is used for fault-tolerant storage. It replicates topic log partitions to multiple servers. Kafka is designed to allow your apps to process records as they occur.

## Prerequisites
This tutorial assumes that you have stable build of docker and docker-compose pre-installed. Installation guidelines can be found [here](https://docs.docker.com/compose/install/).

## Initializing your containers

Switch to this directory and call docker-compose to start your containers

```
$ docker-compose up -d
```
The -d flag starts the containers in background mode. At the point, you may call ``docker-compose ps`` to confirm that your 4 containers are up. Additionally, you may shut down your containers using ``docker-compose stop CONTAINER_NAME``

## Kafka set up
To similiate a kafka set up, we will set up a sample Producer and Consumer under a sample topic. Start by enterring the kafka container using the docker command and creating a topic
```
$ sudo docker exec -it kafka /bin/sh
$ cd /opt/kafka
$ bin/kafka-topics.sh \
--create \
--topic test-topic\
--partitions 1 \
--replication-factor 1 \
--bootstrap-server localhost:9092
```

## Python Producers set up
To simulate producers, we will use a python script to send messages to the clusters. This command will run three producers that will sends messages to every cluster.
```shell
$ docker-compose -f compose-producer.yml up -d
```

## Python Consumers set up
To simulate consumers, we will use a python script to receive messages from the clusters. This command will run three consumers that will receive messages from every cluster.
```shell
$ docker-compose -f compose-consumers.yml up -d
```

## Prometheus set up

Opening [Prometheus Dashboard](http://localhost:9090/graph) show a rudimentary view of all Kafka metrics. Confirm that Kafka data is being scraped by visiting [targets](http://localhost:9090/targets), where the endpoint kafka should be up.
### Adding Up metrics to Prometheus Dashboard

Metrics can be observed right from the Prometheus dashboard. Click on the graph optino and enter the prometheus query desired.


## Grafana set up

### Log in
Login into [Grafana](http://localhost:3000/login) using credentials 'admin' in both user and password fields. You may or may not choose to skip changing the password.

### Add Data Source
Before setting up a dashboard, Prometheus must be added as a data source. Do so by clicking on the Add you first data source card and choosing Prometheus. Assign a suitable name for this and provide the source URL as ``http://localhost:9090`` and Access type of Browser (not Server). Confirm that everything is set upright with the Save & Test button and return to Grafana dashboard.

### Add basic dashboard
On the left side of the dashboard, hover over the Create tab and choose Import. Enter ``721`` under Import via Grafana and Load. Once again, assign a suitable name and choose source as the same Prometheus data source we set up above and import. <br>
The scope of the graphs and refresh rate can be adjusted on the top right of the dashboard.

---
## Producer Tests
To test producer semantics delivery, you have to enter the kafka container and create a topic. After that, you can run the producer-perf-test.sh script to send messages to the topic. 
I leave an example of how to run the script below:

```shell
$ producer-perf-test.sh --topic test-topic --num-records 1000 --record-size 1000 --throughput 1000 --producer-props bootstrap.servers=localhost:9092
```

The test of the project based on compare the different message delivery semantics of Kafka producers (<b>At least once</b>, <b>At most once</b>, <b>Exactly once</b>). <br>
To reproduce the tests, you have to run the <code>producer-perf-test.sh</code> script adding <code>--config-parameter</code> to set the delivery semantics.
We created config file to replicate the tests with different delivery semantics. You can see the config files in the <code>producer-configs</code> folder.

You can see some tests results in the <code>5_million_results.md</code> file.

---

### Generic Tests
If you want to do some more test, take a look at the [Benchmark](./test-results/benchmarks.md) file. There are some examples of tests that you can run to test the performance of your Kafka cluster.

---

### References
- [Kafka](https://kafka.apache.org/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [Monitoring Kafka](https://danielmrosa.medium.com/monitoring-kafka-b97d2d5a5434)
- [Monitoring Kafka Producer and Consumer: Best Practices](https://medium.com/@atri_iiita/monitoring-kafka-consumers-and-publishers-best-practices-9a912de8ad0b)