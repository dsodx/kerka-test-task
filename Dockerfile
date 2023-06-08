FROM python:3.11.3 AS build
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

FROM python:3.11.3
COPY --from=build /venv /venv
ENV PATH="/venv/bin:$PATH"
WORKDIR /app
COPY . .
CMD ["python3", "-m", "bot"]
