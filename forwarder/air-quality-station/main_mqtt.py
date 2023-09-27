User = "air-quality-station@ttn"
Password = "NNSXS.IOZFSLFWR6GE7DCCL2J2DVMT2XUIDMPRGLYP5UY.SFQG24GJR7HQACYMOVFFT766FFZPVYBTUDMJDKBIX2L62XK4CUVA"
User_password = "NNSXS.FD3O3OMZKXFE6KVDS3RNRNZUT47L4MVYLC7REBI.OJJRJQ5GIR2B4A22XYPRLDI64PXQOIEBXVMZD52VKZIIEBEIWADA"
Organization_password = "NNSXS.QEKN262SW4UOZ3OBQLKPUZDJPOY7OVGTL5RHRDQ.BEDDSFM5IOOP4EDUGVUBX63DQZQ6J77HK2RJHI243XXMXKJSVI2A"
Organization_id = "utfpr-td-lora"
theRegion = "AU1"		# The region you are using

# URL e header para requisição HTTP da organização na TTN
ttn_url = "https://eu1.cloud.thethings.network/api/v3/organizations/utfpr-td-lora/applications"
header_ttn = {
	"Authorization": "Bearer NNSXS.QEKN262SW4UOZ3OBQLKPUZDJPOY7OVGTL5RHRDQ.BEDDSFM5IOOP4EDUGVUBX63DQZQ6J77HK2RJHI243XXMXKJSVI2A"
}

import os, sys, logging

import paho.mqtt.client as mqtt
import json
import csv
from datetime import datetime
import requests
from main_parser import parser

logging.basicConfig(filename="forwarder.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logger = logging.getLogger('MQTT')

# MQTT event functions
def on_connect(mqttc, obj, flags, rc):
	if rc == 0:
		logger.info("Connected!")
		mqttc.subscribe("v3/+/devices/+/up", 0)
	elif rc == 1:
		logger.error("Connection refused - invalid client identifier")
	elif rc == 2:
		logger.error("Connection refused - invalid client identifier")
	elif rc == 3:
		logger.error("Connection refused - server unavailable")
	elif rc == 4:
		logger.error("Connection refused - bad username or password")
	elif rc == 5:
		logger.error("Connection refused - not authorised")

	# print("\nReturn code: " + str(rc))

def on_message(mqttc, obj, msg):
	logger.info("Message: " + msg.topic + " " + str(msg.qos)) # + " " + str(msg.payload))
	parser(json.loads(msg.payload))

def on_subscribe(mqttc, obj, mid, granted_qos):
	logger.info("Subscribe: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc, obj, level, string):
	print("\nLog: "+ string)
	logging_level = mqtt.LOGGING_LEVEL[level]
	logging.log(logging_level, string)

# Atualiza a lista de aplicações que a organização colabora
def get_apps(app_ids, clients):
	resp = requests.get(ttn_url, headers=header_ttn)
	parsedResp = json.loads(resp.text)["applications"]
	for item in parsedResp:
		new_app = item["ids"].get("application_id")
		# print("app_id %s" % new_app)
		if new_app not in app_ids:
			app_ids.append(new_app)
			# connects new app to a new MQTT client
	return

# Handling multiple clients - TODO
# app_ids = [] # Lista de aplicações que a organização é colaboradora
# clients = [] # Lista de clientes MQTT
# get_apps(app_ids, clients)

mqttc = mqtt.Client()

# Assign callbacks
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_message = on_message

mqttc.username_pw_set(User, Organization_password)
mqttc.connect("au1.cloud.thethings.network", 1883, 60)
mqttc.subscribe("v3/+/devices/+/up", 0)	# all device uplinks

try:
	mqttc.loop_forever(10)
except KeyboardInterrupt:
	mqttc.disconnect()
	logger.info("Exited with status 0")
	sys.exit(0)
except:
	logger.exception("Exited with status 1")
	mqttc.disconnect()
	sys.exit(0)