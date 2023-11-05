import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = int(environ.get('API_ID', 4410228)) #API ID
API_HASH = environ.get('API_HASH', 'e73c6f2e8842acdeb8bf8c18628bb772') #API HASH
BOT_TOKEN = environ.get('BOT_TOKEN', '6581304256:AAEyZjt0e78ZBPLZAmQoIBGEyOSMP_Xp8PQ') #BOT TOKEN
DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://Cluster0:Cluster0@cluster0.c07xkuf.mongodb.net/?retryWrites=true&w=majority') #MONGO DB
OWNER_ID = int(environ.get('OWNER_ID', 1700825627)) #OWNER ID
MAIN_CHANNEL = int(environ.get('MAIN_CHANNEL', -1001650513858))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get('ARCHIVE_CHANNEL', -1001650513858))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get('MESSAGE_ID', -1001650513858)) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
