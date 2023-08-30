import requests
import logging
import urllib3
import json

redirect_url = "https://200.134.31.211/data/PM_station/"
headers = {
	'Content-Type': 'application/json',
	'IDENTITY_KEY': '792fbe84436b7ce917e488ff7a2f91667137a5f47be2833259628a15a09350d3'
}

urllib3.disable_warnings()
urllib3.connectionpool.log.disabled = True 

logger = logging.getLogger('PARSER')

def parser(json_message):
    end_device_ids = json_message["end_device_ids"]
    device_id = end_device_ids["device_id"]
    # Treat timestamp to dd/MM/yyyyTHH:mm:ssZ
    date, hour = str(json_message["received_at"]).split('.')[0].split('T')
    hour = hour.split(':')
    hour[0] = str(int(hour[0])-3)
    if (int(hour[0]) < 0):
        hour[0] = str(24 + int(hour[0]))
    hour = ':'.join(hour)
    date = date.split('-')
    date = '/'.join((date[2], date[1], date[0]))
    timestamp = 'T'.join((date, hour))

    # location
    uplink_message = json_message["uplink_message"]
    latitude = uplink_message["locations"]["user"]["latitude"]
    longitude = uplink_message["locations"]["user"]["longitude"]
    location = f'{latitude} {longitude}'
    
    to_send = { "observations" : []}

    for key, value in uplink_message["decoded_payload"].items():
        if value != 'NaN':
            this_device = device_id + "_" + key
            to_send["observations"] = [{
                "value" : json.dumps({
                    'raw_value': value,
                    'coordinates':{
                        'lat': latitude,
                        'lon': longitude
                    }
                }),
                "timestamp" : timestamp,
                "location": location
            }]
            print(to_send)
            send_to_sentilo(this_device, to_send, value)
    return

def send_to_sentilo(sensor_id, body, value):
    sensor_url = redirect_url + sensor_id
    try:
        resp = requests.put(url=sensor_url, json=body, headers=headers, verify=False)
        if resp.status_code == 200:
            logger.info("Uplink fowarded succesfully! sensor_id: " + str(sensor_id) + " - " + str(value))
        else:
            logger.warn("Uplink fowarded status code: " + str(resp.status_code))
    except:
        logger.exception("Uplink request error")
    return