FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

# Dependências do sistema
RUN apt-get update && apt-get install -y \
    pandoc \
    libpangocairo-1.0-0 \
    libcairo2 \
    libpangoft2-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala as dependências Python
RUN pip install --no-cache-dir weasyprint markdown2

# Cria diretório de trabalho
WORKDIR /app

# Copia o conteúdo para dentro do container
COPY . .

# Define comando de execução
CMD ["python", "app/main.py"]
