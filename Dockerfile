FROM python:3.10.11-alpine

RUN mkdir -p /usr/src/bookmarks

COPY . /usr/src/bookmarks

WORKDIR /usr/src/bookmarks/bookmarks

RUN pip install -r /usr/src/bookmarks/requirements.txt


CMD ["python", "manage.py", "runserver" , "0.0.0.0:8000"]

