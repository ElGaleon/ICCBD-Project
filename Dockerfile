FROM wurstmeister/kafka

ADD /jmx-exporter/kafka-2_0_0.yml /usr/app/prom-jmx-agent-config.yml
ADD https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.19.0/jmx_prometheus_javaagent-0.19.0.jar /usr/app/jmx_prometheus_javaagent.jar
