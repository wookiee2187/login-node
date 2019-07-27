#creates pod with login-node image
from kubernetes import client, config, utils
import os
from os import path
import pprint
import time
from pyhelm.chartbuilder import ChartBuilder 
from pyhelm.tiller import Tiller 

def main():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    k8s_client = client.ApiClient()
    k8s_api = client.ExtensionsV1beta1Api(k8s_client)
    deps = k8s_api.read_namespaced_deployment(name
    = "login-node-n", namespace ="default")
    pod_name = os.environ["HOME"]
    print(pod_name)
    pod = k8s_api.read_namespaced_deployment_status(name = "login-node-n", namespace = "default")
    pp = pprint.PrettyPrinter(indent =4)
    v1 = client.CoreV1Api()
    k8s_client = client.ApiClient()
    serv = v1.read_namespaced_service(name = "login-node-service", namespace = "default")
    pp.pprint(serv.spec.ports[0].node_port)
    os.system("POD=$(kubectl get pod -l app=login-node-n -o jsonpath="{.items[0].metadata.name}"")
    print(POD)
    pp.pprint(deps)
    print os.environ
    config.load_kube_config(
        os.path.join(os.path.expanduser('~'), '.kube', 'config')) 
    print os.environ
    KUBERNETES_HOST = "https://%s:%s" % (os.getenv("KUBERNETES_SERVICE_HOST"), os.getenv("KUBERNETES_SERVICE_PORT"))
    print(KUBERNETES_HOST)

if __name__ == '__main__':
    main()
