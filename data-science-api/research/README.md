# <Nome-do-Projeto> - Research

Pasta usada para a exploração de dados do projeto <Nome-do-Projeto> buscando inserir aplicações de ciência de dados.


## Dados

- Indicar onde estão os dados a serem utilizados.


### Setup

1. Se ainda não tiver, crie o arquivo `.env` na raiz do projeto. Há um template no arquivo `.env.example`.

2. Garanta que as variáveis do `.env` estejam configuradas corretamente. Preste um atenção especial ao parâmetro `DATA_VOLUME`, que deve indicar um caminho absoluto no computador onde
os dados do projeto estão armazenados. Exemplo: se a pasta de dados ficará no diretório `/home/user/dados-<Nome-do-Projeto>`, configure `DATA_VOLUME=/home/user/dados-<Nome-do-Projeto>`

3. De build nos containers:

```
docker-compose build
```

4. Faça download dos arquivos que serão usados e mova para a pasta de dados do projeto (caminho indicado no `DATA_VOLUME`).

## Como executar os notebooks?

1. Instale o Docker. Instruções para [Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04) e [Windows](https://docs.docker.com/docker-for-windows/install/)

2. Instale o [Docker Compose](https://docs.docker.com/compose/install/), caso não tenha sido instalado junto com o Docker.

3. Crie um arquivo `.env` com o conteúdo do arquivo de exemplo (`.env.example`)

- Este arquivo contém parâmetros e configurações de portas TCP que serão utilizados pelo Docker
- O parâmetro mais importante é o `DATA_VOLUME`, que indica a pasta no seu computador onde os dados (.csv, .zip etc) estão armazenados.

4. Dê build no projeto:

```console
cd <pasta do projeto>
docker-compose build
```

5. Suba o servidor Jupyter:

```console
docker-compose up
```

6. Acesse a URL que aparecerá no console.


## Como adicionar uma nova biblioteca no projeto?

1. Edite o arquivo `processing/requirements.txt`, adicionando o nome e a versão da biblioteca que deverá ser instalada. 

Por exemplo:

```txt
# Bibliotecas Python
numpy==1.15.1
```

2. Refaça o build do projeto

```
docker-compose build
```

3. Suba o servidor Jupyter

```
docker-compose up
```
