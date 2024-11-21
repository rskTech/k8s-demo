FROM python:2.7-onbuild
EXPOSE 8080
CMD [ "python", "http_serv.py" ]
