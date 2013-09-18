from subprocess import call

def take_photo(seq):
  call (["raspistill -t 0 -n -o mg"+seq+".jpg"], shell=True)
  
def convert_photo():
  call (["convert mg.jpg -rotate 270 -resize 48x84\! -brightness-contrast 50 -colors 2 -monochrome photo.bmp"],shell=True)

