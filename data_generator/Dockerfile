# Utilizar uma imagem base Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requirements
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY . .

# Definir variáveis de ambiente com valores padrão que podem ser substituídos em tempo de execução
ENV DB_DIALECT=${DB_DIALECT}
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_HOST=${DB_HOST}
ENV DB_PORT=${DB_PORT}
ENV DB_NAME=${DB_NAME}

# Definir o comando padrão para iniciar a aplicação
CMD ["python", "run.py"]
