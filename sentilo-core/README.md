# sentilo-core
Esse projeto docker roda os módulos relacionados a sentilo, como:
* redis
* MongoDB
* Agents 
* Sentilo Catalog Web
* Sentilo Server

Configurações relacionadas a sentilo 

## Multitenant 
Caso o container seja recriado do zero, é necessário modificar o arquivo
_usr/local/tomcat/webapps/sentilo-catalog-web/WEB-INF/web.xml_ de acordo com
a documentação da sentilo.

O usuário **sadmin** é quem controla as organizações, já outros usuários, incluindo admins
devem fazer login pela rota de sua respectiva organização.