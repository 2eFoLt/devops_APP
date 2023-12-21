docker system prune -a -f
docker network create -d bridge devops_net
docker run --name=devops_db -d --network="devops_net" -p 3306:3306 -h db 2efolt/devops_db
docker run --name=devops_app -d --network="devops_net" -p 5000:5000 2efolt/devops_app