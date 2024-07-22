FROM python:3.8

LABEL maintainer="vladosmen29@gmial.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY req.txt .

RUN apt-get update &&  apt-get upgrade -y
RUN pip install -r req.txt

COPY . /app/

VOLUME ["/app/staticfiles", "/app/media"]

EXPOSE 8008

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8008", "--timeout", "10000", "--limit-request-field_size", "16384", "--workers", "2"]
