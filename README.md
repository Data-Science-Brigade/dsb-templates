# dsb-templates

Templates of Docker projects for Data Science and coding projects


## data-science-exploratory

**Description:** A simple folder structure meant for exploratory projects. Contains pyspark Jupyter notebook.

Directory structure:

```
| data-science-exploratory
├── .env.example              # Default PORTs and user settings
├── docker-compose.yml
├── research /                # Jupyter notebooks
├───── Dockerfile (*)
├───── requirements.txt
├── data /                    # Not tracked by Git

```

\* Dockerfile inherited from [pyspark-jupyter-notebook](https://hub.docker.com/r/jupyter/pyspark-notebook/)

## data-science-cloud

**Description:** For more complex data science projects that involve creation of python modules. Spark included by default.

```
| data-science-exploratory
├── .env.example              # Default PORTs and user settings
├── docker-compose.yml        # Spark-server + Spark-worker
├── research /                # Jupyter notebooks
├───── Dockerfile (*)
├───── requirements.txt
├── cloud /                   # Scripts to interact with Google Cloud 
├───── Dockerfile
├── data /                    # Not tracked by Git

```

\* Dockerfile inherited from [jupyter/pyspark-jupyter-notebook](https://hub.docker.com/r/jupyter/pyspark-notebook/)


## data-science-full

**Description:** For more complex data science projects that involve creation of python modules. Spark included by default.

```
| data-science-exploratory
├── .env.example              # Default PORTs and user settings
├── docker-compose.yml        # Spark-server + Spark-worker
├── research /                # Jupyter notebooks
├───── Dockerfile (*)
├───── requirements.txt
├── processing /              # Python modules and scripts
├───── Dockerfile (**)
├───── requirements.txt
├───── shared /               # Python modules live here
├───── tests /                # Python tests live here
├───── scripts /              # Python and Bash scripts live here
├── cloud /                   # Scripts to interact with Google Cloud 
├───── Dockerfile
├── data /                    # Not tracked by Git

```

\* Dockerfile inherited from [jupyter/pyspark-jupyter-notebook](https://hub.docker.com/r/jupyter/pyspark-notebook/)

\** Dockerfile inherited from [dsb/pyspark-image](https://hub.docker.com/r/datasciencebrigade/pyspark-image)



