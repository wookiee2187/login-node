#creates pod with login-node image
from kubernetes import client, config, utils
import kubernetes.client
from kubernetes.client.rest import ApiException
import os, sys
import pprint 
import time
import subprocess, yaml
from flask import Flask, flash, redirect, render_template, request
from random import randint
from jinja2 import Environment, FileSystemLoader

def main():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    k8s_client = client.ApiClient()
    k8s_api = client.ExtensionsV1beta1Api(k8s_client)
    pp = pprint.PrettyPrinter(indent =4)
    try:
    	# checks if deployment, service, configmap already created
        check = k8s_api.read_namespaced_deployment_status(name= "login-node-n",namespace ="default")
        print("deployment already exists")
    except Exception:
        pass
        # rendering template and creating configmap
        config_data = yaml.load(open('vals.yaml'),Loader=yaml.FullLoader)
        #itemp_up = render_template('condor_config.local.j2', request_name = "request",inventory_hostname = "hostname")
        env = Environment(loader = FileSystemLoader('./templates'), trim_blocks=True, lstrip_blocks=True)
        template = env.get_template('condor_config.local.j2')
        temp_up = template.render(config_data)
        name = 'temcon'
        namespace = 'default'
        body = kubernetes.client.V1ConfigMap()
        body.data = dict([("condor_config.local" ,temp_up)])
        body.metadata = kubernetes.client.V1ObjectMeta()
        body.metadata.name = name
        configuration = kubernetes.client.Configuration()
        api_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(configuration))
        try:
            api_response = api_instance.create_namespaced_config_map(namespace, body)
        except ApiException as e:
            print("Exception when calling CoreV1Api->create_namespaced_config_map: %s\n" % e)
        #creating deployment, service, and configmap 
        utils.create_from_yaml(k8s_client, "deployNservice.yaml")
        utils.create_from_yaml(k8s_client, "tconfig.yaml")
        # waits till deployment created
        deps = k8s_api.read_namespaced_deployment_status(name = "login-node-n", namespace ="default")
        while(deps.status.available_replicas != 1):
            k8s_api = client.ExtensionsV1beta1Api(k8s_client)
            deps = k8s_api.read_namespaced_deployment_status(name= "login-node-n", namespace ="default")
        print("DEPLOYMENT CREATED")
    dep = k8s_api.read_namespaced_deployment(name = "login-node-n", namespace = "default")
    pp.pprint(dep)
    serv = v1.read_namespaced_service(name = "login-node-service", namespace = "default")
    pp.pprint(serv.spec.ports[0].node_port)
    list_pods = v1.list_namespaced_pod("default")
    pod = list_pods.items[0]
    node = v1.read_node(pod.spec.node_name)
    pp.pprint(node.status.addresses[0].address)
if __name__ == '__main__':
    main()
