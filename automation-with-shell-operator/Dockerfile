# Dockerfile
FROM python:3.9
RUN useradd --create-home app

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN chmod +x run_unit_test.sh

RUN chown -R app:app .
# change user
# USER <username>
USER app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7200"]
