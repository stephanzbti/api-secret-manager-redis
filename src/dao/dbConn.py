import redis
from decouple import config

redis_password = config('REDIS_PASSWORD', '')
redis_db = config('REDIS', 'localhost')

conn = redis.StrictRedis(host=redis_db, port=6379, db=0,
                         password=redis_password, decode_responses=True)

def connectionRedis():
    try:
        return conn
    except (redis.exceptions.ConnectionError, redis.exceptions.BusyLoadingError, redis.exceptions.AuthenticationError) as e:
        return(e)