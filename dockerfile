FROM python:3.8

WORKDIR /pizza

ENV DATABASE_URI=${MY_DATABASE}

ENV KEY=${MY_SECRET_KEY}

COPY application /pizza/application

COPY app.py create.py requirements.txt /pizza/

RUN pip install -r requirements.txt

COPY . /pizza/

ENTRYPOINT ["python3", "app.py"]