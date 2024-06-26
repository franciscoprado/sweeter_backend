# Sweeter - REST API em Flask

Projeto que fornece uma API REST para a aplicação de microbloggin chamada Sweeter, feita em Angular.

![Diagrama da aplicação Sweeter](diagrama-Sweeter.png "Diagrama da aplicação Sweeter")

O objetivo aqui é apresetar uma API implementada seguindo o estilo REST.

As principais tecnologias que serão utilizadas aqui:
 - [Flask](https://flask.palletsprojects.com/en/2.3.x/)
 - [SQLAlchemy](https://www.sqlalchemy.org/)
 - [OpenAPI3](https://swagger.io/specification/)
 - [SQLite](https://www.sqlite.org/index.html)

## Arquivo .env

É preciso criar um arquivo contendo as variáveis usadas na aplicação.

Copie o arquivo `.env.example` presente na raiz do projeto, cole ele no mesmo lugar e renomeie para `.env`, removendo o .example do final.

## Chave da API da TinyURL

Antes, é preciso adicionar a chave de API do TinyURL, serviço de encurtamento de URLs.
Tal chave deverá ser adicionada ao arquivo `.env` presente na pasta raiz do projeto:

`TINYURL_API_KEY=<sua-chave-aqui>`

A chave estará presente no envio do projeto, junto com os links do GitHub dos repositórios.

## Carregar massa de dados de testes (seed)

É possível usar uma massa de dados para pré-visualizar um conteúdo na aplicação. Para isso, é preciso executar o comando a seguir:

```
python -m seed
```

O comando deverá ser executado de dentro do ambiente virtual, caso esteja sendo usado.

---
### Instalação

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

---
### Executando o servidor


Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

---
### Acesso no browser

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

---
## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t sweeter-rest-api .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5000:5000 sweeter-rest-api
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador.



### Alguns comandos úteis do Docker

>**Para verificar se a imagem foi criada** você pode executar o seguinte comando:
>
>```
>$ docker images
>```
>
> Caso queira **remover uma imagem**, basta executar o comando:
>```
>$ docker rmi <IMAGE ID>
>```
>Subistituindo o `IMAGE ID` pelo código da imagem
>
>**Para verificar se o container está em exceução** você pode executar o seguinte comando:
>
>```
>$ docker container ls --all
>```
>
> Caso queira **parar um conatiner**, basta executar o comando:
>```
>$ docker stop <CONTAINER ID>
>```
>Subistituindo o `CONTAINER ID` pelo ID do conatiner
>
>
> Caso queira **destruir um conatiner**, basta executar o comando:
>```
>$ docker rm <CONTAINER ID>
>```
>Para mais comandos, veja a [documentação do docker](https://docs.docker.com/engine/reference/run/).