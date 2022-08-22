FROM python:3 as dev

ADD ./requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install twine pytest
