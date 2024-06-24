import os
import sys
import logging
from dotenv import load_dotenv
from app import run

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"CLASSPATH: {os.environ.get('CLASSPATH')}")

kafka_bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS')
logger.info(f"KAFKA_BOOTSTRAP_SERVERS: {kafka_bootstrap_servers}")

if not kafka_bootstrap_servers:
    logger.error("KAFKA_BOOTSTRAP_SERVERS is not set.")
    sys.exit(1)

if __name__ == "__main__":
    run(kafka_bootstrap_servers)
