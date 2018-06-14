import os
import subprocess

#print(subprocess.check_call(['ping',"cisco.com"]))

def check_ping():
    hostname = "google.com"
    #response = os.system("ping " + hostname)
    response = subprocess.check_call(['ping',"cisco.com"])
    # and then check the response...
    if response == 1:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus

pingstatus = check_ping()
