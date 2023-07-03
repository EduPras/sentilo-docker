echo "Starting sentilo..."
docker-compose up -d;

echo "Generating certs for ELK..."
docker-compose -f ELK/docker-compose_gen-cert.yml up -d;

echo "Starting ELK...";
docker-compose -f ELK/docker-compose.yml up -d;