echo "Starting sentilo..."
sentilo-core/build_sentilo_docker_image.sh
sentilo-core/start_sentilo_docker.sh

echo "Generating certs for ELK..."
docker-compose -f ELK/docker-compose_gen-cert.yml up -d;

echo "Starting ELK...";
docker-compose -f ELK/docker-compose.yml up -d;