name = 'neha'
sshpubstring = 'rand saads'
i =1000
string_to_append = '\n' + '    ' + str(name) +':x:' + str(i) + ':' + str(i) + '::'+ '/home/' + str(name) + ':' + '/bin/bash:' + str(sshpubstring)
print(string_to_append)
open("tconfig.yaml", "r")
contents =f.read()
f= open("newconf.yaml","w+")
f.write(open(tconfig.yaml,"r") + string_to_append)
