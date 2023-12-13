docker network create -d bridge devops_net || true
docker run -d -p 5000:5000 --network devops_net 2efolt/devops_app
docker run -d -h db --network devops_net 2efolt/devops_db
