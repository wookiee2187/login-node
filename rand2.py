    def create_conf_users(self, request):
        config.load_kube_config(config_file = '/etc/kubernetes/admin.conf')
        core_v1_api = kubernetes.client.CoreV1Api()
        body = kubernetes.client.V1ConfigMap(apiversion = 'v1', kind = 'ConfigMap', metadata = kubernetes.client.V1ObjectMeta(name = "new-config-" + str(request.name), namespace = "default", d
ata = {'tconfig-file.conf':'|+ 
   slateci:x:1000:1000::/home/slateci:/bin/bash:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQClkGpJ1+B2qPc5gtoywRsKBTj2wO6CR0ywqKTvcdTdFnqnStYsCKD8SL14MwNCKHHk70jv1yeIyJRJD1ctfrrc7oaY5hj+zUZgavmo8pfnBiEsTPEVPmPocLdGfsH7NXuRuuTLk+3snBW7N3S22YVJytXKrFwLjigeA+SltquN6t3vHBepON8k2VKxNfZXROhiOI4vf7qW5/G8i75qJ4dWuGvAoh9dceYFwNcL1aZGPo/LVaHm0eb8/o2aNQuhAWfwSRz/7Lz9vjflaJAQWjV1P8GYCDdXfWnzD7tk6qWOoPR2iUgOckF+rJPMCfsMnbsu9OiNliftreOzFqL3q6TvXlDNz5brgOnIDCgFC20ZhNRhLhjC+PvdmIi5VVoY3NjHrKzMKT2tkGpI1WGr9Xl89pUQ7tw9QblmOWW0SHl9hwaG/uKrJz3zuDZcvr9eeMk8Qr5OK/3hDW0+/ddXTy1JU3QA7p/J42jA4Jfv6eW6jAbKTa99luAwQ76N3vodU30= nehalingareddy@Nehas-MacBook-Pro.local 
   neha:x:1003:1003:/home/neha::/bin/bash:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQClkGpJ1+B2qPc5gtoywRsKBTj2wO6CR0ywqKTvcdTdFnqnStYsCKD8SL14MwNCKHHk70jv1yeIyJRJD1ctfrrc7oaY5hj+zUZgavmo8pfnBiEsTPEVPmPocLdGfsH7NXuRuuTLk+3snBW7N3S22YVJytXKrFwLjigeA+SltquN6t3vHBepON8k2VKxNfZXROhiOI4vf7qW5/G8i75qJ4dWuGvAoh9dceYFwNcL1aZGPo/LVaHm0eb8/o2aNQuhAWfwSRz/7Lz9vjflaJAQWjV1P8GYCDdXfWnzD7tk6qWOoPR2iUgOckF+rJPMCfsMnbsu9OiNliftreOzFqL3q6TvXlDNz5brgOnIDCgFC20ZhNRhLhjC+PvdmIi5VVoY3NjHrKzMKT2tkGpI1WGr9Xl89pUQ7tw9QblmOWW0SHl9hwaG/uKrJz3zuDZcvr9eeMk8Qr5OK/3hDW0+/ddXTy1JU3QA7p/J42jA4Jfv6eW6jAbKTa99luAwQ76N3vodU30= nehalingareddy@Nehas-MacBook-Pro.local
   rand:x:1004:1004:/home/rand::/bin/bash:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQClkGpJ1+B2qPc5gtoywRsKBTj2wO6CR0ywqKTvcdTdFnqnStYsCKD8SL14MwNCKHHk70jv1yeIyJRJD1ctfrrc7oaY5hj+zUZgavmo8pfnBiEsTPEVPmPocLdGfsH7NXuRuuTLk+3snBW7N3S22YVJytXKrFwLjigeA+SltquN6t3vHBepON8k2VKxNfZXROhiOI4vf7qW5/G8i75qJ4dWuGvAoh9dceYFwNcL1aZGPo/LVaHm0eb8/o2aNQuhAWfwSRz/7Lz9vjflaJAQWjV1P8GYCDdXfWnzD7tk6qWOoPR2iUgOckF+rJPMCfsMnbsu9OiNliftreOzFqL3q6TvXlDNz5brgOnIDCgFC20ZhNRhLhjC+PvdmIi5VVoY3NjHrKzMKT2tkGpI1WGr9Xl89pUQ7tw9QblmOWW0SHl9hwaG/uKrJz3zuDZcvr9eeMk8Qr5OK/3hDW0+/ddXTy1JU3QA7p/J42jA4Jfv6eW6jAbKTa99luAwQ76N3vodU30= nehalingareddy@Nehas-MacBook-Pro.local'}
        try:
            api_response = api_instance.create_namespaced_config_map(namespace, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
        except ApiException as e:
            print("Exception when calling CoreV1Api->create_namespaced_config_map: %s\n" % e)
