# API Secretmanager-Access

## Aplicação

Esta aplicação tem o objetivo de fazer acesso ao AWS Secret Manager, armazenar as secrets no Redis e envia-la como resposta. Com esse fluxo, você não precisaria fazer o acesso ao AWS Secret Manager a todo momento, aumentando seu custo de operação, sendo necessário apenas utilizar essa API para que você tenha o retorno dos dados, e assim diminuíndo seu custo com operação. Qualquer secret pode ser acessada mediante a essa API, não sendo necessário uma configuração para que seja acessado apenas uma determinada secret.

A segurança das secrets que ficam armazenadas no Redis, é feito somente internamente entre a API e o serviço do Redis, dessa forma somente a API com essa configuração de redes do Docker poderia fazer o acesso ao Redis.

Toda a aplicação pode rodar dentro de um contâiner Docker, junto com o Docker-Compose para que seja feito o build completo da aplicação.

## API Secret Manager

### Documentação API

Essa API foi desenvolvida com o módulo do Flask Restful, desta forma ela atende a todas as necessidades RestFul que uma API de microserviço necessitária. Ela pode ser feito o acesso por qualquer outro microserviço que necessita-se de uma determinada secret, independente da secret que o microserviço necessitá, sendo necessário apenas informar qual a secret, aws_login, aws_secret e region que essa secret está armazenada.

#### EndPoint: '/getsecret'

Este EndPoint serve para buscar o secret dentro do Redis, ou caso não exista, diretamente no AWS Secret Manager.

##### PayLoad:

```
{
    'aws_login': 'STRING', -> AWS Login Key
    'aws_secret': 'STRING', -> AWS Login Secret Key
    'aws_region': 'STRING', -> AWS Region Secret
    'aws_secret_name': 'STRING' ->  AWS Secret Manager (Secret Name)
}    
```

#### EndPoint: '/remove'

Este EndPoint serve deletar alguma secret que foi armazenada dentro do Redis. Sempre que você atualizar alguma Secret dentro do AWS Secret Manager é necessário deletar ela também no Redis.

##### PayLoad:

```
{
    'aws_login': 'STRING', -> AWS Login Key
    'aws_secret_name': 'STRING' ->  AWS Secret Manager (Secret Name)
}    
```

#### EndPoint: '/removeall'

Este EndPoint serve deletar todas as secrets armazenadas dentro do Redis.

##### PayLoad:

```
{
    'redis_password': 'STRING' -> Redis Password
}    
```


#### Variáveis de Ambiente API

Para configurar as variáveis de ambiente desta aplicação é necessário modificar, dependendo da forma que irá executar a aplicação, Docker-Compose ou Dockerfile as variáveis de ambiente, sendo elas descritas abaixo:

```
FLASK_ENV -> Flask Environment
REDIS -> Redis URK
REDIS_PASSWORD -> Redis Password
LOG_LEVEL -> Logger Level Info
PORT -> Porta de execução da aplicação
```

### Estrutura dos Dados

Esta aplicação foi estruturada pensando de maneira simples e fácil de dar manutenção, porntato sendo da seguinte maneira:

```
api-start.py
src/
    - controller
        - secret
            getsecret.py
            remove.py
            removeAll.py
    - dao
        - aws_connect.py
        - dbConn.py
    - config
        - aws_regions.py
```

### Dependências API

Para rodar essa aplicação é necessário ter o Python 3.7.2, Docker, Docker-Compose e junto com eles instalar as dependências que estão descritar dentro do **requirements.txt**.

[Python 3.7.2](https://www.python.org/downloads/release/python-372/)

Para instalar os módulos necessários para o Python é necessário rodar o comando abaixo:

```pip3 install -r requirements.txt```

Este comando irá instalar as seguintes dependências:

```
boto3
python-decouple
redis
Flask-RESTful
Flask
json
```

### Execução da Aplicação

Para se executar essa aplicação, apenas é necessário fazer todas as configurações propostas acima e após isto, executar com os seguinte comandos:

```
$ sudo docker build -t IMAGE_NAME:TAG .
$ sudo docker run -dti -p 3000:3000 IMAGE_NAME
```

## Redis

### Documentação Redis

O Redis neste projeto está configurado para armazenar os dados que são retornados do AWS Secret Manager desta forma não é necessário fazer acesso a todo momento do AWS Secret Manager, sendo necessário apenas um acesso e após isso sua secret será armazenada no Redis, e acessos posteriores serão feitos com as secrets armazenadas no redis.

Para maiores informações sobre o Redis em Python, segue o link abaixo:

[Redis Python](https://pypi.org/project/redis/)

Para configurar as a senha de acesso ao Redis desta aplicação é necessário modificar no Docker-Compose o comando de inicio desta aplicação, sendo elas descritar abaixo:

```
redis-server --requirepass {REDIS PASSWORD}
```

## Execução da aplicação completa

Essa aplicação foi desenvolvida para ser executada em cima de um contâiner, mais especificamente Docker, porém para que ele funcione perfeitamente é necessário que seja executado via docker-compose apenas uma vez, sendo o ambiente totalmente configurado a partir do docker-compose. Para que a aplicação execute corretamente é necessário que seja feita a configuração das variáveis de ambiente corretamente como descrita acima em cada serviço que irá executar, após essa configuração é necessário executar os passos abaixo para que a aplicação execute.

### Instalação do Docker Linux, Docker-Compose Linux e Python 3.7.2

O tutorial de instalação do Docker esta descrito no site da própria Docker, o mesmo vale para o docker-compose.

[Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
[Docker-Compose](https://docs.docker.com/compose/install/)

### Inicialização da Aplicação

Para que a aplicação seja iniciada é necessário estar na pasta raiz da aplicação e executar os seguinte comandos:

```
$ sudo docker-compose build
$ sudo docker-compose up -d
```