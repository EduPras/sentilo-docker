#!/bin/bash
# variables used into the docker-compose.yml
export SENTILO_VERSION="2.0.0"
export SENTILO_CONF_DIR="./conf"
export REDIS_VERSION="6.2.6-alpine"
export MONGO_VERSION="4.4.2-bionic"
export KBN_CONF_PATH=/usr/share/kibana/config
export ELASTIC_CONF_PATH=/usr/share/elasticsearch/config
export LOGSTASH_CONF_PATH=/usr/share/logstash/config
export ELK_VERSION=8.8.1

MODE="$1"
if [[ "$MODE" == "up" ]]; then
    MODE="up -d"
fi
SERVICE="$2"
ALL=""
# Initial platform image conf files dir
# All them had been configured to run into docker ecosystem
# They are mandatory

source ./.envsrc

# Start sentilo-core
if [[ "$SERVICE" == "$ALL" || "$SERVICE" == "sentilo" ]]; then
    echo "Starting sentilo-core..."
    export COMPOSE_PROJECT_NAME="sentilo200"
    docker compose -f ./sentilo-core/docker-compose.yml $MODE
fi
# Start ELK
if [[ "$SERVICE" == "$ALL" || "$SERVICE" == "elk" ]]; then
    echo "Starting ELK..."
    export COMPOSE_PROJECT_NAME=es_sentilo
    docker compose -f ./ELK/docker-compose.yml $MODE
fi
# Start monitoring
if [[ "$SERVICE" == "$ALL" || "$SERVICE" == "monitoring" ]]; then
    export COMPOSE_PROJECT_NAME=monitoring
    docker compose -f ./monitoring/docker-compose.yml $MODE
fi

# Start reverse proxy
if [[ "$SERVICE" == "$ALL" || "$SERVICE" == "proxy" ]]; then
    export COMPOSE_PROJECT_NAME=proxy
    docker compose -f ./proxy/docker-compose.yml $MODE
fi