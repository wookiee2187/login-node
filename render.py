from flask import Flask, flash, redirect, render_template, request
from random import randint

app = Flask(__name__)

@app.route("/")
def hello():
	temp_up = render_template('condor_config.local.j2', request_name = "request", inventory_hostname = "hostname")
#	print(temp_up)
#	file1 = open("templates/condor_config.local.j2","w")
 #       file1.write(temp_up)
  #      file1.close()
        f = open("condor_config.local","w+")
        f.write(temp_up)
        f.close()
	return temp_up
# render_template('condor_config.local.j2', request_name = "request", inventory_hostname = "hostname")

if __name__ == "__main__":
	app.run(debug=True)
