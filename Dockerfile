FROM python:3.11.3
WORKDIR /app

COPY . .
RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "bot"]
