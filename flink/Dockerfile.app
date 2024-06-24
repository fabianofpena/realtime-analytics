# Dockerfile.app
FROM fabianofpena/flink-python-base:1.4

# Add your Python scripts and JAR files as root
USER root
RUN mkdir -p /opt/flink/usrlib/src /opt/flink/lib
COPY src /opt/flink/usrlib/src
COPY jars /opt/flink/lib

# Set the environment variable for Kafka bootstrap servers
ENV KAFKA_BOOTSTRAP_SERVERS=stream-kafka-bootstrap.processing.svc.cluster.local:9092

# Set permissions and switch to flink user
RUN chown -R flink:flink /opt/flink/usrlib/src /opt/flink/lib
USER flink

# Set the working directory
WORKDIR /opt/flink/usrlib/src
