FROM jupyter/pyspark-notebook:e8613d84128b

WORKDIR /mnt/code

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN conda install python-graphviz

RUN ipython3 profile create
RUN echo 'import pandas as pd; pd.set_option("display.width", 160)' >> /home/jovyan/.ipython/profile_default/ipython_config.py
RUN echo 'c.NotebookApp.port = 8888' >> /home/jovyan/.jupyter/jupyter_notebook_config.py

USER root

RUN apt update && apt install -y python-pydot python-pydot-ng graphviz

USER jovyan

RUN jupyter contrib nbextension install --user
RUN jupyter nbextensions_configurator enable --user
RUN jupyter serverextension enable --py jupyter_spark
RUN jupyter nbextension install --py jupyter_spark --user
RUN jupyter nbextension enable --py jupyter_spark
RUN jupyter nbextension enable --py widgetsnbextension
RUN jupyter nbextension enable execute_time/ExecuteTime
RUN jupyter nbextension enable codefolding/main
RUN jupyter nbextension enable codefolding/edit
RUN jupyter nbextension enable toc2/main
RUN jupyter nbextension enable collapsible_headings/main
#RUN jt -t chesterish -T -N -kl -ofs 10 -tfs 11


EXPOSE 8080
EXPOSE 8081
EXPOSE 7077
EXPOSE 4040
