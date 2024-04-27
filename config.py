import os

API_ID = API_ID = 24119778

API_HASH = os.environ.get("API_HASH", "cca11ca97dd8683d65ca1beb62baceb1")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6571673893:AAEDAoL8D-NAqOZ0oLW7RsL_5kOaseXQjwA")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7171191819))

LOG = -1002098346215

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7171191819").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


