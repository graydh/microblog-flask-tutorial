FROM python:3.9-slim

LABEL Description="test smtp server"
EXPOSE 8025
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
CMD python3 -m aiosmtpd --nosetuid --debug --debug --listen 0.0.0.0:8025