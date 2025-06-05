FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN apt-get update \
    && apt-get install -y gnupg2 \
    && echo "deb http://deb.debian.org/debian bullseye main" > /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y netcat postgresql-client
RUN apt-get update && apt-get install -y netcat postgresql-client
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
