from FakeSensor import *
from random import randint
from time import sleep

AIR_QUALITY_PROVIDER_TOKEN = '39f82fde822f86520259871b4ceaf91306da76583f1743a2004ebbdac7ac2d1b'
# Instantiating sensors

# - COMP1 sensors config
token = AIR_QUALITY_PROVIDER_TOKEN
provider_name  = 'AIR_QUALITY_PROVIDER'
location = '-24.73326751241871 -53.76481221537956'

comp1_temp_sensor = FakeSensor(token, provider_name, 'ESP32_1_TEMP_sensor', location)
comp1_pm10_sensor = FakeSensor(token, provider_name, 'ESP32_1_PM10_sensor', location)
comp1_CO2_sensor = FakeSensor(token, provider_name, 'ESP32_1_CO2_sensor', location)

# - COMP2 sensors config, same provider (token and name)
location = '-24.72461397949373 -53.74502484960853'

comp2_temp_sensor = FakeSensor(token, provider_name, 'ESP32_2_TEMP_sensor', location)
comp2_pm10_sensor = FakeSensor(token, provider_name, 'ESP32_2_PM10_sensor', location)
comp2_CO2_sensor = FakeSensor(token, provider_name, 'ESP32_2_CO2_sensor', location)

# (-1)^n
def gen_sign():
    return (-1)**randint(0,1)

# +x%*prev_value or -x%*prev_value
def gen_new_value(prev_value):
    # % varies between 0-8
    percentage = randint(0,8)/100
    return prev_value+(gen_sign()*percentage*prev_value)

# distorced value to the second component/sensor
def gen_distorced_value(src):
    return src+(gen_sign()*randint(0,5)/100*src)

# initing sensors values with average values
co2 = 600
pm10 = 40
temp = 27
while (True):
    co2 = gen_new_value(co2)
    pm10 = gen_new_value(pm10)
    temp = gen_new_value(temp)
    # CO2 sensor
    comp1_CO2_sensor.send_data(co2)
    comp2_CO2_sensor.send_data(gen_distorced_value(co2))
    # temp sensor
    comp1_temp_sensor.send_data(temp)
    comp2_temp_sensor.send_data(gen_distorced_value(temp))
    # pm10 sensor
    comp1_pm10_sensor.send_data(pm10)
    comp2_pm10_sensor.send_data(gen_distorced_value(pm10))
    sleep(5)