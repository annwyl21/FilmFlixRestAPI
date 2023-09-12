# a recognised image
FROM python

# what file do we want to run
WORKDIR /code

COPY requirements.txt .

RUN pip3 install -r requirements.txt

# copy from here to the local directory on docker
COPY . .

EXPOSE 5000

ENTRYPOINT [ "gunicorn", "app:app" ]