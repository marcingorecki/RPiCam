from subprocess import call
import utils 

def take_photo(seq):
  call (["raspistill -t 0 -n -o mg"+seq+".jpg"], shell=True)

def take_sync_photo(comm_server, lcd):
  now = utils.get_time()
  comm_server.send_to_client(now)
  take_photo(now)  
  
def convert_photo():
  call (["convert mg.jpg -rotate 270 -resize 48x84\! -brightness-contrast 50 -colors 2 -monochrome photo.bmp"],shell=True)

