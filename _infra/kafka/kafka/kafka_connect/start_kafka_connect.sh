#!/bin/bash

# Start Kafka Connect in distributed mode
exec /opt/kafka/bin/connect-distributed.sh /opt/kafka/config/connect-distributed.properties
