import requests
import logging
import urllib3
import json

redirect_url = "http://localhost:8081/data/toledo-pr@coleta-rastreamento/"
headers = {
	'Content-Type': 'application/json',
	'IDENTITY_KEY': '0b54fe743e82dac27049c388615f49242dd2a52bab690eb732659f57e8db7ae3'
}

urllib3.disable_warnings()
urllib3.connectionpool.log.disabled = True 

TENANT = "toledo-pr"
logger = logging.getLogger('PARSER')

def parser(json_message):
    end_device_ids = json_message["end_device_ids"]
    device_id = end_device_ids["device_id"]
    # Treat timestamp to dd/MM/yyyyTHH:mm:ssZ
    date, hour = str(json_message["received_at"]).split('.')[0].split('T')

    date = date.split('-')
    date = '/'.join((date[2], date[1], date[0]))
    timestamp = 'T'.join((date, hour))

    # location
    uplink_message = json_message["uplink_message"]
    # latitude = uplink_message["locations"]["user"]["latitude"]
    # longitude = uplink_message["locations"]["user"]["longitude"]
    if uplink_message.get("decoded_payload", None) == None:
        logger.error("Cannot get decoded payload from " + str(device_id))
        return
    decoded_payload = uplink_message["decoded_payload"]
    if decoded_payload.get("altitude", None) != None and decoded_payload.get("latitude", None) != None:
        latitude = decoded_payload["latitude"]
        longitude = decoded_payload["longitude"]
        del decoded_payload["latitude"]
        del decoded_payload["longitude"]
    elif decoded_payload.get("lat", None) != None and decoded_payload.get("lon", None) != None:
        latitude = decoded_payload["lat"]
        longitude = decoded_payload["lon"]
        del decoded_payload["lat"]
        del decoded_payload["lon"]

    decoded_payload["coordinates"] = {
        "lat": latitude, 
        "lon": longitude
    }
        
    location = f'{latitude} {longitude}'
    
    to_send = { "observations" : []}

    # sensor name = <TENANT>@<device_id>
    to_send["observations"] = [{
        "value" : json.dumps(uplink_message["decoded_payload"]),
        "timestamp" : timestamp,
        "location": location
    }]
    # print(to_send)
    send_to_sentilo(device_id, to_send,to_send)
    return

def send_to_sentilo(sensor_id, body, value):
    sensor_url = redirect_url + sensor_id
    try:
        resp = requests.put(url=sensor_url, json=body, headers=headers, verify=False)
        print(resp.text)
        if resp.status_code == 200:
            logger.info("Uplink fowarded succesfully! sensor_id: " + str(sensor_id) + " - " + str(value))
        else:
            logger.warn("Uplink fowarded status code: " + str(resp.status_code))
    except:
        logger.exception("Uplink request error")
    return