# Kubernetes - two APIs

The application provides two APIs available in `localhost/api1` and `localhost/api2` paths.

To deploy the application, follow these steps:

1. Set up Ingress Controller (if you don't have).

Ingress is configured to use NGNIX ingress controller. You can use `kubectl` command:
  
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.5.1/deploy/static/provider/cloud/deploy.yaml
```
  
2. Create API images:

`docker build -t api1-img <api1-dockerfile-path>` 
    
`docker build -t api2-img <api2-dockerfile-path>` 
  
For `task1` as the current directory, run:
	
```
    docker build -t api1-img ./api1
```
		
```
    docker build -t api2-img ./api2
```
  
3. Apply deployment and ingress:

`kubectl apply -f <api1-deployment-file.yml>`
    
`kubectl apply -f <api2-deployment-file.yml>`
    
`kubectl apply if <ingress-file.yml>`
  
For `task1` as the current directory, run:
  
```
   kubectl apply -f ./k8s/deployment/api1.yml
```

```
   kubectl apply -f ./k8s/deployment/api2.yml
```

```
   kubectl apply if ./k8s/ingress.yml
```
