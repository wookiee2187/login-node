#creates pod with login-node image
from kubernetes import client, config, utils
import os
import pprint 
import time
from pyhelm.chartbuilder import ChartBuilder 
from pyhelm.tiller import Tiller 
import subprocess

def main():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    k8s_client = client.ApiClient()
    utils.create_from_yaml(k8s_client, "deployNservice.yaml")
    utils.create_from_yaml(k8s_client, "tconfig.yaml")
    k8s_api = client.ExtensionsV1beta1Api(k8s_client)        	
    deps = k8s_api.read_namespaced_deployment_status(name 
    = "login-node-n", namespace ="default")
    pp = pprint.PrettyPrinter(indent =4)
    while(deps.status.available_replicas != 1):
        k8s_api = client.ExtensionsV1beta1Api(k8s_client)
        deps = k8s_api.read_namespaced_deployment_status(name
        = "login-node-n", namespace ="default")
    print("DEPLOYMENT CREATED")
    serv = v1.read_namespaced_service(name = "login-node-service", namespace = "default")
    pp.pprint(serv.spec.ports[0].node_port)
    bashcmd ="(kubectl get pod -l app=login-node-n -o jsonpath='{.items[0].metadata.name}')"
    pod_name2 = subprocess.check_output(bashcmd, shell=True)
    podsy = v1.read_namespaced_pod(pod_name2,"default")
    nodey = v1.read_node(podsy.spec.node_name)
    pp.pprint(nodey.status.addresses[0].address)
if __name__ == '__main__':
    main()
