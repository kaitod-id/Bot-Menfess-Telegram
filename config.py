from dotenv import load_dotenv
from os import getenv, path

load_dotenv() if not path.exists("local.env") else load_dotenv("local.env")


class Config:
    api_id = int(getenv("API_ID", "24465982"))
    api_hash = getenv("API_HASH", "2b3131b7d3f6a42bd4ae1ba3b58c11c4")
    bot_token = getenv("BOT_TOKEN", "6344639589:AAEIxPkMYUUr2K6PloxytU-CR-oeMYLeErU")
    log_channel = int(getenv("LOG_CHANNEL", "-1001930361818"))
    fsub_chid = int(getenv("FORCESUB_CHANNEL", "-1001825244023"))
    db_chid = int(getenv("DB_CHANNEL", "-1001930361818"))
    blacklisted_channel = [int(x) for x in getenv("BLACKLISTED_CHANNEL", "-1001965792519").split(",") if x is not None]
    channel1 = int(getenv("CHANNEL_1", "-1001825244023"))
    channel2 = int(getenv("CHANNEL_2", "-1001855788004"))
    channel3 = int(getenv("CHANNEL_3", "-1001802473399"))


config = Config()
