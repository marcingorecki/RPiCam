import sys
from subprocess import call

def shutdown:
   call (["shutdown -h now"], shell=True)

def quit(comm_server, lcd):
   comm_server.send_to_client("QUIT")
   shutdown()
   sys.exit()
