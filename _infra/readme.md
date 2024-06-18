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

# 3) Install Kafka Strimzi
helm install \
      --namespace "processing" \
      --debug \
      --wait=false  \
      "kafka" -f values.yaml .

# Install Apache Pinot namespace datastore
helm install \
      --namespace "datastore" \
      --debug \
      --wait=false  \
      "pinot" -f values.yaml .

