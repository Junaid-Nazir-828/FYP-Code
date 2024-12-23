import configparser

config = configparser.ConfigParser()
config.read('config.ini')

url = config['CONFIGURATION']['URL']
relay_id = int(config['CONFIGURATION']['RELAY_ID'])

print(type(config['CONFIGURATION']['RELAY_ID']))
# if url == '' or relay_id == 'no':
#     print('ok')