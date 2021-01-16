FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /brocoolio

COPY requirements.txt /brocoolio/
RUN pip install -r requirements.txt

COPY . .
RUN chmod 755 ./entrypoint.sh

RUN chown -R 1001:1001 .
USER 1001

CMD ["bash", "entrypoint.sh"]
