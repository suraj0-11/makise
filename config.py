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

Config.AUTH_USERS = [6953453057,-1002037908910,1212386996,-1002038244305]
Config.API_ID = 5168062
Config.API_HASH = "04c049aa96d1cc87920b45b7fb43c0d0"
Config.BOT_TOKEN = "6519805517:AAFiX-NMkszvdThiwIplnFLHgDB78J_LbQw"
Config.REDIS_HOST = "" 
#redis-14044.c91.us-east-1-3.ec2.cloud.redislabs.com
Config.REDIS_PASS = "AB7X2pYjowMkLQqOuM1rhwmXqBgKoGpk"
#FEsHndW4SHTzcTJQWJYHpCDja6RmYnhf
REDIS_PORT = "19522"
#14044
#.

#.
