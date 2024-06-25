# Infra Setup

## Create namespaces 

```sh
# 1) create namespaces
kubectl create namespace database
kubectl create namespace processing
kubectl create namespace datastore
```

## Deploy Flink Operator

```sh
cd _infra/flink

# Deploy cert-manager
kubectl create -f https://github.com/jetstack/cert-manager/releases/download/v1.8.2/cert-manager.yaml

# Deploy Flink Helm chart
helm repo add flink-operator-repo https://downloads.apache.org/flink/flink-kubernetes-operator-1.7.0
helm install \
      --namespace "processing" \
      --debug \
      --wait=false  \
      "flink" -f values.yaml .

# Submit a testing job
kubectl create -f https://raw.githubusercontent.com/apache/flink-kubernetes-operator/release-1.8/examples/basic.yaml
```

## Deploy MySQL data generator database

```sh
# Deploy MySQL helm chart
cd _infra/mysql
helm install \
      --namespace "database" \
      --debug \
      --wait=false  \
      "mysql" -f values.yaml .

# Get pass
MYSQL_ROOT_PASSWORD=$(kubectl get secret --namespace database mysql -o jsonpath="{.data.mysql-root-password}" | base64 -d)

# Port-forward
kubectl port-forward svc/mysql 3306:3306 -n database
```

## Install Apache Pinot

```sh
# Deploy Apache Pinot
cd _infra/pinot
helm install \
      --namespace "datastore" \
      --debug \
      --wait=false  \
      "pinot" -f values.yaml .

```

## Install Strimzi Operator and Kafka

```sh
# Deploy Strimzi Operator 
cd _infra/strimzi
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
```

## Validate Kafka Topics

```sh
# Run kafka cli commands underneath the pod
kubectl exec -it stream-kafka-0 -n processing -- /bin/bash
bin/kafka-topics.sh --list --bootstrap-server stream-kafka-bootstrap:9092

# List Topics
kubectl exec -it stream-kafka-0 -n processing -- bin/kafka-topics.sh --list --bootstrap-server stream-kafka-bootstrap.processing.svc.cluster.local:9092

# Read Data from Raw Topics
kubectl exec -it stream-kafka-0 -n processing -- bin/kafka-console-consumer.sh --bootstrap-server stream-kafka-bootstrap.processing.svc.cluster.local:9092 --topic mysql_retail_addresses --from-beginning
kubectl exec -it stream-kafka-0 -n processing -- bin/kafka-console-consumer.sh --bootstrap-server stream-kafka-bootstrap.processing.svc.cluster.local:9092 --topic mysql_retail_customers --from-beginning
kubectl exec -it stream-kafka-0 -n processing -- bin/kafka-console-consumer.sh --bootstrap-server stream-kafka-bootstrap.processing.svc.cluster.local:9092 --topic mysql_retail_order_items --from-beginning
kubectl exec -it stream-kafka-0 -n processing -- bin/kafka-console-consumer.sh --bootstrap-server stream-kafka-bootstrap.processing.svc.cluster.local:9092 --topic mysql_retail_orders --from-beginning
kubectl exec -it stream-kafka-0 -n processing -- bin/kafka-console-consumer.sh --bootstrap-server stream-kafka-bootstrap.processing.svc.cluster.local:9092 --topic mysql_retail_products --from-beginning

# Read Data from Enriched Topics
kubectl exec -it stream-kafka-0 -n processing -- bin/kafka-console-consumer.sh --bootstrap-server stream-kafka-bootstrap.processing.svc.cluster.local:9092 --topic enriched_orders --from-beginning

# Delete Topics
kubectl exec -it stream-kafka-0 -n processing -- bin/kafka-topics.sh --delete --bootstrap-server stream-kafka-bootstrap.processing.svc.cluster.local:9092 --topic enriched_orders

# Count Topics rows
# Final Offsets
kubectl exec -it stream-kafka-0 -n processing -- \
  bin/kafka-run-class.sh kafka.tools.GetOffsetShell \
  --broker-list stream-kafka-bootstrap.processing.svc.cluster.local:9092 \
  --topic enriched_orders \
  --time -1

# Initial Offsets
kubectl exec -it stream-kafka-0 -n processing -- \
  bin/kafka-run-class.sh kafka.tools.GetOffsetShell \
  --broker-list stream-kafka-bootstrap.processing.svc.cluster.local:9092 \
  --topic enriched_orders \
  --time -2
```



