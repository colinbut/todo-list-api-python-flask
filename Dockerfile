FROM python:3.8-alpine
LABEL maintainer "Colin But"
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -qr requirements.txt
CMD [ "python", "src/app.py" ]