import redis
from redis import ConnectionPool

pool = ConnectionPool(host='localhost', port=6379, db=0)
# Une connexion
r = redis.Redis(connection_pool=pool)

# Plusieurs connexions
r1 = redis.Redis(connection_pool=pool)
r2 = redis.Redis(connection_pool=pool)