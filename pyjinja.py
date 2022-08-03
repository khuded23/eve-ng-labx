#!/usr/bin/python

import yaml
import json
from yaml.loader import SafeLoader
from pprint import pprint
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
from jinja2 import Template






with open('template.j2',mode='r') as file:
	#print(file.read())
	template = Template(file.read())


with open("device.yml") as f:
	data = yaml.load(f, Loader=SafeLoader)

	# for item in data['dc1']:
	# 	print(router_template.render((data['dc1'][item])))

	for dc in data:
		for item in data[dc]:
			site = (data[dc][item])
			with open(site['hostname'],'w') as config:
				config.write(template.render(site))
