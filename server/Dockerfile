FROM python:3.9
WORKDIR /server

RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5005
COPY . .
CMD [ "python", "app.py" ]