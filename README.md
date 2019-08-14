# README

# VC3 container documentation 

# Running the container
To start up the VC3 container, run the bash script runnew.sh. If the container was previously running, run the bash script delete.sh, and $docker stop vc3, and then rerun the bash script runnew.sh. runnew.sh should start the VC3 container, and while validating the allocation, the terminal output should show an SSH key, presented like this - 
You will need to paste the following token into the remote cluster in ~/.ssh/authorized_keys:



<<<<<<<<<<<<<< TOKEN BEGINS >>>>>>>>>>>>>>>

[your_key]

<<<<<<<<<<<<< TOKEN ENDS >>>>>>>>>>>>>>>>>>



You will need to open another terminal tab, and ssh into slate-micro-condor.slateci.io, with username centos and your private key. Open the authorized keys by using vi ~/.ssh/authorized_keys and append your ssh key to the file. 

Go back to the other tab, and press enter. After it finishes running you can view the logs by running $docker logs -f vc3. This should show all the logs that occurred while running the runnnew.sh script. The runnew.sh script has commands to create a request, and you can check that the login pod has been created by ssh'ing into the pod using the private key to the public key submitted in the request. You can check that the request terminate command works by using $docker exec -i vc3 vc3-client request-terminate --request-name [request_name]. The logs should indicate the success of this operation, and sshing into the login pod should no longer work. 


