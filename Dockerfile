FROM python:3.12-slim

RUN apt-get update && apt-get install -y chromium chromium-driver && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .env
COPY ./src ./src

CMD ["python", "src/reclameaqui.py"]
