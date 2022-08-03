from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime
from netmiko.ssh_exception import AuthenticationException, NetMikoTimeoutException
import yaml
from yaml.loader import SafeLoader
from pprint import pprint


class device():
	def __init__(self, device_type, host, port,filename):
		self.device_type = device_type
		self.host = host
		self.port = port
		self.file=filename
		self.secret = 'cisco'

		print(self.device_type)
		print(self.host)
		print(self.port)

		self.device = {'device_type': device_type,
		               'host': host,
		               'port': port,
		               'secret': self.secret}

		try:
			with ConnectHandler(**self.device) as router:
				print(f'connecting to {self.host}')
				# router.send_command(
				# 	expect_string= "% Please answer 'yes' or 'no'"
				# 	command_string = 'no'
				router.enable()
				router.config_mode()
				router.send_config_from_file(self.file)
				print("configuration successfulll...writing to memory")
				router.send_command('wr mem')


		except NetMikoTimeoutException:
			print(f'Unable to connect to {self.host} ')
		except AuthenticationException:

			print(f'Authentication failed {self.host}')

		except Exception as unknown_error:
			print(f'{unknown_error}Unknown error')

if __name__ == "__main__":

	bgl = '/Users/khuded/Documents/Python-Projects/Network-Projects/labx/router1.bgl'
	bom = '/Users/khuded/Documents/Python-Projects/Network-Projects/labx/router1.bom'
	sin = '/Users/khuded/Documents/Python-Projects/Network-Projects/labx/router1.sin'
	tky = '/Users/khuded/Documents/Python-Projects/Network-Projects/labx/router1.tky'

	BGL = device('cisco_ios_telnet','192.168.5.106','32770',bgl)
	BOM = device('cisco_ios_telnet','192.168.5.106','32773',bom)
	SIN = device('cisco_ios_telnet','192.168.5.106','32771',sin)
	TKY = device('cisco_ios_telnet','192.168.5.106','32772',tky)