#creates pod with login-node image
from kubernetes import client, config, utils
import os, sys
import pprint 
import time
import subprocess
from flask import Flask, render_template

def main():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    k8s_client = client.ApiClient()
    k8s_api = client.ExtensionsV1beta1Api(k8s_client)
    pp = pprint.PrettyPrinter(indent =4)
    check = k8s_api.read_namespaced_deployment_status(name
    = "login-node-n", namespace ="default")
    if check != None:
        serv = v1.read_namespaced_service(name = "login-node-service", namespace = "default")
        pp.pprint(serv.spec.ports[0].node_port)
        list_pods = v1.list_namespaced_pod("default")
        pod = list_pods.items[0]
        node = v1.read_node(pod.spec.node_name)
        pp.pprint(node.status.addresses[0].address)
        sys.exit(0)
    utils.create_from_yaml(k8s_client, "deployNservice.yaml")
    utils.create_from_yaml(k8s_client, "tconfig.yaml")
    deps = k8s_api.read_namespaced_deployment_status(name 
    = "login-node-n", namespace ="default")
    while(deps.status.available_replicas != 1):
        k8s_api = client.ExtensionsV1beta1Api(k8s_client)
        deps = k8s_api.read_namespaced_deployment_status(name
        = "login-node-n", namespace ="default")
    print("DEPLOYMENT CREATED")
    serv = v1.read_namespaced_service(name = "login-node-service", namespace = "default")
    pp.pprint(serv.spec.ports[0].node_port)
    list_pods = v1.list_namespaced_pod("default")
    pod = list_pods.items[0]
    node = v1.read_node(pod.spec.node_name)
    pp.pprint(node.status.addresses[0].address)
    render_template('condor_config.local.j2', request_name = "request", inventory_hostname = "hostname")
if __name__ == '__main__':
    main()
