from netmiko import ConnectHandler
from pprint import pprint
from netmiko.ssh_exception import AuthenticationException, NetMikoTimeoutException

router4 = {
	'device_type': 'cisco_ios_telnet',
	'host': '192.168.5.106',
	# "username": "admin",
	# "password": "cisco",
	# 'secret': 'cisco',
	'port': 32770}


def telnet_config(device):

	try:
		with ConnectHandler(**device) as router:
			print("Connecting to device", device)
			router.enable()
			router.config_mode()
			router.send_config_from_file('/Users/khuded/Documents/Python-Projects/Network-Projects/labx/router1.bgl')
			print("configuration successfulll...writing to memory")
			router.send_command('wr mem')


	except NetMikoTimeoutException:
		print(f'Unable to connect to {device1["host"]}')


if __name__ == "__main__":
	telnet_config(router4)
