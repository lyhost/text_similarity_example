FROM python:3.6-slim
ENV APP_NAME text_similiar
ENV APP_DIR /home/admin/$APP_NAME
RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR

RUN pip install --no-cache-dir numpy hug gunicorn

COPY . $APP_DIR

EXPOSE 8000

ENTRYPOINT ["sh", "start.sh"]
