import os
import dotenv
#import SmartEncoder.Database.db.myDB as db


dotenv.load_dotenv()

class Config(object):
  API_ID = int(os.environ.get("API_ID", 12345))
  API_HASH = os.environ.get("API_HASH")
  BOT_TOKEN = os.environ.get("BOT_TOKEN")
  AUTH_USERS = os.environ.get("AUTH_USERS")
  GOD = os.environ.get("GOD")
  REDIS_HOST = os.environ.get("REDIS_HOST")
 # REDIS_PORT = int(os.environ.get("REDIS_PORT", 12345))
  REDIS_PASS = os.environ.get("REDIS_PASS")
  DOWNLOAD_LOCATION = "downloads"

Config.AUTH_USERS = [6147004598, 6052965703,6953453057]
Config.API_ID = 3281305
Config.API_HASH = "a9e62ec83fe3c22379e3e19195c8b3f6"
Config.BOT_TOKEN = "6519805517:AAFF3KKXb0EYT1H8OLcREQeXc4p35HyYoJ4"
Config.REDIS_HOST = "redis-19522.c8.us-east-1-4.ec2.cloud.redislabs.com" 
#redis-14044.c91.us-east-1-3.ec2.cloud.redislabs.com
Config.REDIS_PASS = "AB7X2pYjowMkLQqOuM1rhwmXqBgKoGpk"
#FEsHndW4SHTzcTJQWJYHpCDja6RmYnhf
REDIS_PORT = "19522"
#14044
#.


#.
