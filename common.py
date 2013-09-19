import sys
from subprocess import call

def quit(comm_server, lcd):
   comm_server.send_to_client("QUIT")
   call (["shutdown -h now"], shell=True)
   sys.exit()
