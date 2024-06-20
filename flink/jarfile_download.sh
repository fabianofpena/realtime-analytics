#!/bin/sh

JARS_DIR=jars

KAFKA_CLIENTS_JAR=https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/2.8.0/kafka-clients-2.8.0.jar
FLINK_CONNECTOR_BASE_JAR=https://repo1.maven.org/maven2/org/apache/flink/flink-connector-base/1.17.2/flink-connector-base-1.17.2.jar
MYSQL_CONNECTOR_JAR=https://repo.maven.apache.org/maven2/mysql/mysql-connector-java/8.0.27/mysql-connector-java-8.0.27.jar
FLINK_JDBC_CONNECTOR_JAR=https://repo.maven.apache.org/maven2/org/apache/flink/flink-connector-jdbc/3.1.0-1.17/flink-connector-jdbc-3.1.0-1.17.jar

mkdir -p ${JARS_DIR}

wget -P ${JARS_DIR} ${KAFKA_CLIENTS_JAR}
wget -P ${JARS_DIR} ${FLINK_CONNECTOR_BASE_JAR}
wget -P ${JARS_DIR} ${MYSQL_CONNECTOR_JAR}
wget -P ${JARS_DIR} ${FLINK_JDBC_CONNECTOR_JAR}
