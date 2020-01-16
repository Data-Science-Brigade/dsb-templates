# Pyspark image from https://hub.docker.com/r/datasciencebrigade/pyspark-image
FROM datasciencebrigade/pyspark-image:1.2

COPY conf/jars/* $SPARK_HOME/jars/
COPY conf/hadoop/ $HADOOP_CONF_DIR/

WORKDIR /mnt/code
COPY Makefile Makefile

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash"]
