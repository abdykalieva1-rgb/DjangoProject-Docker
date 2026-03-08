FROM python:3.11-slim

WORKDIR /app

# Копируем requirements.txt и устанавливаем библиотеки
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы проекта
COPY . .

# Запускаем сервер Django (0.0.0.0 нужно, чтобы контейнер был доступен снаружи)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]