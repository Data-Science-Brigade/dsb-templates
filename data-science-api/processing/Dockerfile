# Python image from https://hub.docker.com/_/python
FROM python:3.7-stretch

WORKDIR /mnt/code

RUN apt-get update \
  && apt-get -y install vim gcc netcat poppler-utils wait-for-it default-jre zip

ENV TZ 'America/Sao_Paulo'
RUN echo $TZ > /etc/timezone && \
    apt-get update && apt-get install -y tzdata && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean 

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["entrypoint.sh"]
CMD ["uvicorn", "--reload", "--host", "0.0.0.0", "--port", "5000", "api:app"]
