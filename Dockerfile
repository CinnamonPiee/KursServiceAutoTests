FROM python:3.13

# Устанавливаем зависимости для добавления репозитория Google
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    ca-certificates \
    libx11-6 \
    libxcomposite1 \
    libxrandr2 \
    libgdk-pixbuf2.0-0 \
    libnss3 \
    libxss1 \
    libasound2 \
    libappindicator3-1 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libgdk-pixbuf2.0-0 \
    libpangocairo-1.0-0 \
    libpango-1.0-0

# Добавляем репозиторий Google Chrome
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'

# Устанавливаем Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable

# Устанавливаем зависимости проекта
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Запускаем тесты
CMD ["pytest"]
