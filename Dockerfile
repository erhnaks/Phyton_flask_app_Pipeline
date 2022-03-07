FROM python:3.8

WORKDIR /app

ENV DATABASE_URI=msqlite:///chefdb

ENV MY_KEY=123456789

COPY . .

COPY app.py create.py requirements.txt /app/

RUN pip install -r requirements.txt 

RUN python3 create.py

ENTRYPOINT ["python3", "app.py"]