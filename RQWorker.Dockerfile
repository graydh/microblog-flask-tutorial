FROM python:3.9-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP microblog.py
RUN flask translate compile

ENTRYPOINT ["rq"]
CMD ["worker", "-u", "redis://redis:6379/0", "microblog-tasks"]