# Scripts

Use este diretório para armazenar scripts .sh ou .py que rodam independentes da API. Alguns scripts são necessários para criar uma base de dados inicial ou para rodar um algoritmo de pre-processamento (exemplo: converter documentos para .txt) ou outras rotinas ou execuções em _batch_.

## Como rodar os scripts?

Os scripts poderão ser executados apenas uma vez ou periodicamente pela aplicação. Suponha que haja um script **run_initial_data_processing.sh**, é possível executá-lo como uma aplicação independente usando `docker-compose run`:

```console
docker-compose run --rm --service-ports bash scripts/run_initial_data_processing.sh
```

**E se eu precisar rodar um script dentro de uma instância de um container Docker que já está rodando?**

Se você já tiver um container *processing* ativo e quiser rodar o script no mesmo container, use:

```console
docker-compose exec container bash scripts/run_initial_data_processing.sh
```
