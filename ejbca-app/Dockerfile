# Dockerfile
FROM python:3.9-slim

RUN pip install flask requests

WORKDIR /app

COPY app.py /app

EXPOSE 9090

CMD ["python", "app.py"]
