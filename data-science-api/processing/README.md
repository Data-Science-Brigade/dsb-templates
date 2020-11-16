# <Nome-do-Projeto> - Processing

Pasta usada para o processamento dos dados do projeto <Nome-do-Projeto>.


## <Nome-da-API>  - SETUP

A API poderá ser configurada para o ambiente de desenvolvimento e testes ou para o ambiente de produção. Para isso, existem dois arquivos docker-compose:

- docker-compose-test-yml: Ambiente de desenvolvimento e testes
- docker-compose.yml: Ambiente mais próximo da configuração de deploy e produção (caso haja alguma particularidade)

O setup é praticamente idêntico, porém no ambiente de deploy e produção, podemos utilizar a pasta `processing/conf` para armazenar arquivos de configuração. 

Pode ser informado um exemplo de uso da pasta conf.


### Ambiente Desenvolvimento

O caminho mais fácil é usar o comando `make`. Para subir a aplicação com todas as configurações padrão, simplesmente rode:

```
make setup
make up
```

Alternativamente, se quiser fazer passo a passo, siga as instruções abaixo:

1. Configure o arquivo `.env`

```
cp .env.example .env
```

Por padrão, a variável `DATA_VOLUME` apontará para `./data`, altere manualmente esse valor caso esteja armazenando os seus dados localmente em algum outro diretório.


2. Faça o build do projeto:

```
docker-compose -f docker-compose-test.yml build
```

3. Suba a API

```
docker-compose -f docker-compose-test.yml up
```

## Testes Unitários

Uma das metodologias de desenvolvimento que seguimos nessa API é a chamada [TDD - _Test Driven Development_](https://en.wikipedia.org/wiki/Test-driven_development). Nessa metodologia, os testes unitários têm um papel fundamental: eles devem descrever todas as funcionalidades suportadas e permitidas pela API e até mesmo as situações em que a API deverá lançar algum erro.


Quando tiver trabalhando em uma tarefa de implementar alguma nova funcionalidade da API, o ideal é que você comece escrevendo o teste.

Por exemplo, se tiver que implementar uma função para calcular distância de coseno entre dois vetores, primeiro escreva um teste `test_cosine_similarity_works_as_expected` e ali dentro escreva todo o esqueleto da função que será testada:

```
from api.v1.similarity import cosine_similarity

def test_cosine_similarity_works_as_expected(self):

  vector_a = np.array([1, 3, 5, 1, 2])
  vector_b = np.array([23, 45, 1, 5, 6])

  result = cosine_similarity(vector_a, vector_b)
  expected_result = 0.23411

  assert result == pytest.approx(expected_result)

```

Note que nesse teste eu já suponha que a função `cosine_similarity` existe dentro do módulo `api.v1.similarity` e já recebe dois vetores numéricos. Se eu rodar o teste agora, ele vai falhar porque a função ainda não existe.

Agora que eu defini o que a nova função deve garantir, em termos de entrada e saída de dados, eu escrevo a função dentro do módulo `api.v1.similarity`. E aí, ao rodar o teste, a expectativa é que ele vá passar normalmente.

Nossos testes são escritos e validados com a biblioteca [pytest](https://docs.pytest.org/en/stable/contents.html).

### Como os testes funcionam?

Da forma como está configurado, o pytest irá seguir o seguinte fluxo:

1. Importa o código que está no `processing/tests/__init__.py`
  - Basicamente, isso vai inicializar a superclasse de testes `PySparkUnittestBase`, que é a base de todos os testes unitários da api.
  - **_Todas as classes de testes unitários devem herdar dessa classe!_**
  - A classe encapsula algumas funcionalidades básicas que podem ser reutilizadas em todos os testes unitários: aplicação cliente do FastAPI para testar os endpoints, conexões a bancos de dados de testes, inicialização de serviços (ex.: HDFS)
1. Rodar todo o código que está na função `processing/tests/conftest.py#pytest_configure`
1. Para cada classe de teste, o pytest irá **primeiro** executar o método `setup_class`.
  - Por padrão, o setup_class já é definido na classe `PySparkUnittestBase`. Na maioria dos casos, não é necessário reimplementar esse método.
1. O pytest então irá rodar cada função que inicie com a palavra "teste"
  - Por isso é importante nomear os testes com o seguinte padrão: `def test_...`

ATENÇÃO: a ordem em que os testes são executados não é garantida. Cada função de teste deve ser atômico, ou seja, um teste não deve depender de nada gerado no teste de cima.


### Como escrever um teste novo?

Toda vez que implementar uma nova feature ou requisito da API, adicione um teste unitário para garantir que aquela função/método funciona.

1. Dentro da pasta `processing/tests`, identifique o módulo mais adequado para o teste que deverá escrever. Por exemplo, se estiver escrevendo uma nova métrica de similaridade, adicione o teste ao `test_similarity.py`
1. Todo módulo de teste deverá conter uma ou mais classes de testes que herdam de `PySparkUnittestBase`. Por exemplo:

  ```
  class TestSimilarityMetrics(PySparkUnittestBase):

      @classmethod
      def setup_class(cls):
          super().setup_class()

      def test_<nome_do_seu_test_aqui>:
        ...
  ```
1. O nome do teste deve ser bem descritivo, não tem problema ser grande. Por exemplo:

  ```
  def test_cosine_similarity_works_as_expected(self):
     ...

  def test_api_return_exception_when_input_is_incorrect(self):
     ...

  ```
1. Lembre-se: você está escrevendo testes **unitários**, cada teste deve declarar todos os objetos que precisa usar. UM TESTE NÃO DEVE DEPENDER DE OUTRO PARA FUNCIONAR, CADA TESTE DEVE TENTAR SER O MAIS ATÔMICO POSSÍVEL. Não deve testar muitas coisas ao mesmo tempo. Ao escrever testes, não tem problema repetir algumas definições.
1. O que garante se um teste está passando ou falhando são os comandos `assert`. Saiba mais sobre os asserts [neste link](https://docs.pytest.org/en/stable/assert.html#assert).


### Como logar algo no terminal?

Não use `print`, use `logger`! O logger já está configurado no módulo `processing/api/v1/logging.py` e vai printar no terminal com cores e tudo mais. Dentro do código, use:

```
import logger

logger.debug("Debug")

logger.info("Mensagem")

logger.warn("Algo aqui tá meio estranho ou fora do padrão, pode dar algum erro")

logger.error("Erro")

# Como logar Exceptions
logger.exception(e)

# Use o método bind caso queira informar os parâmetros que foram passados
logger.bind(payload=bot_in.dict()).error(error_msg)
```

### Como rodar os testes que estou escrevendo?

Ao desenvolver um teste/funcionalidade da API, a forma mais prática é abrir um container e ir fazendo testes a medida que vc vai escrevendo a função.

Para abrir o shell do container `processing-test`, rode o comando `docker-compose run`:

```
docker-compose -f docker-compose-test run --rm --service-ports processing-test bash
```

Lá dentro, rode todos os testes com o comando:

```
python3 -m pytest tests/
```

Mas, suponha que você está trabalhando no módulo `tests/test_similarity.py`, você pode rodar apenas os testes desta classe com o comando:

```
python3 -m pytest tests/test_similarity.py
```

No terminal, você verá o total de testes que foram executados e quais delhes falharam ou deram erro.

### Como debugar linha a linha do que estou fazendo?

O [ipdb](https://hasil-sharma.github.io/2017-05-13-python-ipdb/) é seu melhor amigo aqui.

1. Adicione um breakpoint na linha de código que você quer que o terminal pare:

  ```
  class Exemplo():

    def run_feature(self):
      some_variable = some_value

      import ipdb; ipdb.set_trace() # Adicione essa linha em qualquer parte do código

      some_other_variable = some_function(some_variable)
  ```

1. Rode o pytest em modo debug:

  ```
  python3 -m pytest -sv
  ```

1. Quando o código passar pela linha do `ipdb`, o interpretador Python vai se abrir pra você e você poderá ver todas as variáveis disponíveis naquele ponto do código, como se você tivesse executando linha a linha.

1. Rode o que quiser rodar, verifique o que quiser verificar. Se quiser que o código continue rodando linha a linha, digite `j` no terminal. Caso queira que o código termine de rodar por completo (até o próximo breakpoint), digite `n` no terminal.

1. Dúvidas? O restante da equipe pode te ajudar, faça uma pergunta no canal do projeto no Slack.

### Como rodar todos os testes?

Antes de submeter um PR, é bom garantir que as suas mudanças não introduziram bugs em outras partes do código. Para isso, sempre rode **todos** os testes antes do commit final:

```
python3 -m pytest

# Ou ainda (pra ficar mais verbose)

python3 -m pytest -sv
```

Alternativamente, use o comando `make` para rodar todos os testes:

```
make test
```

Mas cuidado: esse comando apaga os containers Docker deste projeto que estejam existentes ou ativos e recria tudo do zero.
