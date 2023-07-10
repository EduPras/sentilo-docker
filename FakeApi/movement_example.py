from FakeSensor import *
from random import randint
from time import sleep
import json

# It's necessary to create providers, components and tokens in sentilo catalog
UTF_PROVIDER_TOKEN = 'ff32e43fcc89a7a5022e37595cddfe69c55454f7d0a0b3a1d83844a458185103'

fake_temp_sensor1 = FakeSensor(UTF_PROVIDER_TOKEN, 'Utfpr-TD', 'Temp1', '-24.7259747 -53.760350')
fake_temp_sensor2 = FakeSensor(UTF_PROVIDER_TOKEN, 'Utfpr-TD', 'Temp2', '-24.7259747 -53.760350')

acc = 0
long = -53.760350
long2 = -53.760350 
while(True):
    rand = randint(10,35)

    long = long + 0.00001
    long2 = long2 - 0.00001
    fake_temp_sensor1.send_data(json.dumps({
        "observations":[{
            "value": json.dumps({
                "value": rand,
                "component": "COMP1"
            }),
            "location": "-24.7259747 " +str(long)
        }]
    }))
    fake_temp_sensor2.send_data(json.dumps({
        "observations":[{
            "value": json.dumps({
                "value": rand+4,
                "component": "COMP1"
            }),
            "location": "-24.7259747 " +str(long2)
        }]
    }))
    print(rand)
    sleep(5)