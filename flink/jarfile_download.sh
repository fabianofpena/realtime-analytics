#!/bin/sh

JARS_DIR=jars

KAFKA_CLIENTS_JAR=https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/2.8.0/kafka-clients-2.8.0.jar
FLINK_CONNECTOR_BASE_JAR=https://repo1.maven.org/maven2/org/apache/flink/flink-connector-base/1.17.2/flink-connector-base-1.17.2.jar
MYSQL_CONNECTOR_JAR=https://repo.maven.apache.org/maven2/mysql/mysql-connector-java/8.0.27/mysql-connector-java-8.0.27.jar
FLINK_JDBC_CONNECTOR_JAR=https://repo.maven.apache.org/maven2/org/apache/flink/flink-connector-jdbc/3.1.0-1.17/flink-connector-jdbc-3.1.0-1.17.jar

mkdir -p ${JARS_DIR}

# download a JAR if it doesn't already exist
download_jar() {
  local url=$1
  local dir=$2
  local file_name=$(basename ${url})

  if [ -f "${dir}/${file_name}" ]; then
    echo "${file_name} already exists, skipping download."
  else
    wget -P ${dir} ${url}
  fi
}

download_jar ${KAFKA_CLIENTS_JAR} ${JARS_DIR}
download_jar ${FLINK_CONNECTOR_BASE_JAR} ${JARS_DIR}
download_jar ${MYSQL_CONNECTOR_JAR} ${JARS_DIR}
download_jar ${FLINK_JDBC_CONNECTOR_JAR} ${JARS_DIR}
