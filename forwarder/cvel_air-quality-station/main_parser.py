import requests
import logging
import urllib3
import json

redirect_url = "https://sentilo.td.utfpr.edu.br/data/cascavel-pr@qualidade-ar/"
headers = {
	'Content-Type': 'application/json',
	'IDENTITY_KEY': '46984abdd5c39f8b0722a8f8f0382b803f091d59eee6470d4d2cee84b5253bb2'
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
        # default lat log at UTFPR-TD
        latitude = '-24.7330471'
        longitude = '-53.7663416'
        if uplink_message.get('locations'):
            latitude = uplink_message["locations"]["user"]["latitude"]
            longitude = uplink_message["locations"]["user"]["longitude"]
        elif uplink_message.get('rx_metadata')[0].get('location'):
            latitude = uplink_message['rx_metadata'][0]['location']['latitude']
            longitude = uplink_message['rx_metadata'][0]['location']['longitude']
        
        location = f'{latitude} {longitude}'
    
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
    except:
        logger.exception("Parser error")
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