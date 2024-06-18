# Create virtualenv

```sh
# Local environment
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt 
```

```sh
# Mysql DB deployment
docker-compose up -d

# Connect through an IDE
host: localhost
port: 3306
user: root
pass: password
```