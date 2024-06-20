FROM apache/flink:1.17.2

# Define o diretório de trabalho
WORKDIR /src

# Copia o código da aplicação Flink para o contêiner
COPY . /src

# Instala as dependências necessárias (por exemplo, pip para instalar pacotes Python)
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install -r requirements.txt

# Cria um diretório para os arquivos JAR no contêiner
RUN mkdir -p /opt/flink/lib

# Copia os arquivos JAR para o diretório /opt/flink/lib no contêiner
COPY jars /opt/flink/lib

# Define a variável de ambiente para incluir o diretório dos JARs no classpath do Flink
ENV FLINK_CLASSPATH="/opt/flink/lib/*"

# Comando para iniciar a aplicação Flink
CMD ["python3", "main.py"]
