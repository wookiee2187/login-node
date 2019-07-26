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
    deps = k8s_api.read_namespaced_deployment(name 
    = "login-node-n", namespace ="default")
    pod = v1.read_namespaced_pod(name = MY_POD_NAME, namespace = "default")
    pp = pprint.PrettyPrinter(indent =4)
    pp.pprint(deps.status)
    pp.pprint(pod)
    print(deps.status.available_replicas)
    passwd = os.getenv("PASSWDFILE")
    while(deps.status.available_replicas != 1):
        #print(pod_ip)
        #print(node_name)
    	print("Deployment not created")

if __name__ == '__main__':
    main()
