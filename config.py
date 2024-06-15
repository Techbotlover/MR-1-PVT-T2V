import os

API_ID = API_ID = 27560342

API_HASH = os.environ.get("API_HASH", "cd10f0b290f53f7c9a3f22c6cd788b60")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7291812440:AAHudgxXyYigFk2TF1jfCrezLCI1jZYDJFk")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6988460039))

LOG = -1002054181760

try:
    ADMINS=[7045457279]
    for x in (os.environ.get("ADMINS", "6988460039").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


