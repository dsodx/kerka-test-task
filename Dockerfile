FROM python:3.11.3
WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
CMD ["python3", "-m", "bot"]
