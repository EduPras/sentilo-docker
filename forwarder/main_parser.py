import requests

redirect_url = "https://200.134.31.211/data/PM_station/"
headers = {
	'Content-Type': 'application/json',
	'IDENTITY_KEY': '01eb334b600c1b0ad3b7e7e552d5d4d473c7b0c971955d77b1b157441a1c7894'
}

def parser(json_message):
    end_device_ids = json_message["end_device_ids"]
    device_id = end_device_ids["device_id"]
    # Treat timestamp to dd/MM/yyyyTHH:mm:ssZ
    date, hour = str(json_message["received_at"]).split('.')[0].split('T')
    hour = hour.split(':')
    hour[0] = str(int(hour[0])-3)
    hour = ':'.join(hour)
    date = date.split('-')
    date = '/'.join((date[2], date[1], date[0]))
    timestamp = 'T'.join((date, hour))

    uplink_message = json_message["uplink_message"];
    to_send = { "observations" : []}

    for key, value in uplink_message["decoded_payload"].items():
        if value != 'NaN':
            this_device = device_id + "_" + key
            print(this_device)
            to_send["observations"] = [{
                "value" : value,
                "timestamp" : timestamp 
            }]
            send_to_sentilo(this_device, to_send)
    return

def send_to_sentilo(sensor_id, body):
    sensor_url = redirect_url + sensor_id
    try:
        resp = requests.put(url=sensor_url, json=body, headers=headers, verify=False)
        if resp.status_code == 200:
            print("[PARSER] Uplink fowarded succesfully!")
    except requests.exceptions.RequestException as e:
        print("[PARSER] Uplink request error")
        print(e)    
    return