FROM python:3.8

WORKDIR /pizza

ENV DATABASE_URI=mysql+pymysql://root:pizza123@mysql_container:3306/chefdb

ENV KEY=123456789

COPY application /pizza/application

COPY app.py create.py requirements.txt /pizza/

RUN pip install -r requirements.txt

COPY . /pizza/

ENTRYPOINT ["python3", "app.py"]
