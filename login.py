#creates pod with login-node image
from kubernetes import client, config, utils
import os
import pprint 
import time
from pyhelm.chartbuilder import ChartBuilder 
from pyhelm.tiller import Tiller 

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
#    pp.pprint(deps)
#    print(deps.status.available_replicas)
    while(deps.status.available_replicas != 1):
        k8s_api = client.ExtensionsV1beta1Api(k8s_client)
        deps = k8s_api.read_namespaced_deployment_status(name
        = "login-node-n", namespace ="default")
    print("DEPLOYMENT CREATED")

if __name__ == '__main__':
    main()
