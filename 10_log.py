import logging
from datetime import datetime

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')
# logging.debug('aaaaaaa')
# logging.info('bbbbb')
# logging.warning('ccccc')
# logging.error('dddddd')
# logging.critical('eeeee')

# 터미널과 파일에 함께 로그 남기기
logFormatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

filename = datetime.now().strftime('mylogfile_%Y%m%d%H%M%S.log')
fileHandler = logging.FileHandler(filename, encoding='utf-8')
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug('aaaaaaa')
logger.info('bbbbb')
logger.warning('ccccc')
logger.error('dddddd')
logger.critical('eeeee')
