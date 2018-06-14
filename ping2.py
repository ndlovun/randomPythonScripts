import os
import subprocess
import socket

import time
from datetime import timedelta

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ur_ip = s.getsockname()[0]

start_time = time.monotonic()

line = "*+"*20
print(line)
print('Your IP address is ', ur_ip)

ip_add = input("Enter IP or hostname to be pinged: ")

with open(os.devnull, 'w') as DEVNULL:
    try:
        # stdout=DEVNULL suppress output
        subprocess.check_call(['ping',ip_add],stdout=DEVNULL, stderr=DEVNULL)
        is_up = "UP"

    except subprocess.CalledProcessError:
        is_up = "DOWN"

print("Host ",ip_add, "is", is_up)

end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))
print(line)
