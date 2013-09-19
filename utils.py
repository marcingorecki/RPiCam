import time

def get_time():
  date = time.strftime("%Y-%b-%d", time.localtime())
  hour = time.strftime("%H:%M:%S", time.localtime())
  return date+"_"+hour

