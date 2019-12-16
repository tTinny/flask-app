Working with Docker Images

Downloading the file from docker hub.

  docker pull praks1310/flask1:latest

Run a container from the Docker Image using a port

  docker run -d --name flask_app -p 5000:5000 praks1310/flask1

    -d is to detach the terminal from the container process (run it in the background)
    --name is to specify a name for the container
    -p local:container is to forward traffic from a local port to a port in the container

Checking the application is working

  open http://localhost:5000
  
  open http://localhost:5000/result  OR
  
  curl http://localhost:5000
  
  curl http://localhost:5000/result

Verify container logs with docker logs

  docker logs flask_app

Stop and remove the local container

  docker stop flask_app && docker rm flask_app



Working with kubernetes

Deploying to Kubernetes

Creating a deployment using kubectl

   kubectl apply -f f-pod.yml

Exposing a service

  kubectl expose -f flask-svc.yml --type=NodePort

Verify container logs with kubectl logs

  kubectl logs flask_app

Checking the application is working

  open http://localhost:5000
  
  open http://localhost:5000/result OR
  
  curl http://localhost:5000
  
  curl http://localhost:5000/result
