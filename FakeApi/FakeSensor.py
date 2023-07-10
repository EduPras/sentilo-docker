from dotenv import load_dotenv
import os
import requests
load_dotenv()

ID_KEY = os.getenv("ID_KEY")
URL_API = os.getenv("URL_API")

class FakeSensor:
    def __init__(self, provider_token, provider, sensor, location):
        self.sensor = sensor
        self.location = location
        self.provider_token = provider_token
        self.provider = provider
        self.headers = {
            "IDENTITY_KEY": self.provider_token
            # 'Content-Type': 'application/json'
        }

    def send_data(self, data):
        ## TODO request as json not working
        # json = {
        #     "observations":[{
        #         "value": data,
        #         "location": self.location
        #     }]
        # }
        # print(json)
        url = f'{URL_API}data/{self.provider}/{self.sensor}/{data}'
        r = requests.put(url=url, headers=self.headers, verify=False)
        print(f'\n\
        Text: {r.text}\n\
        Status code: {r.status_code}\n\
        Sensor: {self.sensor}\t value: {data}\n') 