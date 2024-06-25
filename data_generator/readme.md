## Data Generator App Instructions

## Create virtualenv

```sh
# Setup Local environment
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt 

# Mysql DB deployment
docker-compose up -d

# Connect through an IDE
host: localhost
port: 3306
user: root
pass: password
```

## Build and Push application to container registry

```sh
make all
```

## Deploy application on kubernetes cluster

```sh
cd data_generator/cron
kubectl apply -f cron_mysql.yaml
```