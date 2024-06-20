FROM apache/flink:1.17.2

# Copia o código da aplicação Flink para o contêiner
COPY . /app

# Define o diretório de trabalho
WORKDIR /app

# Instala as dependências necessárias (por exemplo, pip para instalar pacotes Python)
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install -r requirements.txt

# Comando para iniciar a aplicação Flink
CMD ["python3", "flink_enriched_app.py"]
