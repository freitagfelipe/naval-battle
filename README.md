# Naval battle

- Esse projeto foi desenvolvido para a disciplina de verificação e validação e tem como objetivo praticar o que foi aprendido sobre Test Driven Development e Behavior Driven Development.

## Como foi feito

- O projeto utiliza o [Python](https://www.python.org/) na sua versão 3.10 e o [Pipenv](https://pypi.org/project/pipenv/) para gerenciamento de ambiente virual e dependências. Ademais, o jogo utiliza o [termcolor](https://pypi.org/project/termcolor/) para imprimir colorido durante o jogo, utiliza o [pytest](https://pypi.org/project/pytest/) e [pytest-cov](https://pypi.org/project/pytest-cov/) para execução dos testes e produção da cobertura dos testes e também utiliza o [black](https://pypi.org/project/black/) para a formatação do código.

### Executando com o Pipenv (recomendado)

```sh
$ pipenv install
$ pipenv run start
```

### Executando sem o Pipenv

```sh
$ pip install termcolor
$ python3 main.py
```

### Executando os testes e gerando o coverage com o Pipenv (recomendado)

```sh
$ pipenv install --dev
$ pipenv run test
```

### Executando os testes e gerando o coverage sem o Pipenv

```sh
$ pip install pytest pytest-cov
$ pytest --cov --cov-report=html:coverage_report
```
