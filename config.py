from os import environ

API_ID = int(environ.get("API_ID", "979826"))
API_HASH = environ.get("API_HASH", "238183386c30590d073b457166ba260d")
BOT_TOKEN = environ.get("BOT_TOKEN", "7511409204:AAGU9jBa0zIwtQwZBbQnTjtoI5BDWY1AzHM")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002636069197"))
ADMINS = int(environ.get("ADMINS", "1074804932"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://sainallamilli17:Animes3u@jra.bhuokyq.mongodb.net/?retryWrites=true&w=majority&appName=JRA") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "JRA")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
