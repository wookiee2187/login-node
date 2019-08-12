#!/bin/bash
set -e
#Start the container
sudo docker run --detach -v $(pwd)/templates:/templates -v ~/.kube/config:/etc/kubernetes/admin.conf  -v $(pwd)/tasks.conf:/etc/vc3/tasks.conf -v $(pwd)/task/HandleHeadNodes.py:/usr/lib/python2.7/site-packages/vc3master/plugins/task/HandleHeadNodes.py --rm --name vc3 virtualclusters/omnicontainer
sudo docker cp  $(pwd)/vals.yaml vc3:/usr/lib/python2.7/site-packages/vc3master/plugins/task 
sudo docker cp $(pwd)/deployNservice.yaml vc3:deployNservice.yaml
sudo docker cp $(pwd)/tconfig.yaml vc3:/tmp/tconfig.yaml
sudo docker cp /Users/nehalingareddy/.ssh/id_rsa vc3:private_key

echo "sleep 60s for startup..."
sleep 10

vc3client='sudo docker exec vc3 vc3-client'


# create the resource
echo "Creating resource..."
#$sudo docker exec -i vc3 cp tmp/tconfig.yaml tconfig.yaml 
#$sudo docker exec -i vc3 chmod 770 tconfig.yaml
$vc3client nodeinfo-create --owner btovar  --displayname="Generic node size, 1core,1GB,1GB" --cores 4 --memory_mb 1000 --storage_mb 1000 generic-nodesize
$vc3client resource-create --owner lincolnb --accesstype batch --accessmethod ssh --accessflavor condor --accesshost slate-micro-condor.slateci.io --accessport 22 --node generic-nodesize --description "SLATE CI" --displayname "SLATE" --url "https://slatecio.io" --pubtokendocurl "https://slateci.io" --organization "SLATECI" slate-condor --public


# create the user
echo "Creating user..."
$vc3client user-create --firstname Lincoln --lastname Bryant --email lincolnb@uchicago.edu --displayname 'Lincoln Bryant' --identity_id c887eb90-d274-11e5-bf28-779c8998e810 --institution UChicago --sshpubstring 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCo3a7EUYD8qEwMBYlOzNFXXA55Lpcbgl5qlmiuwXdrOV/APr2uoIw3vYix4yYPTQPr8trfscX/NaDpVAhivlmd31ylGBjIaK/Qo0L2aTv38m9++dfflf9AdUtKdMIfddBNyOh5FlTzropoElvdVulJyGIJv6+rQeDMyaKt5HGOJ8yg+xtqcTDbfzHWVK2POP3PlcQsMg+5MkAJQDV2gvO3NxRF+ureedEtSmvEuJNUIGatM3l09FfbU9nOM9T+8xrz9tTJLMhB7QWXcd8V5IFMo+fCoSJG4qKPUrkqIHXvpNRmQ8CvEeVxwgHl/3R+Jtg8OYs7P5mmoKw4r+OBAYhL lincolnb@nam-shub' lincolnb

# create the allocation
echo "Creating allocation..."
$vc3client allocation-create --owner lincolnb --resource slate-condor --accountname centos --description "SLATE Condor" --displayname lincolnb-slate lincolnb.slate-condor

echo "Trying to get allocation public key.."
while true; do
  output=$($vc3client allocation-getpubtoken --allocationname lincolnb.slate-condor)
  if [[ $output == 'None' ]]; then
    echo "No output.. trying again in 5 seconds.."
    sleep 5
  else
    echo "Output looks okay.."
    break
  fi
done
echo "You will need to paste the following token into the remote cluster in ~/.ssh/authorized_keys:"
echo "<<<<<<<<<<<<<< TOKEN BEGINS >>>>>>>>>>>>>>>"
echo $output
echo "<<<<<<<<<<<<< TOKEN ENDS >>>>>>>>>>>>>>>>>>"
echo "Hit Enter once you have done this"
read

sleep 5
echo "Validating allocation..."
$vc3client allocation-validate --allocationname lincolnb.slate-condor

# create the project and add the allocation
echo "creating project and adding allocation..."
$vc3client project-create --owner lincolnb --members lincolnb lincolnb
$vc3client project-addallocation lincolnb lincolnb.slate-condor
$vc3client project-adduser lincolnb lincolnb


# create the virtual cluster template
echo "Creating virtual cluster template..."
$vc3client nodeset-create --owner lincolnb --node_number 1 --app_type htcondor --app_role worker-nodes --app_killorder newest --displayname="htcondor" lincolnb-htcondor-nodeset
$vc3client cluster-create --owner lincolnb --description "htcondor" --displayname="htcondor" lincolnb-htcondor-cluster --public
$vc3client cluster-addnodeset lincolnb-htcondor-cluster lincolnb-htcondor-nodeset

# create the head node template -- is this generated dynamically?
echo "Creating nodeset..."
#$vc3client nodeset-create --owner lincolnb --node_number 1 --app_type htcondor --app_role head-node --displayname="htcondor headnode" vc3-headnode-htcondor

# create the request
$vc3client request-create --owner lincolnb --cluster lincolnb-htcondor-cluster --project lincolnb --allocations lincolnb.slate-condor kube-test
