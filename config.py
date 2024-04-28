import os

API_ID = API_ID = 27506873

API_HASH = os.environ.get("API_HASH", "a6e35f157348c804affcadece912fd30")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6963157086:AAE0KKLfMeN64GRFogr3jAimFN0DtzfvDqY")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6518807195))

LOG = -1002052344384

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6177195410").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


