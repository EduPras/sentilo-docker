from FakeSensor import *
from random import randint
from time import sleep

PROVIDER_TOKEN = '4a648d1513fb6369dd5bdfc8095b8becf02b577d1118f73469c1cc4657e66a4c'

token = PROVIDER_TOKEN
provider_name  = 'Utfpr-TD'
location = '-24.73326751241871 -53.76481221537956'

comp1_temp_sensor = FakeSensor(token, provider_name, 'ESP32_1_TEMP_sensor', location)

while(True):
   temp = randint(10, 35) 
   comp1_temp_sensor.send_data(temp)
   sleep(5)

