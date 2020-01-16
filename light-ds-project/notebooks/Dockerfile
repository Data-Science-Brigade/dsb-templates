# Jupyter pyspark image from https://hub.docker.com/r/datasciencebrigade/jupyter-pyspark-image
FROM datasciencebrigade/jupyter-pyspark-image:1.2

USER jovyan

WORKDIR /mnt/code

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV JUPYTER_EXTERNAL_PORT 8888

RUN cp /etc/jupyter/jupyter_notebook_config.py /home/jovyan/.jupyter/jupyter_notebook_config.py
RUN echo '\nc.NotebookApp.port = int(os.environ["JUPYTER_EXTERNAL_PORT"])' >> /home/jovyan/.jupyter/jupyter_notebook_config.py
