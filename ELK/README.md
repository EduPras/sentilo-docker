# ELK

## Setup
Ao utilizar o script de inicialização **server.sh**, entre dentro do container do
elastic e execute *bin/elasticsearch-setup-passwords*, de acordo com o arquivo
**.envsrc** da raíz do projeto.

Após estar funcionando corretamente, entre na kibana e crie uma role e user para 
o Logstash, novamente, com as mesmas credenciais colocadas no arquivo **.envsrc**