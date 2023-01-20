# Kubernetes - APIs with BFF

The application implements two APIs (Api1, Api2) with an api-gateway (BFF). All trafic is handled by BFF. BFF gets responces from API1 and API1 from API2. API2 randomly raises 500 error.

Api1 has implemented a retry policy, in case of failure:
    - requests are repeated with the exponentially increasing wait time, the wait time starts from 1s, up to 8s, then 8s.
    - requestes are stopped after 5 attempts

API is available at URI 'localhost/api1' 


Follow these steps to deploy the application:
---

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

`kubectl apply -f <bff-deployment-file.yml>`
    
`kubectl apply -f <api1-deployment-file.yml>`

`kubectl apply -f <api2-deployment-file.yml>`
    
`kubectl apply -f <ingress-file.yml>`
  
For `task3` as the current directory, run:
  
```
    kubectl apply -f ./k8s/api-gateway.yml -f ./k8s/api1.yml -f ./k8s/api2.yml -f ./k8s/ingress.yml
```

