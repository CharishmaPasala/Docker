FROM python:3.7.5-alpine
COPY . /app2
WORKDIR /app2
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD ["app1.py"]
