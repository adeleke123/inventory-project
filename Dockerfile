FROM python:3.12-slim
WORKDIR /app
COPY . .
ENV DB_PATH=/data/inventory.db
CMD ["python", "app.py"]
