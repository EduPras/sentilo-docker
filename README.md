# sentilo-docker

## Setup

### Certificados
Antes de iniciar o projeto é necessário que as chaves **privada, pública e de requisição**
estejam localizadas em **certs/server**, sendo nomeadas, respectivamente como: 
server-key.pem, server-cert.pem e server-req.pem.

### Variáveis de ambiente
Na raíz do projeto, adicione um arquivo **.envsrch**, com os seguintes atributos:
```bash
export MONGO_INITDB_ROOT_USERNAME=xxx
export MONGO_INITDB_ROOT_PASSWORD=xxx
export ELASTIC_PASSWORD=xxx
export LOGSTASH_USER=xxx
export LOGSTASH_PASSWORD=xxx
export KIBANA_USER=xxx
export KIBANA_PASSWORD=xxx
```

## Inicialização 
Siga a seguinte ordem, sempre olhando a documentação de cada subprojeto:

1. Iniciar os subprojetos ELK e grafana
2. Iniciar o subprojeto sentilo-core

Sensores que utilizam da LoraWAN como rede para envio de dados e utilizam-se do 
gateway da TTN, é necessário um script que converte requisições MQTT para HTTP.
Esses scripts ainda estão em desenvolvimento, no momento é necessário um script para
cada estação.

> TODO: Fazer um único algoritmo que recebe dados de inúmeras estações 
e realizar o _parser_ corretamente de todos.
> TODO: Adicionar secrets do Redis nas variáveis de ambiente.