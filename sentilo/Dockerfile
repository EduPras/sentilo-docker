FROM maven:latest 

FROM tomcat:9.0.58-jdk8-temurin-focal as prod
LABEL maintainer="luismariotti1"
USER root

RUN mkdir /sentilo	
WORKDIR /sentilo

# install packages
RUN apt-get clean && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    maven \
    supervisor \
    vim
 
# source code
RUN git clone https://github.com/sentilo/sentilo.git . && \
    git checkout v1.9.0

# change permission for execute script
RUN chmod +x -R scripts

# configure mongo for docker network
RUN sed -i "s/.*catalog.mongodb.host=.*/catalog.mongodb.host=mongo-server/" /sentilo/sentilo-agent-alert/src/main/resources/properties/catalog-config.properties
RUN sed -i "s/.*catalog.mongodb.host=.*/catalog.mongodb.host=mongo-server/" /sentilo/sentilo-catalog-web/src/main/resources/properties/catalog-config.properties

# # configure redis for docker network
RUN sed -i "s/.*jedis.pool.host=.*/jedis.pool.host=redis-server/" sentilo-platform/sentilo-platform-service/src/main/resources/properties/jedis-config.properties
RUN sed -i "s/.*jedis.pool.host=.*/jedis.pool.host=redis-server/" sentilo-agent-alert/src/main/resources/properties/jedis-config.properties
RUN sed -i "s/.*jedis.pool.host=.*/jedis.pool.host=redis-server/" sentilo-agent-relational/src/main/resources/properties/jedis-config.properties
RUN sed -i "s/.*jedis.pool.host=.*/jedis.pool.host=redis-server/" sentilo-agent-location-updater/src/main/resources/properties/jedis-config.properties

# prepare compile script to run non interactively
RUN sed -i "s/^read$/#read/" ./scripts/buildSentilo.sh

# compile sentilo
RUN ./scripts/buildSentilo.sh

# copiar para webapps
RUN cp sentilo-catalog-web/target/sentilo-catalog-web.war /usr/local/tomcat/webapps

# # configure opentsdb for docker network
# RUN sed -i "s/.*catalog.mongodb.host=.*/catalog.mongodb.host=mongo-server/" sentilo-agent-historian/src/main/resources/properties/catalog-config.properties
# RUN sed -i "s/.*jedis.pool.host=.*/jedis.pool.host=redis-server/" sentilo-agent-historian/src/main/resources/properties/jedis-config.properties
# RUN sed -i "s/opentsdb.url=http:\/\/127.0.0.1:4242/opentsdb.url=http:\/\/opentsdb-server:4242/g" sentilo-agent-historian/src/main/resources/properties/historian-config.properties

# #configure elasticsearch for docker network
# RUN sed -i "s/.*catalog.mongodb.host=.*/catalog.mongodb.host=mongo-server/" sentilo-agent-activity-monitor/src/main/resources/properties/catalog-config.properties
# RUN sed -i "s/.*jedis.pool.host=.*/jedis.pool.host=redis-server/" sentilo-agent-activity-monitor/src/main/resources/properties/jedis-config.properties
# RUN sed -i "s/elasticsearch.url=http:\/\/localhost:9200/elasticsearch.url=http:\/\/agent-proxy:9000/g" sentilo-agent-activity-monitor/src/main/resources/properties/monitor-config.properties

# execute permission for sentilo server
RUN chmod +x sentilo-platform/sentilo-platform-server/target/appassembler/bin/sentilo-server

# create folder to script
# RUN mkdir /sentilo/persistence-agents

# # copy script that run agents
# COPY agents-install.sh /sentilo/persistence-agents

# # give execute permission to script
# RUN chmod +x /sentilo/persistence-agents/agents-install.sh

# supervisor conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# ENTRYPOINT ["/usr/bin/supervisord"]
CMD [ "/usr/bin/supervisord" ]

EXPOSE 8080
EXPOSE 8081