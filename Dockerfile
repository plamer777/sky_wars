FROM python:3.10-slim

WORKDIR /skywars

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:5000 --threads=4 app:app