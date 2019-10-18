FROM datasciencebrigade/pyspark-image:1.0

WORKDIR /mnt/code
COPY Makefile Makefile

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
