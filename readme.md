# Setup Helm Charts

```sh
# 1) create namespaces
kubectl create namespace database
kubectl create namespace processing
kubectl create namespace datastore


# 2) Install MySQL on database namespace
helm install \
      --namespace "database" \
      --debug \
      --wait=false  \
      "mysql" -f values.yaml .

# Get pass
MYSQL_ROOT_PASSWORD=$(kubectl get secret --namespace database mysql -o jsonpath="{.data.mysql-root-password}" | base64 -d)

# Port-forward
kubectl port-forward svc/mysql 3306:3306 -n database

# 3) Install Strimzi Operator
helm install \
      --namespace "processing" \
      --debug \
      --wait=false  \
      "kafka" -f values.yaml .

# Install Kafka Broker
kubectl apply -f strimzi/kafka/broker.yaml -n processing

# Install KafkaConnect
kubectl apply -f strimzi/kafka/kafka-connect.yaml -n processing

# Install Schema Registry
helm upgrade --install \
      --namespace "processing" \
      --debug \
      --wait=false  \
      "schema-registry" -f values.yaml .

# Add as many as KafkaConnector you need
kubectl apply -f strimzi/kafka/connectors/mysql-connector.yaml


# 4) Install Apache Pinot namespace datastore
helm install \
      --namespace "datastore" \
      --debug \
      --wait=false  \
      "pinot" -f values.yaml .
```

# Check Kafka Topics

```sh
kubectl exec -it stream-kafka-0 -n processing -- /bin/bash
bin/kafka-topics.sh --list --bootstrap-server stream-kafka-bootstrap:9092

# List Topics
kubectl exec -it stream-kafka-0 -n processing -- bin/kafka-topics.sh --list --bootstrap-server stream-kafka-bootstrap.processing.svc.cluster.local:9092

# Read Data from Topics
kubectl exec -it stream-kafka-0 -n processing -- bin/kafka-console-consumer.sh --bootstrap-server stream-kafka-bootstrap.processing.svc.cluster.local:9092 --topic mysql_retail_orders --from-beginning
kubectl exec -it stream-kafka-0 -n processing -- bin/kafka-console-consumer.sh --bootstrap-server stream-kafka-bootstrap.processing.svc.cluster.local:9092 --topic enriched_orders --from-beginning

kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic mysql_retail_orders --from-beginning

# Delete Topics
kubectl exec -it stream-kafka-0 -n processing -- bin/kafka-topics.sh --delete --bootstrap-server stream-kafka-bootstrap.processing.svc.cluster.local:9092 --topic mysql-retail-.retail.addresses

```
