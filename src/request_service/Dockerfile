FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Crear el directorio de logs
RUN mkdir -p /app/logs

COPY . .

CMD ["sh", "-c", "sleep 25 && python app.py"]
