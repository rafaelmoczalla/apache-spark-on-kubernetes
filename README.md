# Tutorial: Apache Spark on Kubernetes
Simple playground for Apache Spark on Kubernetes.

## Prerequisits
1. This project requires Docker Desktop to be installed.
2. Enable a 4 node Kubernetes Cluster in Docker Desktop Settings.

## Quickstart
Check if Kubernetes is running properly.
```bash
kubectl get nodes
```

### Deploy & Start the Apache Spark
Deploy the Spark master.
```bash
kubectl apply -f spark-master.yaml
```
Deploy the Spark workers.
```bash
kubectl apply -f spark-worker.yaml
```
Start the Kubernetes service.
```bash
kubectl apply -f spark-master-service.yaml
```
Check if the Spark master service is created.
```bash
kubectl get services
```
Check if the Spark master is running.
```bash
kubectl get pods
```

Forward the Apache Webserver to your local host & check if you can load the website.
```bash
kubectl port-forward svc/spark-master 8080:8080
curl http://localhost:8080
```

### Delete Apache Spark
Get the deployment names.
```bash
kubectl get deployments --all-namespaces
```
Delete the spark-master & spark-worker.
```bash
kubectl scale deployment spark-worker --replicas=0
kubectl scale deployment spark-master --replicas=0
kubectl delete deployment spark-worker
kubectl delete deployment spark-master
```

Get the service name.
```bash
kubectl get services --all-namespaces
```
Delete the spark-master-service.
```bash
kubectl delete service spark-master
```

## License
Full copyright belongs to me Rafael Moczalla.
