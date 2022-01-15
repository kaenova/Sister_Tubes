FROM python:3.10.1-alpine3.14

WORKDIR /app

COPY covidServer.py .
COPY database_nama.txt .
COPY database_nik.txt .
ENV PYTHONUNBUFFERED="true"

CMD ["python", "covidServer.py", "database_nik.txt", "database_nama.txt", "81"]
