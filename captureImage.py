#!/usr/bin/python
import time,datetime
import os

while 1:
  command="fswebcam -r 1024x768 images/"+time.strftime("%Y%m%d-%H%m%s")+".JPEG"
  output=os.system(command)
  time.sleep(5)

