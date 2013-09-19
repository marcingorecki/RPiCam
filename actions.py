import importlib

actions = [["photo","take_sync_photo","Press OK to take picture"],
           ["common","quit","Shutdown system"]]

def run_command(number, comm_server, lcd):
   cmd = actions[number]
   module = importlib.import_module(cmd[0])
   method = getattr(module,cmd[1])
   method(comm_server, lcd)

def get_text(number):
   return actions[number][2]

def get_count():
   return len(actions)
