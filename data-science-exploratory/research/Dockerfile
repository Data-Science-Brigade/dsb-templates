FROM datasciencebrigade/jupyter-pyspark-image:1.0

USER jovyan

WORKDIR /mnt/code

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ARG JUPYTER_EXTERNAL_PORT
ENV JUPYTER_EXTERNAL_PORT $JUPYTER_EXTERNAL_PORT

RUN cp /etc/jupyter/jupyter_notebook_config.py /home/jovyan/.jupyter/jupyter_notebook_config.py
RUN echo '\nc.NotebookApp.port = int(os.environ["JUPYTER_EXTERNAL_PORT"])' >> /home/jovyan/.jupyter/jupyter_notebook_config.py
