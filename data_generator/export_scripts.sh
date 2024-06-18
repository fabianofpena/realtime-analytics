#!/bin/bash

# Define o diretório raiz do seu projeto e o arquivo de saída
ROOT_DIR="/Users/lucianopena/Dropbox/Data Engineering/kafka/kafka-flink-pinot/data_generator/src"
OUTPUT_FILE="/Users/lucianopena/Dropbox/Data Engineering/kafka/kafka-flink-pinot/data_generator/architecture/scripts.txt"

# Limpa ou cria o arquivo de saída
> "$OUTPUT_FILE"

# Função para extrair o conteúdo dos arquivos
extract_content() {
    local file_path="$1"
    local rel_path="${file_path#$ROOT_DIR/}"  # Obtém o caminho relativo

    # Escreve o caminho relativo no arquivo de saída
    echo "Processing file: $rel_path"  # Debugging output
    echo "1) relative path: $rel_path" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"

    # Escreve "2) content:" e o conteúdo do arquivo no arquivo de saída
    echo "2) content:" >> "$OUTPUT_FILE"
    cat "$file_path" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    echo "----------------------------------------" >> "$OUTPUT_FILE"
}

# Exporta recursivamente os arquivos, excluindo diretórios e arquivos específicos
export_files() {
    local current_dir="$1"
    local subdir

    echo "Entering directory: $current_dir"  # Debugging output

    # Navega por diretórios e subdiretórios
    for subdir in "$current_dir"/*; do
        if [ -d "$subdir" ]; then
            local dirname=$(basename "$subdir")
            if [[ "$dirname" != "__pycache__" && "$dirname" != ".venv" && "$dirname" != "venv" ]]; then
                export_files "$subdir"
            fi
        elif [ -f "$subdir" ]; then
            case "$subdir" in
                *.py|*.yml)
                    extract_content "$subdir"
                    ;;
            esac
        fi
    done
}

# Verify if ROOT_DIR exists
if [ -d "$ROOT_DIR" ]; then
    echo "Root directory found: $ROOT_DIR"  # Debugging output
    # Inicia o processo de exportação a partir do diretório raiz
    export_files "$ROOT_DIR"
    echo "Exportação concluída. Verifique o arquivo em $OUTPUT_FILE."
else
    echo "Root directory does not exist: $ROOT_DIR"  # Debugging output
fi
