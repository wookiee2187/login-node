#!/bin/bash
kubectl delete deployment login-node-n
kubectl delete service login-node-service
kubectl delete configmap new-config
kubectl delete configmap temcon-kube-test
