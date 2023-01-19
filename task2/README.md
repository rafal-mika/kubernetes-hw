# Kubernetes - Secrets

The application provides API with Postgre database.

Database connection string is passed as environment variable.

Database credentials are stored in Kubernetes secrets object.

There are available two method do test database connection

To check database version, use `localhost/db-version`

To check connection status, use `localhost/is-db-connected`

To deploy the application, follow these steps:

1. Set up Ingress Controller (if you don't have).

Ingress is configured to use NGNIX ingress controller. You can use `kubectl` command:
  
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.5.1/deploy/static/provider/cloud/deploy.yaml
```
  
2. Create API image:
      
Go to `compose.yml` directory and run:
	
```
    docker-compose build
```
  
3. Apply deployment and ingress:

`kubectl apply -f <secrets-manifest-file.yml>`
    
`kubectl apply -f <api-deployment-file.yml>`

`kubectl apply -f <volume-claim-file.yml>`

`kubectl apply -f <db-deployment-file.yml>`
    
`kubectl apply -f <ingress-file.yml>`
  
For `task2` as the current directory, run:
  
```
   kubectl apply -f ./k8s/secrets.yml -f ./k8s/api.yml -f ./k8s/db-storage.yml -f ./k8s/db.yml -f ./k8s/ingress.yml
```

