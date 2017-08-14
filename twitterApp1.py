import sys
from twython import Twython

CONSUMER_KEY = '***********************************************'
CONSUMER_SECRET = '********************************************'
ACCESS_KEY = '*************************************************'
ACCESS_SECRET = '**********************************************'


api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
mesaj="RaspberryPi dan gonderilen deneme mesajidir!"
api.update_status(status=mesaj)
print ("{} tweeti gonderildi").format(mesaj)
