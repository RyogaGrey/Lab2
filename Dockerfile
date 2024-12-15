# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем минимальные системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1 && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем Python-зависимости
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение
COPY . .

# Указываем точку входа
ENTRYPOINT ["python", "app.py"]
