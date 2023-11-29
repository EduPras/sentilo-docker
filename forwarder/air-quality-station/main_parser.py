import requests
import logging
import urllib3
import json

redirect_url = "https://sentilo.td.utfpr.edu.br/data/toledo-pr@qualidade-ar/"
headers = {
	'Content-Type': 'application/json',
	'IDENTITY_KEY': '327328b2ada79ccda93ceb28b85869eb5f4a1360e2369c9db99d7298371ee29e'
}

urllib3.disable_warnings()
urllib3.connectionpool.log.disabled = True 

logger = logging.getLogger('PARSER')

def parser(json_message):
    try: 
        end_device_ids = json_message["end_device_ids"]
        device_id = end_device_ids["device_id"]
        # Treat timestamp to dd/MM/yyyyTHH:mm:ssZ
        date, hour = str(json_message["received_at"]).split('.')[0].split('T')
        date = date.split('-')
        date = '/'.join((date[2], date[1], date[0]))
        timestamp = 'T'.join((date, hour))

        # location
        uplink_message = json_message["uplink_message"]
        latitude = uplink_message["locations"]["user"]["latitude"]
        longitude = uplink_message["locations"]["user"]["longitude"]
        location = f'{latitude} {longitude}'
    except:
        logger.exception("Parser error")
    
    to_send = { "observations" : []}

    for key, value in uplink_message["decoded_payload"].items():
        if "Best" in key:
            continue
        if value != 'NaN':
            this_device = key
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
            # <comp_name>_<this_device>
            this_device = "air-quality-comp1_"+this_device
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