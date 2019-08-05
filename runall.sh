#!/bin/bash
set -e
#Start the container
sudo docker run -d -v $(pwd)/tasks.conf:/etc/vc3/tasks.conf -v $(pwd)/task/HandleRequests.py:/usr/lib/python2.7/site-packages/vc3master/plugins/task/HandleRequests.py -v $(pwd)/task/HandleHeadNodes.py:/usr/lib/python2.7/site-packages/vc3master/plugins/task/HandleHeadNodes.py --rm --name vc3 virtualclusters/omnicontainer
echo "sleep 60s for startup..."
sleep 10

vc3client='sudo docker exec vc3 vc3-client'


# create the resource
$vc3client resource-create --owner lincolnb --accesstype batch --accessmethod ssh --accessflavor condor --accesshost slate-micro-condor.slateci.io --accessport 22 --node generic-nodesize --description "SLATE CI" --displayname "SLATE" --url "https://slatecio.io" --pubtokendocurl "https://slateci.io" --organization "SLATECI" slate-condor --public


# create the user
$vc3client user-create --firstname Lincoln --lastname Bryant --email lincolnb@uchicago.edu --displayname 'Lincoln Bryant' --identity_id c887eb90-d274-11e5-bf28-779c8998e810 --institution UChicago --sshpubstring 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCo3a7EUYD8qEwMBYlOzNFXXA55Lpcbgl5qlmiuwXdrOV/APr2uoIw3vYix4yYPTQPr8trfscX/NaDpVAhivlmd31ylGBjIaK/Qo0L2aTv38m9++dfflf9AdUtKdMIfddBNyOh5FlTzropoElvdVulJyGIJv6+rQeDMyaKt5HGOJ8yg+xtqcTDbfzHWVK2POP3PlcQsMg+5MkAJQDV2gvO3NxRF+ureedEtSmvEuJNUIGatM3l09FfbU9nOM9T+8xrz9tTJLMhB7QWXcd8V5IFMo+fCoSJG4qKPUrkqIHXvpNRmQ8CvEeVxwgHl/3R+Jtg8OYs7P5mmoKw4r+OBAYhL lincolnb@nam-shub' lincolnb

# create the allocation
$vc3client allocation-create --owner lincolnb --resource slate-condor --accountname lincolnb --description "SLATE Condor" --displayname lincolnb-slate lincolnb.slate-condor

# create the project and add the allocation
$vc3client project-create --owner lincolnb --members lincolnb lincolnb
$vc3client project-addallocation lincolnb lincolnb.slate-condor


# create the virtual cluster template
$vc3client nodeset-create --owner lincolnb --node_number 1 --app_type htcondor --app_role worker-nodes --app_killorder newest --displayname="htcondor" lincolnb-htcondor-nodeset
$vc3client cluster-create --owner lincolnb --description "htcondor" --displayname="htcondor" lincolnb-htcondor-cluster --public
$vc3client cluster-addnodeset lincolnb-htcondor-cluster lincolnb-htcondor-nodeset

# create the head node template -- is this generated dynamically?
#$vc3client nodeset-create --owner lincolnb --node_number 1 --app_type htcondor --app_role head-node --displayname="htcondor headnode" vc3-headnode-htcondor

# create the request
$vc3client request-create --cluster lincolnb-htcondor-cluster --project lincolnb --allocations lincolnb.slate-condor kube-test 
