FROM python:3.9 
COPY requirements.txt /webapp/requirements.txt
WORKDIR /webapp
RUN pip3 install -r requirements.txt
COPY . /webapp
ENTRYPOINT ["python"]
CMD ["app.py"]
