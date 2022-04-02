def get_path():
	import os
	dir_path = '%s\\AirRadeRevorked\\' %  os.environ['APPDATA'] 
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)
	file_path = '%sconfig.ini' % dir_path
	return file_path
def set(option, value):
	from configparser import ConfigParser
	config = ConfigParser()
	config.read(get_path())
	try:
		config.add_section('options')
	except  Exception as e:
		print(e)
	config.set('options', option, value)
	with open(get_path(), 'w') as f:
		config.write(f)
def get(option):
	from configparser import ConfigParser
	config = ConfigParser()
	config.read(get_path())
	return config.get('options', option)
	
