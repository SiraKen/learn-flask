FROM python:latest

WORKDIR /app

ADD ./src .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
