FROM python:latest

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN python create_table.py

EXPOSE 5000

CMD ["python", "main.py"]