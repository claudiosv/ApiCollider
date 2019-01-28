# FROM tiangolo/uwsgi-nginx-flask:python3.7
# ENV STATIC_INDEX 0
# ENV STATIC_PATH /app/react_app/build
# ENV STATIC_URL /content
# # ENV STATIC_URL /
# ENV UWSGI_INI /app/python_app/uwsgi.ini
# # COPY ./app/python_app /app/python_app
# # COPY ./app/react_app /app/react_app
# # COPY *.conf /etc/nginx/conf.d/
# COPY ./app /app
# WORKDIR /app/python_app
# # RUN python3 -m venv /venv && . venv/bin/activate
# #Install modules
# RUN pip3 install --no-cache-dir -r requirements.txt
FROM alpine:latest
EXPOSE 3031
VOLUME /usr/src/app/public
WORKDIR /usr/src/app
RUN apk add --no-cache \
    uwsgi-python3 \
    python3
COPY . .
RUN rm -rf public/*
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
CMD [ "uwsgi", "--socket", "0.0.0.0:3031", \
    "--uid", "uwsgi", \
    "--plugins", "python3", \
    "--protocol", "uwsgi", \
    "--wsgi-file", "main.py", \
    "--callable", "app", \ 
    "--processes", "4", \
    "--threads", "2" ]
#    "--wsgi", "main:app" ]
# --wsgi-file myflaskapp.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191