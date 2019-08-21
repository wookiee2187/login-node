#!/bin/bash
kubectl delete deployment login-node-n-kube-test --namespace=kube-test
kubectl delete service login-node-service-kube-test --namespace=kube-test
kubectl delete configmap new-config-kube-test --namespace=kube-test
kubectl delete configmap temcon-kube-test --namespace=kube-test
