from kubernetes import client, config, utils
import kubernetes.client
from kubernetes.client.rest import ApiException
import pprint

def main():
	config.load_kube_config()
        pp = pprint.PrettyPrinter(indent =4)
        configuration = kubernetes.client.Configuration()
        api_instance = kubernetes.client.AppsV1Api(kubernetes.client.ApiClient(configuration))
	core_v1_api = client.CoreV1Api()
        namespace = 'default' 
        body = kubernetes.client.V1Deployment() # V1Deployment | 
        body.metadata = kubernetes.client.V1ObjectMeta()
        body.metadata.name = 'login-node-n'
        body.metadata.labels = {'app':'login-node-n'}
	conf_list = []
	conf_list.append(kubernetes.client.V1VolumeMount(name = 'config-vol', mount_path = '/root/tconfig-file.conf',sub_path = 'tconfig-file.conf'))
	conf2_list = []
        volume0 = kubernetes.client.V1Volume(name = 'config-vol', config_map = kubernetes.client.V1ConfigMapVolumeSource(name = 'new-config', items = [kubernetes.client.V1KeyToPath(key = "tconfig-file.conf", path = "tconfig-file.conf")]))
	volume1 = kubernetes.client.V1Volume(name = 'temcon-vol', config_map = kubernetes.client.V1ConfigMapVolumeSource(name = 'temcon', items = [kubernetes.client.V1KeyToPath(key = "condor_config.local", path = "condor_config.local")]))
	print("volumes not")
	env_list = [] 
	env_list.append(kubernetes.client.V1EnvVar(name = 'PASSWDFILE', value = "root/tconfig-file.conf"))
	vol_m_list = []
	vol_m_list.append(kubernetes.client.V1VolumeMount(name = 'config-vol', mount_path = '/root/tconfig-file.conf',sub_path = 'tconfig-file.conf'))
	vol_m_list.append(kubernetes.client.V1VolumeMount(name = 'temcon-vol', mount_path = '/etc/condor/config.d/condor_config.local', sub_path = 'condor_config.local'))
        container0 = kubernetes.client.V1Container(name = 'new-container', env = env_list, image = 'nlingareddy/condor-login', volume_mounts = vol_m_list)
	vol_list = []
	vol_list.append(volume0)
	vol_list.append(volume1)
	cont_list = []
	cont_list.append(container0)
        body.spec = kubernetes.client.V1DeploymentSpec(replicas= 1, selector= kubernetes.client.V1LabelSelector(match_labels= {'app':'login-node-n'}) , template= kubernetes.client.V1PodTemplateSpec(metadata = kubernetes.client.V1ObjectMeta(labels = {'app':'login-node-n'}), spec = kubernetes.client.V1PodSpec(volumes= vol_list, containers = cont_list)))
	serv_list = []
	serv_list.append(kubernetes.client.V1ServicePort(port=22, protocol='TCP'))
	bodys = kubernetes.client.V1Service(metadata= kubernetes.client.V1ObjectMeta(name = 'login-node-service-' + 'request'), spec = kubernetes.client.V1ServiceSpec(type='NodePort', selector={'app':'login-node-n-' + 'request'}, ports=serv_list))
        string_to_append = '    ' + str('user.name') +':x:' + str('i') + ':' + str('i') + ':'+ '/home/' + str('user.name') + '::' + '/bin/bash:' + str('user.sshpubstring') + '\n' + '\n'
        bodyc = kubernetes.client.V1ConfigMap(api_version = 'v1', kind = 'ConfigMap', metadata = kubernetes.client.V1ObjectMeta(name = "new-config-" + str('request.name'), namespace = "default"), data = {'tconfig-file.conf':'|+\nslateci:x:1000:1000::/home/slateci:/bin/bash:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQClkGpJ1+B2qPc5gtoywRsKBTj2wO6CR0ywqKTvcdTdFnqnStYsCKD8SL14MwNCKHHk70jv1yeIyJRJD1ctfrrc7oaY5hj+zUZgavmo8pfnBiEsTPEVPmPocLdGfsH7NXuRuuTLk+3snBW7N3S22YVJytXKrFwLjigeA+SltquN6t3vHBepON8k2VKxNfZXROhiOI4vf7qW5/G8i75qJ4dWuGvAoh9dceYFwNcL1aZGPo/LVaHm0eb8/o2aNQuhAWfwSRz/7Lz9vjflaJAQWjV1P8GYCDdXfWnzD7tk6qWOoPR2iUgOckF+rJPMCfsMnbsu9OiNliftreOzFqL3q6TvXlDNz5brgOnIDCgFC20ZhNRhLhjC+PvdmIi5VVoY3NjHrKzMKT2tkGpI1WGr9Xl89pUQ7tw9QblmOWW0SHl9hwaG/uKrJz3zuDZcvr9eeMk8Qr5OK/3hDW0+/ddXTy1JU3QA7p/J42jA4Jfv6eW6jAbKTa99luAwQ76N3vodU30= nehalingareddy@Nehas-MacBook-Pro.local\n\nneha:x:1003:1003:/home/neha::/bin/bash:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQClkGpJ1+B2qPc5gtoywRsKBTj2wO6CR0ywqKTvcdTdFnqnStYsCKD8SL14MwNCKHHk70jv1yeIyJRJD1ctfrrc7oaY5hj+zUZgavmo8pfnBiEsTPEVPmPocLdGfsH7NXuRuuTLk+3snBW7N3S22YVJytXKrFwLjigeA+SltquN6t3vHBepON8k2VKxNfZXROhiOI4vf7qW5/G8i75qJ4dWuGvAoh9dceYFwNcL1aZGPo/LVaHm0eb8/o2aNQuhAWfwSRz/7Lz9vjflaJAQWjV1P8GYCDdXfWnzD7tk6qWOoPR2iUgOckF+rJPMCfsMnbsu9OiNliftreOzFqL3q6TvXlDNz5brgOnIDCgFC20ZhNRhLhjC+PvdmIi5VVoY3NjHrKzMKT2tkGpI1WGr9Xl89pUQ7tw9QblmOWW0SHl9hwaG/uKrJz3zuDZcvr9eeMk8Qr5OK/3hDW0+/ddXTy1JU3QA7p/J42jA4Jfv6eW6jAbKTa99luAwQ76N3vodU30= nehalingareddy@Nehas-MacBook-Pro.local\n\n'+string_to_append}) 
	try:
            api_response = core_v1_api.create_namespaced_config_map(namespace="default", body = bodyc)
        except ApiException as e:
            print("Exception when calling CoreV1Api->create_namespaced_config_map: %s\n" % e)	
        try:
            api_response = api_instance.create_namespaced_deployment(namespace="default", body=body)
            pp.pprint(api_response)
	    api_response2 = core_v1_api.create_namespaced_service(namespace="default", body=bodys)
	    pp.pprint(api_response2)
        except ApiException as e:
            print("Exception when calling AppsV1Api->create_namespaced_deployment: %s\n" % e)

if __name__ == '__main__':
    main()


