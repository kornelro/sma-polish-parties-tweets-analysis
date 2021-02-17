FROM python:3.6

COPY requirements.txt .
COPY prepare_data.py .

RUN pip3 install -r requirements.txt

RUN mkdir home/work
RUN mkdir home/data
