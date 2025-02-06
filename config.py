from os import environ


# BOT CONFIG
API_ID = environ.get("API_ID", 22469064)  # api id
API_HASH = environ.get("API_HASH", "c05481978a217fdb11fa6774b15cba32")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "-5UyRVl3BjAhZRY")  # bot token

# REDIS
REDIS_HOST = environ.get("REDIS_HOST", "redis-18689.c85.us-east-1-2.ec2.redns.redis-cloud.com")  # redis host uri
REDIS_PORT = environ.get("REDIS_PORT", 18689)  # redis port
REDIS_PASSWORD = environ.get(
    "REDIS_PASSWORD", "5bQedh5WnTg24cMb1DGeRjy1vQxT1cBx"
)  # redis password


ADMINS = [5071005351]
OWNER_ID = 5071005351  # Replace with your Telegram user ID
PRIVATE_CHAT_ID = -1002367641884  # CHAT WHERE YOU WANT TO STORE VIDEOS
USER_CHANNEL = -1002367641884
DUMP_CHANNEL = -1002367641884


# Config
COOKIE = environ.get("COOKIE", "PANWEB=1; csrfToken=tl2pqlIpZs-nq51FEEph_DW8; lang=en; TSID=3g9dXlXOottLSsQspciI9TLgJ3xdVY2m; __bid_n=18ea84278b11d086d64207; _ga=none; ndus=Yq7EMC3teHuiP-N36C2DBOIumBe6Fxt1NCf6es6w; browserid==H5Q7WeEh7u4Dhru6_RM96NUURbH7uwuPeAMiIjm4UCmk9ckdC2IS6TI04w0=; ndut_fmt=0783FEEEE10AA527370BA9BD3BFD896272C84225A1E2DFFBE420CE1B1BC7D99A; _ga_06ZNKL8C2E=none")
