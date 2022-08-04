import configparser
from loguru import logger


logger.add('./logs/log.log', level='WARNING')
logger.debug('Error')
logger.info('Information message')
logger.warning('Warning')

config = configparser.ConfigParser()
config.read('setting.ini')
