from python:3.11-slim

workdir /app

copy requirements.txt .
run pip install --no-cache-dir -r requirements.txt

copy . .

expose 8000

cmd ['unicorn', 'app:app', '--host', '0.0.0.0', '--port', '8000']