# README

# VC3 documentation 

The bash script runall.sh can start up a VC3 container, and volume mount a changed version of the HandleHeadNodes.py file which changes the OpenStack backend to a Kubernetes backend, and a tasks.conf file which has the location of the kubernetes config file. 
The HandleHeadNodes.py file is changed to remove all novaclient references and use the kubernetes python api instead. The function login_info searches for, and outputs pod info if it exists. If it does not, it returns an Exception. The function login_create creates a pod and its required resources to have an ssh CentOS container with HTCondor installed. 
