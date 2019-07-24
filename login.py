#creates pod with login-node image
from kubernetes import client, config, utils

def main():
    config.load_kube_config()
    k8s_client = client.ApiClient()
    utils.create_from_yaml(k8s_client, "deployNservice.yaml")
    k8s_api = client.ExtensionsV1beta1Api(k8s_client)
    print("Deployment created")

if __name__ == '__main__':
    main()
