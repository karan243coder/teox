from os import environ


# BOT CONFIG
API_ID = environ.get("API_ID", 22469064)  # api id
API_HASH = environ.get("API_HASH", "c05481978a217fdb11fa6774b15cba32")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "7542241757:AAFlhvei4M5qpm1KQ6zdXnYhTkRuOAYOgC4")  # bot token

# REDIS
REDIS_HOST = environ.get("REDIS_HOST", "redis-14170.c309.us-east-2-1.ec2.redns.redis-cloud.com")  # redis host uri
REDIS_PORT = environ.get("REDIS_PORT", 14170)  # redis port
REDIS_PASSWORD = environ.get(
    "REDIS_PASSWORD", "CtOceSG35B2flDiOVB8Q33vm4viuF1EQ"
)  # redis password


ADMINS = [7328629001]
OWNER_ID = 7328629001  # Replace with your Telegram user ID
PRIVATE_CHAT_ID = -1002170811388  # CHAT WHERE YOU WANT TO STORE VIDEOS
USER_CHANNEL = -100
DUMP_CHANNEL = -100


# Config
COOKIE = environ.get("COOKIE", "PANWEB=1; csrfToken=tl2pqlIpZs-nq51FEEph_DW8; lang=en; TSID=3g9dXlXOottLSsQspciI9TLgJ3xdVY2m; __bid_n=18ea84278b11d086d64207; _ga=none; ndus=Yq7EMC3teHuiP-N36C2DBOIumBe6Fxt1NCf6es6w; browserid==H5Q7WeEh7u4Dhru6_RM96NUURbH7uwuPeAMiIjm4UCmk9ckdC2IS6TI04w0=; ndut_fmt=0783FEEEE10AA527370BA9BD3BFD896272C84225A1E2DFFBE420CE1B1BC7D99A; _ga_06ZNKL8C2E=none")
