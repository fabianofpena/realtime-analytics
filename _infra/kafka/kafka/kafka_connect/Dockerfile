# Use a versão específica do Kafka 3.6.1 do Strimzi
FROM quay.io/strimzi/kafka:0.39.0-kafka-3.6.1

# Utilizar o usuário root para permissões de escrita
USER root:root

# Instalar wget, tar, gzip
RUN microdnf install wget tar gzip && microdnf clean all

# Criar os diretórios necessários para os plugins
RUN mkdir -p /opt/kafka/plugins/debezium-sqlserver-cdc \
    && mkdir -p /opt/kafka/plugins/debezium-mongodb-cdc \
    && mkdir -p /opt/kafka/plugins/debezium-mysql-cdc \
    && mkdir -p /opt/kafka/plugins/debezium-postgres-cdc

# Definir as versões das ferramentas e dependências
ENV DEBEZIUM_VERSION=2.2.0.Final
ENV KAFKA_CONNECT_PLUGINS_DIR=/opt/kafka/plugins
ENV MYSQL_CONNECTOR_VERSION=8.0.28

# Baixar e extrair Debezium MySQL connector
RUN cd /tmp && \
    wget https://repo1.maven.org/maven2/io/debezium/debezium-connector-mysql/${DEBEZIUM_VERSION}/debezium-connector-mysql-${DEBEZIUM_VERSION}-plugin.tar.gz && \
    tar -xzf debezium-connector-mysql-${DEBEZIUM_VERSION}-plugin.tar.gz && \
    mv debezium-connector-mysql/* ${KAFKA_CONNECT_PLUGINS_DIR}/debezium-mysql-cdc && \
    rm -rf /tmp/*

# Baixar e adicionar o MySQL Connector JAR
RUN wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/${MYSQL_CONNECTOR_VERSION}/mysql-connector-java-${MYSQL_CONNECTOR_VERSION}.jar -P ${KAFKA_CONNECT_PLUGINS_DIR}/debezium-mysql-cdc/

# Copiar o script para iniciar o Kafka Connect e definir permissões
COPY start_kafka_connect.sh /usr/bin/start_kafka_connect.sh
RUN chmod +x /usr/bin/start_kafka_connect.sh

# Configurar variáveis de ambiente
ENV CLASSPATH="${CLASSPATH}:${KAFKA_CONNECT_PLUGINS_DIR}/debezium-mysql-cdc/*"

# Definir usuário de volta para Kafka Connect
USER 1001

# Expor a porta Kafka Connect
EXPOSE 8083

# Comando padrão para iniciar o Kafka Connect
CMD ["start_kafka_connect.sh"]
